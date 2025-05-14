import socket
import threading
import sys

class ChatClient:
    def __init__(self, host='localhost', port=9090):
        self.host = host
        self.port = port
        self.socket = None
        self.running = False
    
    def connect(self):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.host, self.port))
            return True
        except Exception as e:
            print(f"Connection error: {e}")
            return False
    
    def receive_messages(self):
        while self.running:
            try:
                message = self.socket.recv(1024).decode()
                if not message:
                    print("Lost connection to server.")
                    self.running = False
                    break
                
                print(message)
            except Exception as e:
                print(f"Error receiving message: {e}")
                self.running = False
                break
    
    def send_message(self, message):
        """Send a message to the server"""
        try:
            self.socket.send(message.encode())
            return True
        except Exception as e:
            print(f"Error sending message: {e}")
            return False
    
    def start(self):
        if not self.connect():
            return
        
        self.running = True
        
        receive_thread = threading.Thread(target=self.receive_messages)
        receive_thread.daemon = True
        receive_thread.start()
        
        try:
            while self.running:
                message = input()
                if message == "/quit":
                    self.send_message(message)
                    self.running = False
                    break
                
                if not self.send_message(message):
                    break
        except KeyboardInterrupt:
            print("Client shutting down...")
        finally:
            if self.socket:
                self.socket.close()

if __name__ == "__main__":
    host = sys.argv[1] if len(sys.argv) > 1 else 'localhost'
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 9090
    
    print(f"Connecting to {host}:{port}...")
    client = ChatClient(host, port)
    client.start()