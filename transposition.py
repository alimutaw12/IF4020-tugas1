import re

def encrypt(plain_text):
    key = 3
    # plain_text = plain_text.upper()
    # plain_text = re.sub('[^A-Z]+', '', plain_text)
    # plain_text = "".join(dict.fromkeys(plain_text))

    # add X to complete matrix
    while(len(plain_text) % key != 0):
        plain_text += 'X' 
    print(plain_text)
    
    # generate matrix
    row = len(plain_text) // key
    print(row)
    matrix = [[ord(plain_text[(j * key) + i])  for i in range(key)] for j in range(row)]
    print(matrix)

    cipher_text = bytearray()
    for j in range(key):
        for i in range(row):
            cipher_text.append(matrix[i][j])
    print(cipher_text)
    return cipher_text

def decrypt(cipher_text):
    key = 3
    # cipher_text = cipher_text.upper()

    # generate matrix
    row = len(cipher_text) // key
    matrix = [[cipher_text[(j * key) + i]  for i in range(key)] for j in range(row)]
    print(matrix)

    plain_text = bytearray()
    for j in range(key):
        for i in range(row):
            plain_text.append(matrix[i][j])
    print(plain_text, "\n \n")
    return plain_text

plain_text = "ç××ìãÛÏâáãÓñç"
cipher_text = encrypt(plain_text)
decrypt(cipher_text)