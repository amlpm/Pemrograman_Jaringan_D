import socket 
from _thread import *
import sys
from collections import defaultdict as df
import time


class Server:
    def __init__(self):
        self.rooms = df(list)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def buat_koneksi(self, ip_address, port):
        self.ip_address = ip_address
        self.port = port
        self.sock.bind((self.ip_address, int(self.port)))
        self.sock.listen(100)

        while True:
            connection, address = self.sock.accept()
            print(str(address[0]) + ":" + str(address[1]) + " Connected")
            start_new_thread(self.thread_client, (connection,))

        self.sock.close()

    
    def thread_client(self, connection):
        user_id = connection.recv(1024).decode().replace("User ", "")
        room_id = connection.recv(1024).decode().replace("Join ", "")

        if room_id not in self.rooms:
            connection.send(f"Hai, {user_id}! Selamat Datang di Grup Baru - Code oleh Evelyn,Amelia,Syarif".encode())
        else:
            connection.send(f"Hai, {user_id}! Selamat Datang di Grup {room_id} - Code oleh Evelyn,Amelia,Syarif".encode())

        self.rooms[room_id].append(connection)

        while True:
            try:
                message = connection.recv(1024)
                print(str(message.decode()))
                if message:
                    if str(message.decode()) == "FILE":
                        self.file_broadcast(connection, room_id, user_id)
                    else:
                        message_to_send = str(user_id) + ": " + message.decode()
                        self.broadcast(message_to_send, connection, room_id)
                else:
                    self.remove(connection, room_id)
            except Exception as e:
                print(repr(e))
                print("Client disconnected")
                break

    def file_broadcast(self, connection, room_id, user_id):
        nama_file = connection.recv(1024).decode()
        len_file = connection.recv(1024).decode()
        for client in self.rooms[room_id]:
            if client != connection:
                try: 
                    client.send("FILE".encode())
                    time.sleep(0.1)
                    client.send(nama_file.encode())
                    time.sleep(0.1)
                    client.send(len_file.encode())
                    time.sleep(0.1)
                    client.send(user_id.encode())
                except:
                    client.close()
                    self.remove(client, room_id)
        total = 0
        print(nama_file, len_file)
        while str(total) != len_file:
            data = connection.recv(1024)
            total = total + len(data)
            for client in self.rooms[room_id]:
                if client != connection:
                    try: 
                        client.send(data)
                        # time.sleep(0.1)
                    except:
                        client.close()
                        self.remove(client, room_id)
        print("Terkirim")

    def broadcast(self, message_to_send, connection, room_id):
        for client in self.rooms[room_id]:
            if client != connection:
                try:
                    client.send(message_to_send.encode())
                except:
                    client.close()
                    self.remove(client, room_id)

    def remove(self, connection, room_id):
        if connection in self.rooms[room_id]:
            self.rooms[room_id].remove(connection)

if __name__ == "__main__":
    ip_address = "127.0.0.1"
    port = 5005
    s = Server()
    s.buat_koneksi(ip_address, port)
