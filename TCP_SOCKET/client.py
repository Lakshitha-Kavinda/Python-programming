import socket
address = "127.0.0.1"
port = 1234
BUF_SIZE = 1024

#create a socket object named client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((address,port))

data = client.recv(BUF_SIZE) #receive data from the server
client.close()
print(data.decode("utf-8"))

#python library will automatically assign a port to the client