import socket

HOST = '127.0.0.1'
PORT = 12345
BUFFER_SIZE = 1024

filename = input("Enter filename to request from server: ")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    client_socket.send(filename.encode())

    status = client_socket.recv(BUFFER_SIZE).decode()
    if status == "FOUND":
        with open("received_" + filename, "wb") as f:
            while True:
                data = client_socket.recv(BUFFER_SIZE)
                if not data:
                    break
                f.write(data)
        print("✅ File received successfully.")
    else:
        print("❌ File not found on server.")