import socket
import tkinter as tk
from tkinter import font
from tkinter import ttk
from tkinter import filedialog
import time
import threading
import os

class GUI:
    def __init__(self, ip_address, port):
        self.users = {}
        self.users['Amel']={'password':'1'}
        self.users['Evelyn']={'password':'2'}
        self.users['Syarif']={'password':'3'}
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((ip_address, port))

        self.Window = tk.Tk()
        self.Window.withdraw()

        self.login = tk.Toplevel()
        self.login.title("Login")
        self.login.resizable(width=False, height=False)
        self.login.configure(width=400, height=430, bg="#bbf1fa")

        self.keterangan = tk.Label(self.login, text="Made by Evelyn, Amelia, Syarif", justify=tk.CENTER,font="Poppins 8 bold", bg="#bbf1fa")
        self.keterangan.place(relheight=0.15, relx=0.30, rely=0.02)

        self.loginText = tk.Label(self.login, text="MOHON LOGIN TERLEBIH DAHULU", justify=tk.CENTER, font="Poppins 14 bold",bg="#bbf1fa")
        self.loginText.place(relheight=0.15, relx=0.1, rely=0.12)

        self.userLabel = tk.Label(self.login, text="Username: ", font="Poppins 11",bg="#bbf1fa")
        self.userLabel.place(relheight=0.2, relx=0.15, rely=0.25)
        self.userInput = tk.Entry(self.login, font="Poppins 12")
        self.userInput.place(relwidth=0.4 ,relheight=0.1, relx=0.40, rely=0.30)
        self.userInput.focus()

        self.passwordLabel = tk.Label(self.login, text="Password: ", font="Poppins 11",bg="#bbf1fa")
        self.passwordLabel.place(relheight=0.2, relx=0.15, rely=0.40)
        self.passwordInput = tk.Entry(self.login, font="Poppins 12", show="*")
        self.passwordInput.place(relwidth=0.4, relheight=0.1, relx=0.40, rely=0.45)

        self.roomLabel = tk.Label(self.login, text="Id Room: ", font="Poppins 12",bg="#bbf1fa")
        self.roomLabel.place(relheight=0.2, relx=0.15, rely=0.55)
        self.roomInput = tk.Entry(self.login, font="Poppins 11")
        self.roomInput.place(relwidth=0.4 ,relheight=0.1, relx=0.40, rely=0.60)
        
        self.masuk = tk.Button(self.login, text="MASUK", font="Poppins 12 bold",bg="#51c2d5",fg="#ffffff", command = lambda: self.masuk_fungsi(self.userInput.get(), self.roomInput.get(),self.passwordInput.get()))
        self.masuk.place(relx=0.40, rely=0.77)

        self.Window.mainloop()


    def masuk_fungsi(self, username, room_id=0, pw=0):
        self.name = username
        self.room = room_id
        if (username in self.users and self.users[username]['password']== pw):
            self.sock.send(str.encode(username))
            time.sleep(0.1)
            self.sock.send(str.encode(room_id))
            self.login.destroy()
            self.chat_GUI()
            terima = threading.Thread(target=self.terima)
            terima.start()
        else:
            self.warn=tk.Label(self.login,bg="#bbf1fa", text="Salah username/password!",justify=tk.CENTER,font="Poppins 12 bold", fg="#f55c47")
            self.warn.place(relx=0.18, rely=0.90)

    def chat_GUI(self):
        self.Window.deiconify()
        self.Window.title("ROOM "+self.room)
        self.Window.resizable(width=False, height=False)
        self.Window.configure(width=470, height=550, bg="#17202A")
        self.header = tk.Label(self.Window,bg = "#51c2d5",fg = "#ffffff",text = self.name,font = "Poppins 14 bold",pady = 5)
        self.header.place(relwidth = 1)

        self.text = tk.Text(self.Window,width=20,height=2,bg="#c0fefc",fg="#000000",font="Poppins 11",padx=5,pady=5)
        self.text.place(relheight=0.745, relwidth=1, rely=0.08)
		
        self.labelBottom = tk.Label(self.Window, bg="#51c2d5", height=80)
        self.labelBottom.place(relwidth = 1,rely = 0.8)
		
        self.msgInput = tk.Entry(self.labelBottom,bg = "#c0fefc",fg = "#000000",font = "Poppins 11")
        self.msgInput.place(relwidth = 0.74,relheight = 0.03,rely = 0.008,relx = 0.011)
        self.msgInput.focus()

        self.msgBtn = tk.Button(self.labelBottom,text = "Kirim",font = "Poppins 10 bold",width = 20,bg = "#c0fefc",command = lambda : self.tombol_kirim(self.msgInput.get()))
        self.msgBtn.place(relx = 0.77,rely = 0.008,relheight = 0.03,relwidth = 0.22)

        self.labelFile = tk.Label(self.Window, bg="#51c2d5", height=70)
        self.labelFile.place(relwidth = 1, rely = 0.9)

        self.browse = tk.Button(self.labelFile, text="Browse", font="Poppins 10 bold", width=13, bg="#c0fefc",command=self.browse_file)
        self.browse.place(relx=0.011, rely=0.008, relheight=0.03, relwidth=0.15)

        self.fileLocation = tk.Label(self.labelFile,text = "Pilih file",bg = "#c0fefc",fg = "#000000", font = "Poppins 11")
        self.fileLocation.place(relwidth=0.57, relheight=0.03, rely=0.008, relx=0.175)

        self.kirim_fileBtn = tk.Button(self.labelFile,text = "Kirim", font = "Poppins 10 bold",width = 13, bg = "#c0fefc",command = self.kirim_file)
        self.kirim_fileBtn.place(relx=0.77, rely=0.008, relheight=0.03, relwidth=0.22)

        self.text.config(cursor = "arrow")
        scrollbar = tk.Scrollbar(self.text)
        scrollbar.place(relheight = 1,relx = 0.974)
        scrollbar.config(command = self.text.yview)
        self.text.config(state = tk.DISABLED)

    def browse_file(self):
        self.filename = filedialog.askopenfilename(initialdir="/",title="Pilih file",filetypes = (("Text files","*.txt*"),("all files","*.*")))
        self.fileLocation.configure(text="File Dibuka: "+ self.filename)

    def kirim_file(self):
        self.sock.send("FILE".encode())
        time.sleep(0.1)
        self.sock.send(str("client_" + os.path.basename(self.filename)).encode())
        time.sleep(0.1)
        self.sock.send(str(os.path.getsize(self.filename)).encode())
        time.sleep(0.1)

        file = open(self.filename, "rb")
        data = file.read(1024)
        while data:
            self.sock.send(data)
            data = file.read(1024)
        self.text.config(state=tk.DISABLED)
        self.text.config(state = tk.NORMAL)
        self.text.insert(tk.END, "You: "+ str(os.path.basename(self.filename)) + " Dikirim\n\n")
        self.text.config(state = tk.DISABLED)
        self.text.see(tk.END)


    def tombol_kirim(self, msg):
        self.text.config(state = tk.DISABLED)
        self.msg=msg 
        self.msgInput.delete(0, tk.END)
        snd= threading.Thread(target = self.kirim_message) 
        snd.start() 

    def terima(self):
        while True:
            try:
                message = self.sock.recv(1024).decode()

                if str(message) == "FILE":
                    nama_file = self.sock.recv(1024).decode()
                    len_file = self.sock.recv(1024).decode()
                    send_user = self.sock.recv(1024).decode()

                    if os.path.exists(nama_file):
                        os.remove(nama_file)

                    total = 0
                    with open(nama_file, 'wb') as file:
                        while str(total) != len_file:
                            data = self.sock.recv(1024)
                            total = total + len(data)
                            file.write(data)

                    self.text.config(state=tk.DISABLED)
                    self.text.config(state = tk.NORMAL)
                    self.text.insert(tk.END, str(send_user) + ": " + nama_file + " Diterima\n\n")
                    self.text.config(state = tk.DISABLED)
                    self.text.see(tk.END)

                else:
                    self.text.config(state=tk.DISABLED)
                    self.text.config(state = tk.NORMAL)
                    self.text.insert(tk.END,message+"\n\n")

                    self.text.config(state = tk.DISABLED)
                    self.text.see(tk.END)

            except: 
                print("An error occured!") 
                self.sock.close()
                break

    def kirim_message(self):
        self.text.config(state=tk.DISABLED)
        while True:  
            self.sock.send(self.msg.encode())
            self.text.config(state = tk.NORMAL)
            self.text.insert(tk.END, "You: " + self.msg + "\n\n")
            self.text.config(state = tk.DISABLED)
            self.text.see(tk.END)
            break

if __name__ == "__main__":
    ip_address = "127.0.0.1"
    port = 5005
    g = GUI(ip_address, port)
