__author__ = 'lorcan'


# get int from user
# get a base from user to convert int to
# get BASE_X string
# convert BASE_X string back to integer

# get int from user
myStr = input("Enter an integer to convert binary: ")
myInt = int(myStr)

# get a base from user to convert int to
baseStr = input("\nChoose Base 2,8,16 to convert to: ")
baseInt = int(baseStr)

# get BASE_X string
binStr = ''

while myInt > 0:

    if myInt % baseInt == 10:
        binStr = 'A' + binStr
        myInt //= baseInt
    elif myInt % baseInt == 11:
        binStr = 'B' + binStr
        myInt //= baseInt
    elif myInt % baseInt == 12:
        binStr = 'C' + binStr
        myInt //= baseInt
    elif myInt % baseInt == 13:
        binStr = 'D' + binStr
        myInt //= baseInt
    elif myInt % baseInt == 14:
        binStr = 'E' + binStr
        myInt //= baseInt
    elif myInt % baseInt == 15:
        binStr = 'F' + binStr
        myInt //= baseInt
    else:
        binStr = str(myInt % baseInt) + binStr
        myInt //= baseInt

if baseStr == '2':
    print("\nBinary of {}: ".format(myStr),str(binStr))

if baseStr == '8':
    print("\nOctal of {}: ".format(myStr),str(binStr))

if baseStr == '16':
    print("\nHex of {}: ".format(myStr),str(binStr))

# convert BASE_X string back to integer

