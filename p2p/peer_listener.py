import socket
import json

HOST = "127.0.0.1"
PORT = 7001

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"Peer listener started on {HOST}:{PORT}")

conn, addr = server.accept()
data = conn.recv(4096).decode()

try:
    message = json.loads(data)
    print("Received from peer:", message)
except json.JSONDecodeError as e:
    print(f"Failed to parse message from peer: {e}")

conn.send(b"SYNC_OK")
conn.close()
server.close()
