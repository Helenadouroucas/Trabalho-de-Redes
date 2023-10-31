import socket 
import time

HEADER = 64
PORT = 18000
FORMAT ='utf-8'
DISCONNECT_MESAGE = ':D'
SERVER = 'localhost'
ADDR = (SERVER, PORT)

conection_sucesseful = False
try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    conection_sucesseful = True
except:
    print("Não foi possível realizar a conexão")
    conection_sucesseful = False

def send(msg):
    message = msg.encode(FORMAT)
    msg_len = len(message)
    send_len = str(msg_len).encode(FORMAT)
    send_len += b' ' * (HEADER - len(send_len))
    client.send(send_len)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

if(conection_sucesseful == True):
    print("Você está conectado! O Miceli está orgulhoso (provavelmente)")
    print("A mensagem de desconexão é ':D' ")    
    entry = ""    
    while entry != ":D":
        entry = input('Sua mensagem: ')
        try:
            send(entry)
        except:
            break

    print("A conexão com o servidor foi perdida")

'''if __name__=='__main__':
   quantidade = int(input('Quantas msgs vc vai mandar? '))
   for i in range(quantidade):
       entry = input('Sua mensagem: ')
       send(entry)'''
    
        