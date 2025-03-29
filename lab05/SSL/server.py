import socket
import ssl
import threading

server_address = ('localhost', 12345)

client = []

def handle_client(client_socket):
    client.append(client_socket)
    
    print("Da ket noi voi", client_socket.getpeername())
    
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print("Nhan: ", data.decode())
            for c in client:
                try:
                    c.send(data)
                except:
                    client.remove(c)
    except:
        client.remove(client_socket)
    finally:
        print("Ngat ket noi voi", client_socket.getpeername())
        client.remove(client_socket)
        client_socket.close()
        
    
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)
server_socket.listen(5)

print("Dang cho ket noi...")

while True:
    client_socket, client_address = server_socket.accept()
    
    context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    context.load_cert_chain(certfile="./Certificates/server-cert.crt", keyfile="./Certificates/server-key.key")
    
    ssl_socket = context.wrap_socket(client_socket, server_side=True)   
    
    client_thread = threading.Thread(target=handle_client, args=(ssl_socket,))
    client_thread.start()