import socket
import sys
import time

# Client configuration
HOST = '127.0.0.1'  # Server IP address
PORT = 65432        # Port the server is listening on

sales_data = [100.0, 120.0, 90.0, 140.0, 200.0, 150.0, 180.0]
data = ','.join(map(str, sales_data))

# Function to display a progress bar


def print_progress_bar(iteration, total, prefix='', suffix='', length=50, fill='█'):
    percent = ("{:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix))
    sys.stdout.flush()
    if iteration == total:
        print()


print('Data sent:', data)

# Create a socket and connect to the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(data.encode())

    # Display a progress bar while waiting for results
    print('Waiting for results:', end=' ')
    for i in range(101):
        time.sleep(0.1)
        print_progress_bar(i, 100, prefix='Progress:', suffix='Complete')

    # Receive the results from the server
    results = s.recv(1024).decode()

print('\nResults received from the server:')
print(results)
