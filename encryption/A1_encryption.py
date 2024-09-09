# Name = Alexander Willy Johan
# UOW ID = 7907795

from base64 import b64encode
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Util.Padding import pad
import glob


def generate_symmetric_key():
	# Generate Random Symmetric Key
	return get_random_bytes(16)

def generate_pk_sk(name):
	key = RSA.generate(2048)
	
	# Generate Private Key
	private_key = key.export_key()
	file_out = open("sk_{}.pem".format(name), "wb")
	file_out.write(private_key)
	file_out.close()
	print(" ==> Done generating {}'s secret key ".format(name))
	
	# Generate Public Key
	public_key = key.publickey().export_key()
	file_out = open("pk_{}.pem".format(name), "wb")
	file_out.write(public_key)
	file_out.close()
	print(" ==> Done generating {}'s public key ".format(name))
	
def generate_aes_cipher(key):
	cipher = AES.new(key, AES.MODE_CBC)
	print(" ==> Done generating aes cipher")
	
	return cipher
	
	
def encrypt_key(public_key, key):
	# Get C1 (encrypted key)
	cipher_rsa = PKCS1_OAEP.new(public_key)
	enc_data = cipher_rsa.encrypt(key)

	# Send C1
	file_out = open("enc_key.bin", "wb")
	file_out.write(enc_data)
	file_out.close()
	print(" ==> Done encrypting key ")


def encrypt_file(key, filename):
	cipher = generate_aes_cipher(key)
	
	# Encrypt File
	enc_file_name = "{}.enc".format(filename.split(".txt")[0])
	
	file_in = open(filename, 'rb')
	plain_data = file_in.read()
	file_in.close()
	ct_bytes = cipher.encrypt(pad(plain_data, AES.block_size))
	
	file_out = open(enc_file_name, 'wb')
	file_out.write(cipher.iv)
	file_out.write(ct_bytes)
	file_out.close()
	print(" ==> Done encrypting {} to {}".format(filename, enc_file_name))
	
	
	
def main():
	# Generate Two Pairs of Public Key and Secret Key
	generate_pk_sk("alice")
	generate_pk_sk("bob")
	
	# Generate Symmetric Key
	key = generate_symmetric_key()
	
	# Encrypt Symmetric Key
	public_key = RSA.import_key(open("pk_bob.pem").read())
	encrypt_key(public_key, key)
	
	
	# Encrypt Files
	for filename in glob.glob("*.txt"):
		encrypt_file(key, filename)
		print()






main()
