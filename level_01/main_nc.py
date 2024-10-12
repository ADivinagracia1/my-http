import socket
import time

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 8080

my_server_potato = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # initialize the socket
my_server_potato.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # improves performance to close socket when done
my_server_potato.bind((SERVER_HOST, SERVER_PORT)) # bind server to IP address 
my_server_potato.listen(5)
print(f"Listening on port {SERVER_PORT} ...")

while True:
    client_socket, client_address = my_server_potato.accept()
    request = client_socket.recv(1024).decode()
    headers = request.split('\n')
    http_method, http_path, http_version = headers[0].split(" ")

    if http_method == 'GET':
        if http_path == '/':
            fin = open('index.html')
        elif http_path == '/book':
            fin = open('book.json')
        else:
            pass
        
        content = fin.read()
        fin.close
        response='HTTP/1.1 299 OK\n\n' + content

    else: 
        response = 'HTTP/1.1 405 Method Not Allowed\n\nAllow: GET'
    
    client_socket.sendall(response.encode()) 
    client_socket.close()
    