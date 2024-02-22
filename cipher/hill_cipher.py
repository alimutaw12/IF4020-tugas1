import numpy as np
from cipher.utils import Utils

class HillCipher:
    def __init__(self):
        self.utils = Utils()

    def encrypt(self, plain_text, matrix_key):
        k = 3
        while len(plain_text) % k != 0:
            plain_text += 'z'

        plain_text = plain_text.lower()
        plain_text = self.utils.clearString(plain_text)
        i = 0
        j = 0
        chipher_text = ''
        matrix = []
        while i < len(plain_text):
            matrix.append([self.utils.charToInt(plain_text[i])])
            i += 1
            j += 1
            if j >= k:
                j = 0
                m = np.dot(matrix_key, matrix)
                matrix = []
                for l in range(len(m)):
                    chipher_text += self.utils.intToChar(m[l][0] % 26)
                
        print('chiper_text')
        print(chipher_text)
        
        return chipher_text

    def decrypt(self, chipher_text, matrix_key):
        k = 3
        i = 0
        j = 0
        plain_text = ''
        matrix = []
        inverse_matrix = self.inverseMatrix(matrix_key)
        while i < len(chipher_text):
            matrix.append([self.utils.charToInt(chipher_text[i])])
            i += 1
            j += 1
            if j >= k:
                j = 0
                m = np.dot(inverse_matrix, matrix)
                matrix = []
                for l in range(len(m)):
                    plain_text += self.utils.intToChar(m[l][0] % 26)
        
        return plain_text

    def cofactorMatrix(self, matrix):
        num_rows, num_cols = matrix.shape
        cofactors = np.zeros((num_rows, num_cols))

        for i in range(num_rows):
            for j in range(num_cols):
                minor = np.delete(np.delete(matrix, i, axis=0), j, axis=1)
                cofactors[i, j] = (-1) ** (i + j) * np.linalg.det(minor)

        return cofactors

    def adjointMatrix(self, matrix):
        cofactors = self.cofactorMatrix(matrix)
        adjoint = cofactors.T

        return adjoint

    def determinant3x3(self, matrix):
        return int(np.linalg.det(matrix))

    def inverseMatrix(self, matrix):
        det = self.determinant3x3(matrix)
        det = det % 26

        inverse_modulo = self.utils.inverseModulo(det, 26)

        adjoint = self.adjointMatrix(matrix)

        num_rows, num_cols = adjoint.shape

        for i in range(num_rows):
            for j in range(num_cols):
                adjoint[i][j] = adjoint[i][j] % 26

        for i in range(num_rows):
            for j in range(num_cols):
                adjoint[i][j] = int(round((inverse_modulo * adjoint[i][j]) % 26))
            
        return adjoint.astype(np.int32)


# utils = self.utils.Utils()
# algo = HillCipher()

# matrix = np.array([[17, 17, 5], [21, 18, 21], [2, 2, 19]])

# chipher_text = algo.encrypt('paymoremoney', 3, matrix)
# print(chipher_text)
# plain_text = algo.decrypt(chipher_text, 3, matrix)
# print(plain_text)