#
# Created By M Rumman Khan
# Project : Multiplicative Cipher
#
import os
while True:
	
	mode = input("Choose the mode: \n 1 - Encryption \n 2 - Decyption \n 0 - Exit \n")

	if mode == '1':
		str = input("Enter text to encrypt : ")
		k = 7 # Key
		ct = "" # Cipher Text initial
		c = ""
		for i in str:
			o = ord(i) - 65 # ASCII manipulation
			c = chr(((o * k) % 26) + 65)
			ct = ct + c
		print(ct)
		
	elif mode == '2':
		str = input("Enter text to decrypt : ")
		invk = 15  # inverse of Key i.e. 7
		ct = ""
		c = ""
		for i in str:
			o = ord(i) - 65
			c = chr(((o * invk) % 26) + 65)
			ct = ct + c
		print(ct)
	elif mode == '0':
		break
	else:
		print("Wrong Input! Try Again \n")
	