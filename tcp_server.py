import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 12346))
server.listen(5)

print("TCP Server active on Port 12346 ...")

while True:
    client, addr = server.accept()
    data = client.recv(1024).decode()
    if data:
        print(f"[TCP] Received: {data}")
        client.send("TCP Server says: Hello Abdullah! Connection Success.".encode())
    client.close()