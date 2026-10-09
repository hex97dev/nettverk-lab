import socket

HOST = "127.0.0.1"
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    print(f"lytter på {HOST}:{PORT}")

    conn, addr = server.accept()
    with conn:
        print("tilkobling fra", addr)
        data = conn.recv(1024)
        print("mottok:", data.decode(errors="replace"))
        conn.sendall(b"hei fra server\n")
