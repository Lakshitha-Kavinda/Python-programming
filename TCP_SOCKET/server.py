import socket
port = 1234
address = "127.0.0.1"

#create a socket object named server
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #AF_NET for IPv4, SOCK_STREAM for TCP type(socket is TCP type
server.bind((address,port)) #bind the socket to the address and port and let the server listen for incoming connections

server.listen(5) #listen for incoming connections from clients, 5 is the maximum number of queued connections
print("Server is listening")

while True:
    con,address = server.accept() #accept a connection from a client, con is the connection object and address is the address of the client
    print("Connection address is:",address)
    con.send(bytes("Hello client","utf-8")) #send a message to the client