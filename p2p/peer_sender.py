import socket
import json

HOST = "127.0.0.1"
PORT = 7001

message = {
    "task_id": 1,
    "status": "DONE",
    "source": "node-2"
}

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect((HOST, PORT))
    client.send(json.dumps(message).encode())

    response = client.recv(1024).decode()
    print("Peer response:", response)
except OSError as e:
    print(f"Failed to connect to peer at {HOST}:{PORT}: {e}")
finally:
    client.close()
