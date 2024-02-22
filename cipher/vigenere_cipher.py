from cipher.utils import Utils

class VigenereCipher:
    def __init__(self):
        self.utils = Utils()

    def generateKey(self, plain_text, key):
        i = 0
        old_key = key
        while len(key) < len(plain_text):
            key += old_key[i]
            i += 1
            if i >= len(old_key):
                i = 0
        return key

    def encrypt(self, plain_text, key):
        i = 0
        plain_text = plain_text.lower()
        plain_text = self.utils.clearString(plain_text)
        chipher_text = ''
        while i < len(plain_text):
            chipher_text += self.utils.intToChar((self.utils.charToInt(plain_text[i]) + self.utils.charToInt(key[i])) % 26)
            i += 1
        
        return chipher_text

    def decrypt(self, chipher_text, key):
        i = 0
        plain_text = ''
        while i < len(chipher_text):
            plain_text += self.utils.intToChar((self.utils.charToInt(chipher_text[i]) - self.utils.charToInt(key[i])) % 26)
            i += 1
        
        return plain_text
