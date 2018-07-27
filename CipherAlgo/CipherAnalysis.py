#
# Created By M Rumman Khan
# Project : Ciphers Analysis
# Description : Traditional Ciphers with Analysis
#
import os


# Ceaser Cipher
def ceaserCipher():
	str = input("Enter Plain text to encrypt : ")
	k = -2
	ct = ""
	for i in str:
		o = ord(i)
		ct = ct + chr(o + k)
	print("encrypted text: " + ct)


# def egcd(a, b):
#     if a == 0:
#         return (b, 0, 1)
#     else:
#         g, y, x = egcd(b % a, a)
#         return (g, x - (b // a) * y, y)
#
# def modinv(a, m):
#     g, x, y = egcd(a, m)
#     if g != 1:
#         raise Exception('modular inverse does not exist')
#     else:
#         return x % m
#
# Multiplicative Cipher
def MultiCipher():
	str = input("Enter Plain Text to Manipulate : ")
	k = 7  # Key
	ct = ""  # Cipher Text initial
	c = ""
	for i in str:
		o = ord(i) - 65  # ASCII manipulation
		c = chr(((o * k) % 26) + 65)
		ct = ct + c
	print("Encrypted : " + ct)
	
	invk = 15  # inverse of Key i.e. 7
	ct = ""
	c = ""
	for i in str:
		o = ord(i) - 65
		c = chr(((o * invk) % 26) + 65)
		ct = ct + c
	print("Decrypted : " + ct)

def affineCipher():
	# Affine Cipher
	str = input("Enter text to encrypt : ")
	k1 = 7
	k2 = 2
	ct = ""
	c = ""
	for i in str:
		o = ord(i) - 65
		print(o * k1)
		c = chr(((o * k1 + k2) % 26) + 65)
		ct = ct + c
	print("Encrypted :" + ct)


ans = True
while ans:
	print("""
    1.Ceaser
    2.Multiplicative
    3.Affine
    4.Exit
    """)
	ans = input("What would you like to do? ")
	if ans == "1":
		ceaserCipher()
	elif ans == "2":
		MultiCipher()
	elif ans == "3":
		affineCipher()
	elif ans == "4":
		print("\n Goodbye")
		break
	elif ans != "":
		print("\n Not Valid Choice Try again")