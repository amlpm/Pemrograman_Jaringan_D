import time
import datetime
import socket
import logging
from multiprocessing import Process, Pool

TARGET_IP = "192.168.122.255"
TARGET_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEPORT, 1)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST, 1)

#fungsi broadcast untuk membroadcast 2 gambar yang di list 'daftar'
def broadcast(daftar=None):

    #menggunakan if apabila pada list 'daftar' tidak ada gambar tersedia
    #apabila tidak memakai if, akan muncul pesan error 'broadcast() takes 0 positional arguments but 1 was given'
    if (daftar is None):
        return False

    #seperti praktikum UDP 1 dan 2
    fp = open(daftar,"rb")
    sendimg = fp.read(1024)
    while (sendimg):
        if(sock.sendto(sendimg, (TARGET_IP, TARGET_PORT))):
                sendimg = fp.read(1024)
    fp.close()

#sama seperti kodingan pada folder concurrency, hanya ganti fungsi dan menambahkan daftar gambar
def kirim_semua():
    texec = dict()
    daftar = ['Background.jpg', 'ITS.png']
    status_task = dict()

    # 2 task yang dapat dikerjakan secara simultan, dapat diset sesuai jumlah core
    task_pool = Pool(processes=20)
    catat_awal = datetime.datetime.now()
    for k in range(len(daftar)):
        print(f"mengirim {daftar[k]}")
        #bagian ini merupakan bagian yang mengistruksikan eksekusi fungsi download gambar secara multiprocess
        texec[k] = task_pool.apply_async(func=broadcast, args=(daftar[k],))

    #setelah menyelesaikan tugasnya, dikembalikan ke main process dengan mengambil hasilnya dengan get
    for k in range(len(daftar)):
        status_task[k]=texec[k].get(timeout=10)

    catat_akhir = datetime.datetime.now()
    selesai = catat_akhir - catat_awal
    print(f"Waktu TOTAL yang dibutuhkan {selesai} detik {catat_awal} s/d {catat_akhir}")
    print("status TASK")
    print(status_task)

if __name__=='__main__':
    kirim_semua()