import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:9000/")

response = proxy.write_file("sample.txt", "Hello from client via RPC!")
print(response)

file_content = proxy.read_file("sample.txt")
print("File content:\n", file_content)

files = proxy.list_files(".")
print("Files in directory:", files)