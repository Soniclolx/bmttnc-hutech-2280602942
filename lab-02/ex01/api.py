
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
    text = request.json['text']
    key = request.json['key']
    decrypted_text = caesar_cipher.decrypt_text(text, key)
    return jsonify({'decrypted_text': decrypted_text})
#main function
if __name__ == '__main__':
    app.run(debug=True)