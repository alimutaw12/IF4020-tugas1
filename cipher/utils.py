import re

class Utils:
    def charToInt(self, char):
        return ord(char) % 97

    def intToChar(self, int):
        int += 97
        return chr(int)
    
    def clearString(self, string):
        regex = re.compile('[^a-zA-Z]')
        return regex.sub('', string)

    def extendedGcd(self, a, b):
        if a == 0:
            return b, 0, 1
        else:
            gcd, x, y = self.extendedGcd(b % a, a)
            return gcd, y - (b // a) * x, x

    def inverseModulo(self, a, m):
        gcd, x, _ = self.extendedGcd(a, m)
        if gcd != 1:
            raise ValueError(f"{a} tidak memiliki invers modulo dalam modulus {m}")
        else:
            return x % m