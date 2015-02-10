__author__ = 'lorcan'

"""
LAB 4 - Encryption
1 get user to input str
2 get int value of each chr
3 add 1 to each letter
4 reverse

"""

# get user to input str

myStr = input("Enter plaintext to be encrypted: ")

print("\nEncrypting: {}\n".format(myStr))

# get int value of each chr

temp = myStr
newStr = ''

while len(temp) > 0:
    # get int value of each chr
    bit = (temp[-1])
    # add 1 to each letter
    enChrInt = ord(bit) + 1
    enChr = chr(enChrInt)
    newStr += enChr
    print(bit, "->", enChr)
    temp = temp[:-1]

print("\n\nEncrypted string is: ", newStr)

