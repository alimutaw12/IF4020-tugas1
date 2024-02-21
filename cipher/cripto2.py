import utils

utils = utils.Utils()

plain_text = 'negarapenghasilminyakmentahdidunia!@#)()'
key = 'indo'

class VigenereCipherAutoKey:
    def generateKey(self, plain_text, key):
        i = 0
        while len(key) < len(plain_text):
            key += plain_text[i]
            i += 1
        return key

    def encrypt(self, plain_text, key):
        i = 0
        plain_text = plain_text.lower()
        plain_text = utils.clearString(plain_text)
        chipher_text = ''
        while i < len(plain_text):
            chipher_text += utils.intToChar((utils.charToInt(plain_text[i]) + utils.charToInt(key[i])) % 26)
            i += 1
        
        return chipher_text

    def decrypt(self, chipher_text, key):
        i = 0
        plain_text = ''
        while i < len(chipher_text):
            plain_text += utils.intToChar((utils.charToInt(chipher_text[i]) - utils.charToInt(key[i])) % 26)
            i += 1
        
        return plain_text

algo = VigenereCipherAutoKey()

key = algo.generateKey(plain_text, key)
chipher_text = algo.encrypt(plain_text, key)
print(chipher_text)
plain_text = algo.decrypt(chipher_text, key)
print(plain_text)
