import sys
import socket

ip = ['192.168.122.25', '192.168.122.36']

for x in range(2):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = (ip[x], 10000)
    print(f"Connecting to {server_address}")
    sock.connect(server_address)
    print(f"Connected to {server_address}")

try:

    # Send data
    print
    "Enter file name of the image with extension (example: filename.jpg,filename.png) "
    fname = raw_input()
    rname = 'kirimBalik' + str(x) + '.jpg'
    client_socket.send(fname)
    fp = open(fname, 'w')
    while True:
        string = fp.read();
        sock.sendall(string)
        if not string:
            break
        print (f"Sending Image {fname}")
    # Look for the response
    amount_received = 0
    amount_expected = len(string)
    fp = sock,open(fname, 'w')
    while True:
        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            print(f"{data}")
            if not data:
                break
            file.write(data);
finally:
    print(f"Recieving Image {rname}")
    sock.close()
