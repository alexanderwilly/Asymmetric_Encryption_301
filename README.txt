Run in:
--> Python 3.10.12
--> ubuntu-22.04.3

Required files:
--> A1_encryption.py
--> A1_decryption.py
--> .txt files
--> "output" folder (created, if not exists, after A1_decryption.py is executed)

*Prerequisite:
- Make sure that .txt files are created within the same folder/directory as A1_encryption.py and A1_decryption.py
- Make sure that the terminal is on the A1_encryption.py and A1_decryption.py directory (execute the "pwd" command in the terminal to check the current directory, and "ls" to check files in the current terminal directory)
- Make sure that pycryptodome is installed (If not, execute this command in terminal: pip3 install pycryptodome)

How to run:
1. execute the encryption python program by executing "python3 A1_encryption.py"
	- The program will encrypt all .txt and its content into .enc files within the same directory of A1_encryption.py
2. execute the decryption python program by executing "python3 A1_decryption.py"
	- The program will create an "output" folder, if not exists
	- The program will decrypt all .enc files and their content into .txt files to the "output" folder