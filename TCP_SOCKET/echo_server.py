import socket
port = 1234
address = "127.0.0.1"
BUF_SIZE = 1024 # Buffer size for receiving data

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((address, port))
server.listen(5)
print(f"Server is running on port {port}")

while True:
    con, address = server.accept()
    data = con.recv(BUF_SIZE)

    print("data received:",data.decode("utf-8"))
    con.send(bytes(data.decode("utf-8"),"utf-8"))
    #con.send(data)