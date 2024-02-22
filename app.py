from flask import Flask, render_template, jsonify, request
import json
from cipher.cripto import VigenereCipher
from cipher.cripto2 import VigenereCipherAutoKey
from cipher.cripto3 import AffineCipher
from cipher.playfair import PlayfairCipher
from cipher.vigenere_extended import ExtendedVigenereCipher

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

    plain_text = algo.decrypt(plain_text, key)
    data = { 
        "plainText" : plain_text, 
        "key": key
    } 

    return jsonify(data)

if __name__ == "__main__":
    app.run()