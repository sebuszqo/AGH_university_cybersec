import socket
import threading


HOST = '127.0.0.1'

PORT = 9090 

# pobieram nickname użytkownika
nickname = input("Tell me your nickname: ")

# - te same adresy co ma serwer
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # --> tworzę socket internetowy IPv4
# --> SOC_STREAM - uzywam TCP - nie UDP dlatego stream a nie DATAGRAM 

client.connect((HOST,PORT))


# funkcja odpowiadajaca za otrzymywanie wiadomosci od serwera/uzytkownikow
def receive():
    while True:
        try:
            # 1024 bytes
            message = client.recv(1024).decode('utf-8')
            # jeżeli serwer chce poznać nicname to mu go podaje w innym przypadku po prostu wyświetlam wiadomośći otrzymane
            if message == "NICK":
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except KeyboardInterrupt:
            print("\nError, connection closed!")
            client.close()
            break
        except:
            print("\nError, connection closed!")
            client.close()
            break

# funkcja wysylajaca naszse wiadomosci z klienta
def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('utf-8'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()
write_thread = threading.Thread(target=write)
write_thread .start()
