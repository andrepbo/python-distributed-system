import socket

# Client configuration
HOST = '127.0.0.1'  # Server IP address
PORT = 65432        # Port the server is listening on

# Sales data for a week (you can modify this data)
sales_data = [100.0, 120.0, 90.0, 140.0, 200.0, 150.0, 180.0]

# Convert the sales data to a string
data = ','.join(map(str, sales_data))

# Initialize the socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connect to the server
    s.connect((HOST, PORT))
    # Send the data (sales data) to the server
    s.sendall(data.encode())
    # Receive the server's mining results
    mining_results = s.recv(1024).decode()

print('Mining results from the server:')
print(mining_results)
