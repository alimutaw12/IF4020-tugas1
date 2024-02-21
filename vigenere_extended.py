# Extended Vigenere for 256 ASCII char

def encrypt(plain_text, key):
    key = key.encode()
    cipher_text = bytearray()
    for i in range(len(plain_text)):
        key_index = key[i % len(key)]
        cipher = ((plain_text[i]) + key_index) % 256
        cipher_text.append(cipher)
    print(cipher_text[1])
    print(''.join(chr(i) for i in cipher_text))
    print("length: ", len(cipher_text))
    print(bytes(cipher_text))
    print("length: ", len(bytes(cipher_text)), "\n")
    return bytes(cipher_text)

def decrypt(cipher_text,key):
    plain_text = bytearray()
    for i in range(len(cipher_text)):
        key_index = key[i % len(key)]
        byte = ((cipher_text[i]) - ord(key_index)) % 256
        plain_text.append(byte)
    print(''.join(chr(i) for i in plain_text))
    print(bytes(plain_text))
    print("length: ", len(bytes(plain_text)), "\n")
    return bytes(plain_text)

# plain_text = "ç××ìãÛÏâáãÓñç"
with open("test.txt", 'rb') as file:
    plain_text = file.read()
key = "sony"
cipher_text = encrypt(plain_text, key)
decrypt(cipher_text, key)