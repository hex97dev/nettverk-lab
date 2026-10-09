import socket

HOST = "127.0.0.1"
PORT = 8080

with socket.create_connection((HOST, PORT)) as sock:
    sock.sendall(b"hei\n")
    print(sock.recv(1024).decode())
