__author__ = 'lorcan'


# get int from user
# get a base from user to convert int to
# get BASE_X string
# convert BASE_X string back to integer

# get int from user
myStr = input("Enter an integer to convert whatever base you want: ")
while myStr.isdigit() == False:
    print(
        "\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n     !!..OOPS DUMBASS, I asked for an integer..!!\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    myStr = input("\n\nThis time enter an INTEGER to convert whatever base you want: ")
else:
    myInt = int(myStr)

# get a base from user to convert int to
baseStr = input("\nChoose Base 2,8,16 to convert to: ")

if baseStr == '2':
    baseInt = int(baseStr)
elif baseStr == '8':
    baseInt = int(baseStr)
elif baseStr == '16':
    baseInt = int(baseStr)
else:
    print("\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n     !!..OOPS DUMBASS, I asked for an 2,8 or 16..!!\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    myStr = input("\n\nChoose Base 2,8,16 to convert to: ")


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
    print("\nBinary of {}: ".format(myStr), str(binStr))

if baseStr == '8':
    print("\nOctal of {}: ".format(myStr), str(binStr))

if baseStr == '16':
    print("\nHex of {}: ".format(myStr), str(binStr))

# convert BASE_X string back to integer

temp = binStr
power = 0
newInt = 0

while len(temp) > 0:
    bit = (temp[-1])
    if bit == 'A':
        bitInt = 10
    elif bit == 'B':
        bitInt = 11
    elif bit == 'C':
        bitInt = 12
    elif bit == 'D':
        bitInt = 13
    elif bit == 'E':
        bitInt = 14
    elif bit == 'F':
        bitInt = 15
    else:
        bitInt = int(bit)

    newInt += (bitInt * baseInt ** power)
    power += 1
    temp = temp[:-1]

if baseStr == '2':
    print("\nBinary number", binStr, "to integer: ", newInt)

if baseStr == '8':
    print("\nOctal number", binStr, "to integer: ", newInt)

if baseStr == '16':
    print("\nHex number", binStr, "to integer: ", newInt)


