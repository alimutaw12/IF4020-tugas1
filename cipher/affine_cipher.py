from cipher.utils import Utils

class AffineCipher:
    def __init__(self):
        self.utils = Utils()

    def computeGCD(self, x, y):
        gcd, _, _ = self.utils.extendedGcd(x, y)
                
        return gcd

    def encrypt(self, plain_text, key):
        b = 9
        i = 0
        plain_text = plain_text.lower()
        plain_text = self.utils.clearString(plain_text)
        chipher_text = ''
        while i < len(plain_text):
            int = (key * self.utils.charToInt(plain_text[i]) + b) % 26
            chipher_text += self.utils.intToChar(int)
            i += 1
        
        return chipher_text

    def decrypt(self, chipher_text, key):
        b = 9
        i = 0
        plain_text = ''
        inverse_modulo = self.utils.inverseModulo(key, 26)
        while i < len(chipher_text):
            int = (inverse_modulo * (self.utils.charToInt(chipher_text[i]) - b)) % 26
            plain_text += self.utils.intToChar(int)
            i += 1
        
        return plain_text
 
# n = 26

# print('Enter your key:')
# m = input()
# m = int(m)

# algo = AffineCipher()

# gcd = algo.computeGCD(n,m)

# while gcd != 1:
#     print('key is not valid')
#     print('Enter your key:')
#     m = input()
#     m = int(m)
#     gcd = algo.computeGCD(n,m)

# plain_text = 'pinjemduluseratus'

# chipher_text = algo.encrypt(plain_text, m)
# print(chipher_text)
# plain_text = algo.decrypt(chipher_text, m)
# print(plain_text)