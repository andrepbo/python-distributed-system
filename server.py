import socket
import numpy as np

# Server configuration
HOST = '127.0.0.1'  # Server IP address
PORT = 65432        # Port the server will listen on

# Initialize the socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Bind the socket to the address and port
    s.bind((HOST, PORT))
    # Listen for connections
    s.listen()

    print('Waiting for connections...')
    conn, addr = s.accept()  # Accept the connection
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)  # Receive data from the client
            if not data:
                break
            # Convert the received data to a list of numbers
            sales_data = list(map(float, data.decode().split(',')))

            # Perform data mining to find the maximum sales and the day
            max_sales = max(sales_data)
            # Assume days are numbered from 1
            max_sales_day = sales_data.index(max_sales) + 1

            # Prepare the mining results to send back to the client
            mining_results = f"Maximum Sales: {max_sales}, Day: {max_sales_day}"

            # Send the mining results back to the client
            conn.sendall(mining_results.encode())
