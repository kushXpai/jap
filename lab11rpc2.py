from xmlrpc.server import SimpleXMLRPCServer
import os

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {e}"

def write_file(filename, content):
    try:
        with open(filename, 'w') as f:
            f.write(content)
        return "Write successful"
    except Exception as e:
        return f"Error writing to file: {e}"

def list_files(directory):
    try:
        return os.listdir(directory)
    except Exception as e:
        return f"Error listing directory: {e}"

server = SimpleXMLRPCServer(("localhost", 9000))
print("RPC Server is running on port 9000...")

server.register_function(read_file, "read_file")
server.register_function(write_file, "write_file")
server.register_function(list_files, "list_files")

server.serve_forever()