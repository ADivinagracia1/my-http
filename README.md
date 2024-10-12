# my-http

![webserver](pics/webserver.png)

A web server is a system that stores, processes, and delivers webpages to users (clients). This communication is done in HTTP, Hyper Text Transcer Protocol. It is used when data is sent or recieved between the sockets

a socket is an endpoint of a network comms system. It facilitates the sending and recieving of data between a client and server

IP are rules of routing or sending packets of data across networks between devices. Private IP addresses are used to send packets between devices in the same network. Public IP addresses are used to send packets between networks

TCP Sockets! A scoket that uses the Transmission Control Protocol, a STN, SYN-ACK, ACK type protocol (handshake)

DNS converts an IP address (i.e. http://142.250.189.206/) to a string that we understand as website links (i.e. https://www.google.com/)

A port is a virtual point where network connectoins start and end. Each port is associated with a certain proccess/service.
HTTP = Port 80
HTTPS = Port 443


## Easiest way
Level 0 HTTP server
```
python3 -m http.server
```
