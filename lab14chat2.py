import socket
import threading
import time
import json
import os
from datetime import datetime

class ChatServer:
    def __init__(self, host='0.0.0.0', port=9090):
        self.host = host
        self.port = port
        self.server_socket = None
        self.clients = {}
        self.lock = threading.Lock()
        self.user_credentials = {}
        self.load_users()

    def load_users(self):
        try:
            if os.path.exists('users.json'):
                with open('users.json', 'r') as f:
                    self.user_credentials = json.load(f)
                print(f"Loaded {len(self.user_credentials)} users from file")
        except Exception as e:
            print(f"Error loading users: {e}")
            self.user_credentials = {}

    def save_users(self):
        with open('users.json', 'w') as f:
            json.dump(self.user_credentials, f)
        print(f"Saved {len(self.user_credentials)} users to file")

    def authenticate(self, conn, addr):
        conn.send("Welcome to the chat server!\n".encode())
        while True:
            conn.send("1. Login\n2. Register\nChoice: ".encode())
            try:
                choice = conn.recv(1024).decode().strip()
                if not choice:
                    return False, None
                
                if choice == "1":
                    conn.send("Username: ".encode())
                    username = conn.recv(1024).decode().strip()
                    conn.send("Password: ".encode())
                    password = conn.recv(1024).decode().strip()
                    
                    if username in self.user_credentials and self.user_credentials[username] == password:
                        return True, username
                    else:
                        conn.send("Invalid credentials. Try again.\n".encode())
                
                elif choice == "2":
                    conn.send("New username: ".encode())
                    username = conn.recv(1024).decode().strip()
                    if username in self.user_credentials:
                        conn.send("Username already exists. Try another.\n".encode())
                        continue
                    conn.send("New password: ".encode())
                    password = conn.recv(1024).decode().strip()
                    
                    with self.lock:
                        self.user_credentials[username] = password
                        self.save_users()
                    
                    conn.send(f"Registration successful! Welcome {username}.\n".encode())
                    return True, username
            except Exception as e:
                print(f"Authentication error with {addr}: {e}")
                return False, None

    def broadcast(self, message, sender=None):
        timestamp = datetime.now().strftime("%H:%M:%S")
        formatted_message = f"[{timestamp}] {message}"
        
        disconnected_clients = []
        
        with self.lock:
            for username, (client_conn, _) in self.clients.items():
                if sender and username == sender:
                    continue
                
                try:
                    client_conn.send(formatted_message.encode())
                except:
                    disconnected_clients.append(username)
            
            for username in disconnected_clients:
                print(f"Client {username} disconnected during broadcast")
                client_conn, _ = self.clients.pop(username, (None, None))
                if client_conn:
                    client_conn.close()

    def handle_client(self, conn, addr):
        """Handle individual client connections"""
        authenticated, username = self.authenticate(conn, addr)
        
        if not authenticated or not username:
            conn.close()
            return
        
        with self.lock:
            if username in self.clients:
                conn.send("This account is already logged in elsewhere.\n".encode())
                conn.close()
                return
            
            self.clients[username] = (conn, addr)
        
        self.broadcast(f"*** {username} has joined the chat ***")
        print(f"New connection from {addr}, username: {username}")
        
        active_users = ", ".join([user for user in self.clients.keys() if user != username])
        conn.send(f"Currently active users: {active_users if active_users else 'none'}\n".encode())
        conn.send("Type '/help' for commands, '/quit' to exit\n".encode())
        
        try:
            while True:
                data = conn.recv(1024).decode()
                if not data:
                    break
                
                message = data.strip()
                if message == "/quit":
                    break
                elif message == "/help":
                    help_text = (
                        "\n--- Available Commands ---\n"
                        "/help - Show this help message\n"
                        "/users - List all active users\n"
                        "/msg <username> <message> - Send private message\n"
                        "/quit - Exit the chat\n"
                    )
                    conn.send(help_text.encode())
                elif message == "/users":
                    with self.lock:
                        user_list = ", ".join(self.clients.keys())
                    conn.send(f"Active users: {user_list}\n".encode())
                elif message.startswith("/msg "):
                    try:
                        _, target, *msg_parts = message.split(" ")
                        if not msg_parts:
                            conn.send("Message cannot be empty\n".encode())
                            continue
                        
                        pm_content = " ".join(msg_parts)
                        with self.lock:
                            if target in self.clients:
                                target_conn, _ = self.clients[target]
                                timestamp = datetime.now().strftime("%H:%M:%S")
                                target_conn.send(f"[{timestamp}] [PM from {username}] {pm_content}\n".encode())
                                conn.send(f"[{timestamp}] [PM to {target}] {pm_content}\n".encode())
                            else:
                                conn.send(f"User {target} is not online\n".encode())
                    except ValueError:
                        conn.send("Usage: /msg <username> <message>\n".encode())
                else:
                    self.broadcast(f"{username}: {message}", username)
                    timestamp = datetime.now().strftime("%H:%M:%S")
                    conn.send(f"[{timestamp}] You: {message}\n".encode())
        
        except Exception as e:
            print(f"Error handling client {username}: {e}")
        finally:
            with self.lock:
                if username in self.clients:
                    self.clients.pop(username)
            
            conn.close()
            self.broadcast(f"*** {username} has left the chat ***")
            print(f"Connection closed for {username}")

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        try:
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(10)
            print(f"Server started on {self.host}:{self.port}")
            
            while True:
                conn, addr = self.server_socket.accept()
                client_thread = threading.Thread(target=self.handle_client, args=(conn, addr))
                client_thread.daemon = True
                client_thread.start()
        
        except KeyboardInterrupt:
            print("Server shutting down...")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            if self.server_socket:
                self.server_socket.close()

if __name__ == "__main__":
    server = ChatServer()
    server.start()