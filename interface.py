import tkinter as tk
import socket
import threading
import time

HEADER = 64
PORT = 18000
FORMAT ='utf-8'
DISCONNECT_MESAGE = ':D'
SERVER = 'localhost'
ADDR = (SERVER, PORT)

class chatTCP:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(ADDR)

        gui_thread = threading.Thread(target=self.interface)
        receive_thread = threading.Thread(target=self.receive)

        self.on = True
        gui_thread.start()
        receive_thread.start()
    


    def interface(self, master=None):
        self.root = tk.Tk()
        posx = self.root.winfo_screenwidth() // 2 - 450
        posy = self.root.winfo_screenheight() // 2 - 350
        self.root.geometry('%dx%d+%d+%d' % (840, 550, posx, posy))
        self.root.title("Chat TCP")
        self.root.focus_force()
        self.root.configure(bg='#DCDCDC')


        self.frame1 = tk.Frame(master)
        self.frame1.configure(bg='#DCDCDC')
        self.frame1.pack()
        self.caixamensagem = tk.Text(self.frame1, height=30, width=99)
        self.caixamensagem.config(state=tk.DISABLED)
        self.caixamensagem.configure(bg='#F8F8FF')
        self.caixamensagem.pack(pady=6)
        self.frame2 = tk.Frame(master)
        self.frame2.configure(bg='#DCDCDC')
        self.frame2.pack()
        self.entry = tk.Entry(self.frame2, width=58, font=('Arial',14))
        self.entry.configure(bg='#F8F8FF')
        self.entry.pack(side="left",pady=5)
        self.botao = tk.Button(self.frame2, text="ENVIAR", width=20, command=self.send)
        self.botao.pack(side="right",padx=2, pady=5)

        self.root.protocol("WM_DELETE_WINDOW", self.fechar)

        self.root.mainloop()

    
    def send(self):
        msg = self.entry.get()
        #self.entry.insert('')
        message = msg.encode(FORMAT)
        msg_len = len(message)
        send_len = str(msg_len).encode(FORMAT)
        send_len += b' ' * (HEADER - len(send_len))
        self.client.send(send_len)
        self.client.send(message)
    
    def receive(self):
        while self.on:
            try:
                self.caixamensagem.insert(tk.END,self.client.recv(2048).decode(FORMAT))
            except ConnectionAbortedError:
                break
            except ConnectionRefusedError:
                break
            except Exception as e:
                print(f"Error when handling client: {e}")
                self.on = False
                self.root.destroy()
                self.client.close()
                break

    def fechar(self):
        self.on = False
        self.root.destroy()
        self.sock.close()
        exit(0)



chattcp = chatTCP()