#
# Created by M Rumman Khan
# Project : Ceaser Cipher
#
str =  input("Enter Plain text to encrypt : ")
k = -2
ct = ""
for i in str:
	o = ord(i)
	ct = ct + chr(o+k)
print("dexrypted text: "+ ct)


