import socket
port =1234
address = "127.0.0.1"
BUF_SIZE = 1024

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((address,port))

client.send(bytes("Hello...","utf-8"))

data = client.recv(BUF_SIZE)
client.close()

print(data.decode("utf-8"))
