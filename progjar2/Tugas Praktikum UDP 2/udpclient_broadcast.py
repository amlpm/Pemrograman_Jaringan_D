import socket
import time

TARGET_IP = '192.168.122.255' #Bcast = Broadcast Address
TARGET_PORT = 5005
# A broadcast address is a special type of networking address that is reserved
# for sending messages to all nodes on a given network or network segment.


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEPORT, 1)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST, 1)


angka = 0
while True:
    angka = angka+1
    msg = " BROADCAST ini angka {} " . format(angka)
    print(msg)
    sock.sendto(msg.encode(), ("192.168.122.255", TARGET_PORT))
#    time.sleep(1)