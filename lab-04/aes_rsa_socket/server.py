from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad,unpad
import socket
import threading
import hashlib      

#intialize server socket
server_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(5)

#generate RSA key pair
server_key = RSA.generate(2048)
 
 #list of connected clients
clients = []

#function to encrypt message
def encrypt_message(key, message):
    cipher = AES.new(key, AES.MODE_CBC)
    cipher_text = cipher.encrypt(pad(message.encode(), AES.block_size))
    return cipher.iv + cipher_text

#function to decrypt message
def decrypt_message(key, message):
    iv = encrypt_message[:AES.block_size]
    cipher_text = encrypt_message[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return decrypt_message.decode()

#function to handle client connection
def handle_client(client_socket, client_address):
    print(f"Connection with {client_address}")
    #send server's public key to client
    client_socket.send(server_key.publickey().export_key(format='PEM'))
    #receive client's public key
    client_received_key = RSA.import_key(client_socket.recv(2048))
    #generate AES key
    aes_key = get_random_bytes(16)
    #encrypt AES key with client's public key   
    cipher_rsa = PKCS1_OAEP.new(client_received_key)
    encrypted_aes_key = cipher_rsa.encrypt(aes_key)
    client_socket.send(encrypted_aes_key)

    #add client to the list
    clients.append((client_socket,aes_key))
    while True:
        encrypt_message = client_socket.recv(1024)
        decrypt_message = decrypt_message(aes_key, encrypt_message)
        print(f"Received from {client_address} : {decrypt_message}")

        #send recieved message to all clients
        for client in clients:
            if client != client_socket:
                encrypted = encrypt_message(client[1], decrypt_message)
                client.send(encrypted)
            if decrypt_message == "exit":
                break
        clients.remove((client_socket, aes_key))
        client_socket.close()
        print(f"Connection with {client_address} closed")

    #accept client connections
while True:
    client_socket, client_address = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()