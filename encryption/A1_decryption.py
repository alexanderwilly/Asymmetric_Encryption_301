# Name = Alexander Willy Johan
# UOW ID = 7907795

from base64 import b64decode
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Util.Padding import unpad
import glob
import subprocess
import os

def find_folders(pattern):
	folders = [folder for folder in glob.glob(pattern) if os.path.isdir(folder)]
	return folders
	

def create_folder():
	isExist = False
	folders = find_folders("*")
	for folder in folders:
		isExist = True if folder == "output" else False
	
	if not isExist:
		subprocess.call("mkdir output", shell=True)
		print(" ==> output folder successfully created\n")


def decrypt_enc_key(private_key, enc_key):
	cipher_rsa = PKCS1_OAEP.new(private_key)
	return cipher_rsa.decrypt(enc_key)

	
def decrypt_file(cipher, ct_bytes, filename):
	try:
		# Decrypt message
		result = unpad(cipher.decrypt(ct_bytes), AES.block_size).decode('utf-8')
		
		
		# Write into new file (for output)
		file_out_name = filename.split(".enc")[0]
		file_out_name = "result_{}.txt".format(file_out_name)
		file_out = open("output/{}".format(file_out_name), "w")
		file_out.write(result)
		file_out.close()
		
		print(" ===> Decrypted message in {} is =\n{}".format(filename, result), end="")
		print(" ===> Decrypt {} to {} is done!".format(filename, file_out_name))
		
	except ValueError:
		print("Incorrect decryption")
	except KeyError:
		print("Incorrect key")
	

def main():
	# Check if output folder exists
	create_folder()

	# Obtain private key
	private_key = RSA.import_key(open("sk_bob.pem").read())
	
	

	# Obtain enc_key (c1)
	file_in = open("enc_key.bin", "rb")
	enc_key = file_in.read(private_key.size_in_bytes())
	file_in.close()
	
	
	# Obtain key
	k = decrypt_enc_key(private_key, enc_key)
	
	
	
	for filename in glob.glob("*.enc"):
		# Get encrypted files and it's encrypted text
		file_in = open(filename, "rb")
		iv = file_in.read(AES.block_size)
		ct = file_in.read()
		file_in.close()
		
		# Obtain cipher
		cipher = AES.new(k, AES.MODE_CBC, iv)
		
		# Decrypt file
		decrypt_file(cipher, ct, filename)
		
		print()
	

main()
