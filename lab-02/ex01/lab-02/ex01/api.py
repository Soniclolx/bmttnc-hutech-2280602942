from cipher.transposition import TranspositionCipher
transposition_cipher = TranspositionCipher()
@app.route('/api/transposition/encrypt', methods=['POST'])
def transposition_encrypt():
    data = request.get_json()
    plain_text = data.get('plain_text')
    key = int(data.get('key'))
    encrypted_text = transposition_cipher.transposition_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})
@app.route('/api/transposition/decrypt', methods=['POST'])
def transposition_decrypt():
    data = request.get_json()
    cipher_text = data.get('cipher_text')
    key = int(data.get('key'))
    decrypted_text = transposition_cipher.transposition_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})
from cipher.railfence import RailFenceCipher
railfence_cipher = RailFenceCipher()
@app.route('/api/railfence/encrypt', methods=['POST'])
def encrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    encrypted_text = railfence_cipher.railfence_encrypt(cipher_text, key)
    return jsonify({'encrypted_text': encrypted_text})
@app.route('/api/railfence/decrypt', methods=['POST'])
def decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = railfence_cipher.railfence_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})
from cipher.playfair import PlayfairCipher
playfair_cipher = PlayfairCipher()
@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_creatematrix():
    data = request.json
    key = data['key']
    playfair_matrix = playfair_cipher.create_matrix(key)
    return jsonify({'matrix': playfair_matrix})
@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    playfair_matrix = playfair_cipher.create_matrix(key)
    encrypted_text = playfair_cipher.encrypt_text(plain_text, playfair_matrix)
    return jsonify({'encrypted_text': encrypted_text})
@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    playfair_matrix = playfair_cipher.create_matrix(key)
    decrypted_text = playfair_cipher.decrypt_text(cipher_text, playfair_matrix)
    return jsonify({'decrypted_text': decrypted_text})
from cipher.vigenere import VigenereCipher
vigenere_cipher = VigenereCipher()

@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    text = request.json['plain_text']
    key = request.json['key']
    encrypted_text = vigenere_cipher.vigenere_encrypt(text, key)
    return jsonify({'encrypted_text': encrypted_text})
@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    text = request.json['text']
    key = request.json['key']
    decrypted_text = vigenere_cipher.vigenere_decrypt(text, key)
    return jsonify({'decrypted_text': decrypted_text})

from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
app = Flask(__name__)
#caesar cipher algorithm
caesar_cipher = CaesarCipher()
@app.route('/encrypt', methods=['POST'])
def encrypt():
    text = request.json['plain_text']
    key = request.json['key']
    encrypted_text = caesar_cipher.encrypt_text(text, key)
    return jsonify({'encrypted_text': encrypted_text})
@app.route('/decrypt', methods=['POST'])
def caesar_decrypt():
    text = request.json['cipher_text']
    key = request.json['key']
    decrypted_text = caesar_cipher.decrypt_text(text, key)
    return jsonify({'decrypted_text': decrypted_text})
#main function
if __name__ == '__main__':
    app.run(debug=True)