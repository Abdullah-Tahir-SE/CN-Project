import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('127.0.0.1', 54321))

print("UDP Server active on Port 54321 ...")

while True:
    data, addr = server.recvfrom(1024)
    print(f"[UDP] Received: {data.decode()} from {addr}")
    server.sendto("UDP Server says: Packet Received!".encode(), addr)