# Super encrypt is vigenere extended and transposition combined

import vigenere_extended
import transposition

def encrypt(plain_text, key):
    cipher_text = vigenere_extended.encrypt(plain_text, key)
    cipher_text = transposition.encrypt(cipher_text)
    print(cipher_text)
    return cipher_text

def decrypt(cipher_text, key):
    plain_text = transposition.decrypt(cipher_text)
    plain_text = vigenere_extended.decrypt(plain_text, key)
    print(plain_text)
    return plain_text

plain_text = "HOLIDAY IS MY BEST SPORT"
key = "BALI"
cipher_text = encrypt(plain_text, key)
decrypt(cipher_text, key)