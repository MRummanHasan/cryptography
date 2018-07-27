#
# Created By M Rumman Khan
# Project : Affine Cipher
#


str = input("Enter text to encrypt : ")
k1 = 7
k2 = 2
ct = ""
c=""
for i in str:
	o = ord(i) - 65
	print(o * k1)
	c = chr(((o*k1+k2)%26)+65)
	ct = ct + c
print(ct)
