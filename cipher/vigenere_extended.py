# Extended Vigenere for 256 ASCII char
class ExtendedVigenereCipher:
    def encrypt(self, plain_text, key):
        key = key.encode()
        cipher_text = bytearray()
        for i in range(len(plain_text)):
            key_index = key[i % len(key)]
            cipher = (ord((plain_text[i])) + key_index) % 256
            cipher_text.append(cipher)
        result = ''.join(chr(i) for i in cipher_text)
        return result

    def decrypt(self, cipher_text, key):
        key = key.encode()
        plain_text = bytearray()
        for i in range(len(cipher_text)):
            key_index = key[i % len(key)]
            byte = (ord(cipher_text[i]) - key_index) % 256
            plain_text.append(byte)
        result = ''.join(chr(i) for i in plain_text)
        return result

# plain_text = "ç××ìãÛÏâáãÓñç"
# algo = ExtendedVigenereCipher()
# # with open("test.txt", 'rb') as file:
# #     plain_text = file.read()
# key = "sony"
# cipher_text = algo.encrypt(plain_text, key)
# print(cipher_text)
# print(algo.decrypt(cipher_text, key))