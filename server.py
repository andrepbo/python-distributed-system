import socket

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
    conn, addr = s.accept()
    print('Connected by', addr)
    with conn:
        total_sales = 0
        max_sales = 0
        max_sales_day = 0
        sales_data = []
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print('Received data:', data)
            numbers = [float(x) for x in data.decode().split(',') if x]
            print('Parsed numbers:', numbers)
            if numbers:
                total_sales = sum(numbers)
                max_sales = max(numbers)
                max_sales_day = numbers.index(max_sales) + 1

        result = f"Total Sales: {total_sales}, Max Sales: {max_sales} on Day {max_sales_day}"
        print('Sending result:', result)
        conn.sendall(result.encode())
