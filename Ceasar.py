# This script Encripts and Decripts usind the Ceasar Cipher technique

#CREATED BY FAD-X

#COPY, MODIFY, USE AND LEARN :)

#You can download the pyperclip module manually and place it in the same folder if your module imstaller can't find it

# On Linux, simply "wget http://invpy.com/pyperclip.py'

#Windows or any other os, simply visit http://invpy.com/pyperclip.py, download and move it to the required folder

#import pyperclip

message = input("Type or Paste the data to be encrypted or decrypted below \n")

key = int(input("Enter the key value (NUMBERS ONLY!!!)"))

mode = int(input("1). Encrypt \n2). Decrypt \n Choose here__: "))

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

translated = " "

message = message.upper()

for symbol in message:

	if symbol in LETTERS:		num = LETTERS.find(symbol)

		

		if mode == 1:

			num = num + key	

		elif mode == 2:

			num = num - key

		

		if num >= len(LETTERS):

			num = num - len(LETTERS)

		elif num < 0:

			num = num + len(LETTERS)

		translated = translated + LETTERS[num]

	else:

		translated = translated + symbol

		

print(translated)

#pyperclip.copy(translated)
