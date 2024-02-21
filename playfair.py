import re
import string
import numpy as np

alphabet = list(string.ascii_uppercase)

def generateKeyMatrix(key):
    key = key.upper()
    key = re.sub('[^A-Z]+', '', key)
    key = "".join(dict.fromkeys(key))
    for i in alphabet:
        if i not in key:
            key += i
    key = key.replace('J','')
    key_matrix = [[key[(j * 5) + i]  for i in range(5)] for j in range(5)]
    return key_matrix

def addX(plain_text):
    # add X to possible duplicate bigram
    for i in range(len(plain_text) - 1):
        if  (i % 2 != 1) and (plain_text[i] == plain_text[i+1]):
            plain_text = plain_text[:i+1] + 'X' + plain_text[i+1:]
    # add X for plain text with odd number of characters
    if len(plain_text) % 2 == 1:
        plain_text += 'X'
    return plain_text
    
def generateBigram(text):
    bigram_array = []
    for i in range(len(text) - 1):
        if  (i % 2 != 1):
            bigram_array.append((text[i], text[i + 1]))
    return bigram_array

def encrypt(plain_text, key):
    plain_text = plain_text.upper()
    plain_text = re.sub('[^A-Z]+', '', plain_text)
    plain_text = plain_text.replace('J','I')
    plain_text = addX(plain_text)
    print(plain_text)
    bigram_array = generateBigram(plain_text)
    print(bigram_array)

    key_map = np.array(generateKeyMatrix(key))
    cipher_text = ''

    for i in range(len(bigram_array)):
        indexA = np.where(key_map == (bigram_array[i][0]))
        rowA = indexA[0][0]
        colA = indexA[1][0]
        indexB = np.where(key_map == (bigram_array[i][1]))
        rowB = indexB[0][0]
        colB = indexB[1][0]

        # if same row
        if (rowA == rowB):
            if (colA < 4):
                cipher_text += key_map[rowA][colA + 1]
            else:
                cipher_text += key_map[rowA][0]

            if (colB < 4):
                cipher_text += key_map[rowB][colB + 1]
            else:
                cipher_text += key_map[rowB][0]

        # if same column
        elif (colA == colB):
            if (rowA < 4):
                cipher_text += key_map[rowA + 1][colA]
            else:
                cipher_text += key_map[0][colA]

            if (rowB < 4):
                cipher_text += key_map[rowB + 1][colB]
            else:
                cipher_text += key_map[0][colB]

        # else
        else:
            cipher_text += key_map[rowA][colB]
            cipher_text += key_map[rowB][colA]

    return cipher_text

def removeX(cipher_text):
    if (len(cipher_text) % 2 == 0) and (cipher_text[len(cipher_text) - 1] == 'X'):
        cipher_text = cipher_text[:-1]
    for i in range(len(cipher_text) - 1):
        if (cipher_text[i] == 'X') and (cipher_text[i-1] == cipher_text[i+1]):
            cipher_text = cipher_text.replace('X', '') 
    return cipher_text

def decrypt(cipher_text, key):
    bigram_array = generateBigram(cipher_text)
    print(bigram_array)
    key_map = np.array(generateKeyMatrix(key))
    plain_text = ''

    for i in range(len(bigram_array)):
        indexA = np.where(key_map == (bigram_array[i][0]))
        rowA = indexA[0][0]
        colA = indexA[1][0]
        indexB = np.where(key_map == (bigram_array[i][1]))
        rowB = indexB[0][0]
        colB = indexB[1][0]

        # if same row
        if (rowA == rowB):
            if (colA > 0):
                plain_text += key_map[rowA][colA - 1]
            else:
                plain_text += key_map[rowA][4]

            if (colB > 0):
                plain_text += key_map[rowB][colB - 1]
            else:
                plain_text += key_map[rowB][4]

        # if same column
        elif (colA == colB):
            if (rowA > 0):
                plain_text += key_map[rowA - 1][colA]
            else:
                plain_text += key_map[4][colA]

            if (rowB > 0):
                plain_text += key_map[rowB - 1][colB]
            else:
                plain_text += key_map[4][colB]

        # else
        else:
            plain_text += key_map[rowA][colB]
            plain_text += key_map[rowB][colA]

        plain_text = removeX(plain_text)
        # plain_text = plain_text.replace("I", "J")

    return plain_text

plain_text = "temui ibu nanti malam!@#$%^&*"
# plain_text = "anbaac"
key = "JALAN GANESHA SEPULUH!!!!!"
print("key matrix: \n", generateKeyMatrix(key))
cipher_text = encrypt(plain_text, key)
print("cipher teks: ", cipher_text, "\n")
print("plain teks: ", decrypt(cipher_text, key))