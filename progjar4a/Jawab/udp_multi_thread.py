#Referensi https://www.bogotobogo.com/python/python_network_programming_server_client_file_transfer.php

from file_client_cli import remote_get
import time
import datetime
import threading
import socket

#sama seperti kodingan pada folder concurrency, hanya ganti fungsi dan menambahkan daftar gambar
def kirim_semua():
    texec = dict()
    daftar = 'pokijan.jpg'

    catat_awal = datetime.datetime.now()
    for k in range(100):
        print(f"mengirim {k}")
        #bagian ini merupakan bagian yang mengistruksikan eksekusi fungsi kirim gambar secara multithread
        texec[k] = threading.Thread(target=remote_get, args=(daftar,))
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