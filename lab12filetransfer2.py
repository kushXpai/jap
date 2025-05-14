import socket
import threading
import os

HOST = '127.0.0.1'
PORT = 12345
BUFFER_SIZE = 1024

def handle_client(client_socket, address):
    print(f"[+] Connected to {address}")
    try:
        filename = client_socket.recv(BUFFER_SIZE).decode()
        print(f"[{address}] Requested file: {filename}")

        if os.path.isfile(filename):
            client_socket.send("FOUND".encode())
            with open(filename, "rb") as f:
                while True:
                    bytes_read = f.read(BUFFER_SIZE)
                    if not bytes_read:
                        break
                    client_socket.sendall(bytes_read)
            print(f"[{address}] File sent successfully.")
        else:
            client_socket.send("NOTFOUND".encode())
            print(f"[{address}] File not found.")
    except Exception as e:
        print(f"[!] Error with {address}: {e}")
    finally:
        client_socket.close()
        print(f"[-] Connection closed for {address}")

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"[+] Server listening on {HOST}:{PORT}")

    while True:
        client_socket, addr = server.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_thread.start()

start_server()