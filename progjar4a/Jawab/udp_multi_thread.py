#Referensi https://www.bogotobogo.com/python/python_network_programming_server_client_file_transfer.php

from file_client_cli import remote_get
import time
import datetime
import threading
import socket

#target IP kirim
TARGET_IP = "192.168.122.255" #Bcast = Broadcast Address
TARGET_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEPORT, 1)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST, 1)

#fungsi kirim untuk mengirim gambar pada daftar
def kirim(daftar=None):

    #menggunakan if apabila pada list 'daftar' tidak ada gambar tersedia
    #apabila tidak memakai if, akan muncul pesan error 'kirim() takes 0 positional arguments but 1 was given'
    if (daftar is None):
        return False

    #seperti praktikum UDP 1 dan 2
    f = open(daftar,"rb")
    l = f.read(1024)
    while (l):
        if(sock.sendto(l, (TARGET_IP, TARGET_PORT))):
                l = f.read(1024)
    f.close()

#sama seperti kodingan pada folder concurrency, hanya ganti fungsi dan menambahkan daftar gambar
def kirim_semua():
    texec = dict()
    daftar = 'Background.jpg'

    catat_awal = datetime.datetime.now()
    for k in range(100):
        print(f"mengirim {k}")
        #bagian ini merupakan bagian yang mengistruksikan eksekusi fungsi kirim gambar secara multithread
        texec[k] = threading.Thread(target=kirim, args=(daftar,))
        texec[k].start()

    #setelah menyelesaikan tugasnya, dikembalikan ke main thread dengan join
    for k in range(100):
        texec[k].join()

    catat_akhir = datetime.datetime.now()
    selesai = catat_akhir - catat_awal
    print(f"Waktu TOTAL yang dibutuhkan {selesai} detik {catat_awal} s/d {catat_akhir}")

#fungsi kirim_semua akan dijalankan secara multithread
if __name__=='__main__':
    kirim_semua()