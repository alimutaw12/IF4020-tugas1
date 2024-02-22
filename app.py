from flask import Flask, render_template, jsonify, request
import json
from cipher.vigenere_cipher import VigenereCipher
from cipher.vigenere_cipher_auto_key import VigenereCipherAutoKey
from cipher.affine_cipher import AffineCipher
from cipher.hill_cipher import HillCipher
from cipher.playfair import PlayfairCipher
from cipher.vigenere_extended import ExtendedVigenereCipher
import numpy as np

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    _form = request.json
    plain_text = _form['plainText']
    key = _form['key']
    cipher = _form['cipher']
    
    if (cipher == '1'):
        algo = VigenereCipher()
        key = algo.generateKey(plain_text, key)
    elif (cipher == '2'):
        algo = VigenereCipherAutoKey()
        key = algo.generateKey(plain_text, key)
    elif (cipher == '3'):
        algo = ExtendedVigenereCipher()
    elif (cipher == '4'):
        algo = PlayfairCipher()
    elif (cipher == '6'):
        matrixData = np.fromstring(key, dtype=int, sep=';')
        matrix = []
        idx = 0
        for i in range(len(matrixData)):
            matrixTemp = []
            for j in range(3):
                if idx < len(matrixData):
                    try:
                        element = int(matrixData[idx])
                        matrixTemp.append(matrixData[idx])
                    except ValueError:
                        data = { 
                            "chipherText" : 'Key harus integer', 
                            "key": key
                        } 
                        return jsonify(data)

                idx += 1
            if len(matrixTemp) == 3:
                matrix.append(matrixTemp)
            # print(matrix[i]) 
        
        print(matrix)
        if len(matrix) == 0:
            data = { 
                "chipherText" : 'Key tidak valid', 
                "key": key
            } 

            return jsonify(data) 

        matrix = np.array(matrix)
        num_rows, num_cols = matrix.shape

        k = 3
        if num_rows != k and num_cols != k:
            data = { 
                "chipherText" : 'Key tidak valid', 
                "key": key
            } 

            return jsonify(data) 

        algo = HillCipher()
        old_key = key
        key = matrix
    elif (cipher == '5'):
        algo = AffineCipher()
        try:
            key = int(key)
        except ValueError:
            data = { 
                "chipherText" : 'Key harus integer', 
                "key": key
            } 

            return jsonify(data)

        gcd = algo.computeGCD(26, key)

        if gcd != 1:
            data = { 
                "chipherText" : 'Key tidak valid', 
                "key": key
            } 

            return jsonify(data)
    else:
        algo = VigenereCipher()

    chipher_text = algo.encrypt(plain_text, key)
    if (cipher == '6'):
        key = old_key
    
    data = { 
        "chipherText" : chipher_text, 
        "key": key
    } 

    return jsonify(data)

@app.route('/decrypt', methods=['POST'])
def decrypt():
    _form = request.json
    plain_text = _form['plainText']
    key = _form['key']
    cipher = _form['cipher']
    
    if (cipher == '1'):
        algo = VigenereCipher()
        key = algo.generateKey(plain_text, key)
    elif (cipher == '2'):
        algo = VigenereCipherAutoKey()
        key = algo.generateKey(plain_text, key)
    elif (cipher == '3'):
        algo = ExtendedVigenereCipher()
    elif (cipher == '4'):
        algo = PlayfairCipher()
    elif (cipher == '6'):
        matrixData = np.fromstring(key, dtype=int, sep=';')
        matrix = []
        idx = 0
        for i in range(len(matrixData)):
            matrixTemp = []
            for j in range(3):
                if idx < len(matrixData):
                    try:
                        element = int(matrixData[idx])
                        matrixTemp.append(matrixData[idx])
                    except ValueError:
                        data = { 
                            "plainText" : 'Key harus integer', 
                            "key": key
                        } 
                        return jsonify(data)

                idx += 1
            if len(matrixTemp) == 3:
                matrix.append(matrixTemp)
            # print(matrix[i]) 
        
        print(matrix)
        if len(matrix) == 0:
            data = { 
                "plainText" : 'Key tidak valid', 
                "key": key
            } 

            return jsonify(data) 

        matrix = np.array(matrix)
        num_rows, num_cols = matrix.shape

        k = 3
        if num_rows != k and num_cols != k:
            data = { 
                "plainText" : 'Key tidak valid', 
                "key": key
            } 

            return jsonify(data) 

        algo = HillCipher()
        old_key = key
        key = matrix
    elif (cipher == '5'):
        algo = AffineCipher()
        try:
            key = int(key)
        except ValueError:
            data = { 
                "plainText" : 'Key harus integer', 
                "key": key
            } 

            return jsonify(data)

        gcd = algo.computeGCD(26, key)

        if gcd != 1:
            data = { 
                "plainText" : 'Key tidak valid', 
                "key": key
            } 

            return jsonify(data)
    else:
        algo = VigenereCipher()

    plain_text = algo.decrypt(plain_text, key)
    if (cipher == '6'):
        key = old_key

    data = { 
        "plainText" : plain_text, 
        "key": key
    } 

    return jsonify(data)

if __name__ == "__main__":
    app.run()