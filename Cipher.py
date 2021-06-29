# Name: Alice Liang
# EID: axl84
# Unique Section Number: 84825
# Assignment: #2
# Date: 6/13/20

# Input: strng is a string of 100 or less of upper case, lower case, and digits
# Output: function returns an encrypted string
from math import sqrt


def encrypt(strng):

    l = len(strng)
    k = findNextSquareRoot(l)

    # convert string to 2D array
    rows, cols = (k, k)
    matrix = [['*' for i in range(cols)] for j in range(rows)]

    index = 0
    for i in range(k):
        for j in range(k):
            if index < l:
                matrix[i][j] = strng[index]
                index += 1

    # rotate matrix clockwise
    r, c = (k, k)
    rotatedM = [['*' for i in range(c)] for j in range(r)]

    for i in range(k):
        for j in range(k):
            rotatedM[j][k-1-i] = matrix[i][j]

    # convert rotated matrix to encrypted string
    stringEnc = ""
    for i in range(k):
        for j in range(k):
            if rotatedM[i][j] != '*':
                stringEnc += rotatedM[i][j]

    return stringEnc

# Input: strng is a string of 100 or less of upper case, lower case, and digits
# Output: function returns an encrypted string


def decrypt(stringQ):

    l = len(stringQ)
    k = findNextSquareRoot(l)

    # convert string to 2D array
    rows, cols = (k, k)
    matrix = [['*' for i in range(cols)] for j in range(rows)]

    index = 0
    for i in range(k):
        for j in range(k):
            revIndex = k*(k-1-j)+i

            if revIndex < l and index < l:
                matrix[i][j] = stringQ[index]
                index += 1

    # rotate matrix counter clockwise
    r, c = (k, k)
    rotatedM = [['*' for i in range(c)] for j in range(r)]

    for i in range(k):
        for j in range(k):
            rotatedM[i][j] = matrix[j][k-1-i]

    # convert rotated matrix to dencrypted string
    stringDec = ""
    for i in range(k):
        for j in range(k):
            if rotatedM[i][j] != '*':
                stringDec += rotatedM[i][j]

    return stringDec


def findNextSquareRoot(num):

    root = sqrt(num)
    intRoot = int(root)
    if intRoot * intRoot < num:
        intRoot += 1

    return intRoot


def main():

    # open file cipher.in and read strings
    infile = open("encrypt.txt", "r")

    n = int(infile.readline().strip())

    if n < 1 or n > 100:
        return "invalid N: 1 <= N <= 100"

    encryptMsgs = list()
    for i in range(n):
        string = infile.readline().strip()
        lenOfStr = len(string)
        # ensure strng is between 1 and 100 characters (inclusive)
        if lenOfStr >= 1 and lenOfStr <= 100:
            # encrypt the string P
            encryptP = encrypt(string)
            encryptMsgs.append(encryptP)
        else:
            print("invalid string: ", string)

    infile.close()

    # open file encrypt.out and write the encrypted string list
    outfile = open("encrypt.out", "w")
    for i in range(len(encryptMsgs)):
        outfile.write(encryptMsgs[i] + "\n")
    outfile.close()

    return encryptMsgs


if __name__ == "__main__":
    main()
