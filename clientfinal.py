import socket
import threading

def testarip(ip,msg):
   lista = msg.split("[(")
   lista2 = lista[1].split(",")
   ip2 = lista2[0][1:-1]
   if ip == ip2:
      return False
   else:
      return True

# Conectar no servidor
conection_sucesseful = False
ip = ''
try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 18000))
    conection_sucesseful = True
    ip = client.getpeername()[0]
    print("Você está conectado! Yay")
    print("A mensagem de desconexão é ':D' ")  
    print("Escreva a sua mensageem:")    
except:
    print("Não foi possível realizar a conexão")
    conection_sucesseful = False


# Ouvir o servidor
def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if testarip(ip,message):
                print(message)

        except ConnectionAbortedError:
            print('ConexÃ£o Encerrada')
            break
        except:    
            print("Um erro aconteceu!")
            client.close()
            break

# Enviar pro servidor
def write():
    while True:
        message = str(input())
        len_message = len(message)
        client.send(str(len_message).encode('utf-8'))
        client.send(message.encode('utf-8'))

        if message == ':D':
            client.close()
            break


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
