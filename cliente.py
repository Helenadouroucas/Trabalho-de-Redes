import socket
import threading
'''                                  ***IMPORTANTE***                                  '''
def testarip(ip,msg):           #Função para testar se a mensagem que o servidor está te retornando é a mesma...
   lista = msg.split("[(")      #...a sua própria, evitando dobrar sua mensagem no chat...
   lista2 = lista[1].split(",") #Se testar servidores e clientes no mesmo ip, desativar essa função
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
    print("Escreva a sua mensagem:")    
except:
    print("Não foi possível realizar a conexão")
    conection_sucesseful = False

encerraThread = threading.Event()

# Ouvir o servidor
def receive():
    while not encerraThread.is_set():
        try:
            message = client.recv(64).decode('utf-8')
            if testarip(ip,message): #se testar clientes e servidores no mesmo ip, desativar esse if
                print(message)

        except ConnectionAbortedError:
            print('ConexÃ£o Encerrada')
            encerraThread.set()
            
        except:    
            print("Um erro aconteceu!")
            client.close()
            encerraThread.set()
            

# Enviar pro servidor
def write():
    while not encerraThread.is_set():
        message = str(input())
        client.send(message.encode('utf-8'))

        if message == ':D':
            client.close()
            encerraThread.set()
            



receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
