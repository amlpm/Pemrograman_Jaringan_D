# Tugas Praktikum UDP 2

### Soal 
1. Loadlah file tersebut di simulator. Dalam praktikum ini lakukan broadcast dari sebuah client udp di alpine-1 agar dapat membroadcast pengiriman ke alpine-2 dan alpine-3 sekaligus, tambahkan  host alpine-4 dan alpine-5 yang dapat dikirimi broadcast juga
2. Gunakan file progjar2/udpclient_broadcast.py dan progjar2/udpserver_broadcast.py. Sesuaikan parameter dan variabel program agar sesuai dengan lingkungan jaringan  ,
3. Jalankan dengan urutan, server dan kemudian client
4. Jalankan dengan urutan client, baru kemudian server 
5. Apakah perbedaan yang terjadi ?
6. Buatlah dokumen PDF yang berisikan screenshot dari 
7. modifikasi program yang dilakukan, dan hasil menjalankan dengan urutan berbeda tadi


### Jawab

1. Menambahkan Alpine 4 dan Alpine 5, lalu menyambungkannya ke eth0.

![Topologi](https://user-images.githubusercontent.com/57977401/116732640-b1e0b800-aa1d-11eb-8f6f-1d7b95cc9026.png) 
<br><br><br>

2. Menset Alpine 4 dan Alpine 5 dengan IP Address DHCP dengan langkah sebagai berikut
- Masukkan command ```nano /etc/network/interfaces```
- Uncomment pada bagian ```auto eth0``` dan ```iface eth0 inet dhcp```
- Reload node
- Cek IP Addres dengan ifconfig, atau dengan melakukan ping ke google.com
<br><br><br>

### Ping Google.com untuk Alpine 4 dan Alpine 5
![Alpine4-PingGoogle](https://user-images.githubusercontent.com/57977401/116733521-c6718000-aa1e-11eb-85a8-f2ff151ae019.png) <br>
![Alpine5-PingGoogle](https://user-images.githubusercontent.com/57977401/116733504-c2456280-aa1e-11eb-9560-9ea67dd51b0a.png) <br><br>

### ifconfig untuk Alpine 4 dan Alpine 5
![Alpine4-IPAddress](https://user-images.githubusercontent.com/57977401/116733665-f3be2e00-aa1e-11eb-99f4-613437986d0e.png) <br>
![Alpine5-IPAddress](https://user-images.githubusercontent.com/57977401/116733659-f15bd400-aa1e-11eb-871a-502d8f7e5f7c.png) 
<br><br><br>

3. Clone Repository github pada tiap alpine dengan command ```git clone https://github.com/amlpm/Pemrograman_Jaringan_D```
<br><br><br>

4. Ubah kode program pada udpclient.py pda alpine 1 menjadi seperti di bawah

![Alpine1-Program-udpclient](https://user-images.githubusercontent.com/57977401/116733974-629b8700-aa1f-11eb-8216-f087bd54cd2e.png) <br><br><br>

### Penjelasan
- 192.168.122.255 yang merupakan Broadcast Address yang terdapat pada seluruh alpine (bisa dicek saat melakukan ifconfig, letaknya persis disebelah inet addr dengan tulisan Bcast)
- Broadcast address merupakan jenis IP address yang digunakan untuk mengirim data ke semua host yang masih berada dalam satu network
<br><br><br>

5. Ubah kode program pada udpserver.py pada alpine 2 hingga 5 menjadi seperti di bawah

![Alpine2-Program-udpserver](https://user-images.githubusercontent.com/57977401/116734732-33394a00-aa20-11eb-8b3f-1d4e254865df.png) <br>
![Alpine3-Program-udpserver](https://user-images.githubusercontent.com/57977401/116734754-36ccd100-aa20-11eb-8c98-5950583e929e.png) <br>
![Alpine4-Program-udpserver](https://user-images.githubusercontent.com/57977401/116734742-35030d80-aa20-11eb-8d21-f5aabade368f.png) <br>
![Alpine5-Program-udpserver](https://user-images.githubusercontent.com/57977401/116734759-38969480-aa20-11eb-8f4d-03c7d481a43a.png) <br>

### Penjelasan
- Ubah IP SERVER menjadi IP server masing-masing alpine. Berikut merupakan daftar IP Address Alpine 2 hingga 5
- alpine2: 192.168.122.143
- alpine3: 192.168.122.170
- alpine4: 192.168.122.55
- alpine5: 192.168.122.182
<br><br><br>

6. Jalankan Server dan Client dengan command
- ```python3 udpserver_broadcast.py``` untuk server (Alpine 2-5)
- ```python3 udpclient_broadcast.py``` untuk client (Alpine 1)
<br><br><br>

7. Hasil dari menjalankan Server lalu Client 
### Alpine 1

![Alpine1-Hasil-ServerClient](https://user-images.githubusercontent.com/57977401/116735992-df2f6500-aa21-11eb-96d0-d3e709077d4e.png) <br>

### Alpine 2

![Alpine2-Hasil-ServerClient](https://user-images.githubusercontent.com/57977401/116735993-dfc7fb80-aa21-11eb-9917-92b694ce0e88.png) <br>

### Alpine 3

![Alpine3-Hasil-ServerClient](https://user-images.githubusercontent.com/57977401/116735997-e0609200-aa21-11eb-8621-bb0b0a58b51a.png) <br>

### Alpine 4

![Alpine4-Hasil-ServerClient](https://user-images.githubusercontent.com/57977401/116735981-dc347480-aa21-11eb-9a42-bd11b6a625a9.png) <br>

### Alpine 5

![Alpine5-Hasil-ServerClient](https://user-images.githubusercontent.com/57977401/116735988-de96ce80-aa21-11eb-9998-90f04d1b5b87.png) <br>

### Kesimpulan
- Alpine 2 hingga 5 mendapat broadcast message dengan lengkap dan sama, dalam hal ini angka 1 hingga node diberhentikan, yaitu angka 5.
<br><br><br>

8. Hasil dari menjalankan Client lalu Server    
### Alpine 1

![Alpine1-Hasil-ClientServer](https://user-images.githubusercontent.com/57977401/116736161-16057b00-aa22-11eb-924f-f9c1826e7bd2.png) <br>

### Alpine 2

![Alpine2-Hasil-ClientServer](https://user-images.githubusercontent.com/57977401/116736143-100f9a00-aa22-11eb-8a44-b7a797400028.png) <br>

### Alpine 3

![Alpine3-Hasil-ClientServer](https://user-images.githubusercontent.com/57977401/116736169-1867d500-aa22-11eb-9155-47ff1acf3543.png) <br>

### Alpine 4

![Alpine4-Hasil-ClientServer](https://user-images.githubusercontent.com/57977401/116736175-1b62c580-aa22-11eb-8b4c-134b32827fae.png) <br>

### Alpine 5

![Alpine5-Hasil-ClientServer](https://user-images.githubusercontent.com/57977401/116736183-1f8ee300-aa22-11eb-9161-0a35792b2abe.png) <br>

### Kesimpulan
- Alpine 2 hingga 5 mendapat broadcast message tidak lengkap (dengan awalan broadcast message yang berbeda namun berakhir dengan angka yang sama) dengan daftar sebagai berikut:
- Alpine 2 dimulai dari angka 3-12
- Alpine 3 dimulai dari angka 4-12
- Alpine 4 dimulai dari angka 6-12
- Alpine 5 dimulai dari angka 8-12
<br><br><br>

8. Perbedaan hasil nomor 6 (Menjalankan Server lalu Client) dan hasil nomor 7 (Menjalankan Client lalu Server)
- Menjalankan server lalu client akan diperoleh hasil broadcast yang lengkap
- Menjalankan client lalu server akan diperoleh hasil broadcast yang berbeda, tergantung kapan server dijalankan baru pesan broadcastnya masuk