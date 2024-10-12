import socket
import time

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 8080

# Parameters:
# (1) IP Address, (2) TCP
# socket.SOCK_STREAM = TCP
# socket.SOCK_DGRAM = UDP
my_server_potato = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # initialize the socket

# Parameter explanation
# Create a socket-level option 
# allow the socket to close when things are finished
# 1/0 enables or disables the option
my_server_potato.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # improves performance to close socket when done

# my_server_potato.setblocking(False) # enables non-blocking, enabling the queue

# Every website has an IP address, they just change the name to make it more readible
# accessible to any device = 0.0.0.0
# accessible to this computer only = 127.0.0.1
# Webservers listen on port 8080
my_server_potato.bind((SERVER_HOST, SERVER_PORT)) # bind server to IP address

# parameter:
# 5 contents of the queue
# 6th item in the queue will be refused  
my_server_potato.listen(5)

print(f"Listening on port {SERVER_PORT} ...")
# We established a server, socket options, bind ports, and had it listen
# We didnt do client requests to the server nor we sent any data 

### How do we take the front element of the queue?
while True:
    client_socket, client_address = my_server_potato.accept()
    request = client_socket.recv(1024).decode() # comes as bytes, thats why we have to decode it
    # print(request)
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
        response = 'HTTP/1.1 405 Method Not Allowed\n\nAllow: GET' #always expects \n\n
    
    client_socket.sendall(response.encode()) # is a string, encode it into bytes
    client_socket.close()
    
# open `localhost:8080` on a web browser

# WSGI = Webserver Gateway Interface


### HTTP 1.1 response structure
# STATUS LINE (HTTP versoin, Status Code, Opt Text Msg)
# HEADERS
# MESSAGE-BODY 


### Format of an HTTP Request
# POST / HTTP/1.1
# content-length: 33
# accept-encoding: gzip, deflate, br
# Accept: */*
# User-Agent: Thunder Client (https://www.thunderclient.com)
# Content-Type: application/json
# Host: localhost:8080
# Connection: close


# HTTP versions:
# 0.9, 1.0, [1.1], 2.0, 3.0
# HTTP1.1 = Basic TCP server
# HTTP2.0 = Multiplexing
# HTTP3.0 = QUIC protocol (not TCP)