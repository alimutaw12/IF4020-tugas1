import utils

utils = utils.Utils()

class AffineCipher:
    def computeGCD(self, x, y):
        gcd, _, _ = utils.extendedGcd(x, y)
                
        return gcd

    def encrypt(self, plain_text, m, b):
        i = 0
        plain_text = plain_text.lower()
        plain_text = utils.clearString(plain_text)
        chipher_text = ''
        while i < len(plain_text):
            int = (m * utils.charToInt(plain_text[i]) + b) % 26
            chipher_text += utils.intToChar(int)
            i += 1
        
        return chipher_text

    def decrypt(self, chipher_text, m, b):
        i = 0
        plain_text = ''
        inverse_modulo = utils.inverseModulo(m, 26)
        while i < len(chipher_text):
            int = (inverse_modulo * (utils.charToInt(chipher_text[i]) - b)) % 26
            plain_text += utils.intToChar(int)
            i += 1
        
        return plain_text
 
n = 26

print('Enter your key:')
m = input()
m = int(m)

algo = AffineCipher()

gcd = algo.computeGCD(n,m)

while gcd != 1:
    print('key is not valid')
    print('Enter your key:')
    m = input()
    m = int(m)
    gcd = algo.computeGCD(n,m)

b = 9

plain_text = 'pinjemduluseratus'

chipher_text = algo.encrypt(plain_text, m, b)
print(chipher_text)
plain_text = algo.decrypt(chipher_text, m, b)
print(plain_text)