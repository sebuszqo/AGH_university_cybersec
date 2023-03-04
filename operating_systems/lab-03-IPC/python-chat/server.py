import socket
import threading 

HOST = '127.0.0.1' #localhost --> uruchamiam na moim komputerze więc to będzie adres serwera, 
# --> jeśli chciałbym w sieci WAN to tutaj leci mój adres prywatny jako urządzenia 

PORT = 9090 #--> przypisuje wolny port (80 - http 20 etc. - nie wybieram portów zarezerwowanych)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # --> tworzę socket internetowy IPv4
# --> SOC_STREAM - uzywam TCP - nie UDP dlatego stream a nie DATAGRAM 

server.bind((HOST,PORT)) # --> binduje, przypisuje adres i port do servera 

server.listen() # --> każemy nasłuchiwać naszemu serwerowi na nowe przychodzące połączenia

clients = [] # --> lista zawierająca clients

nicknames = [] # --> lista zawierająca nicknames of clients

# funkcja broadcastująca - wysyłająca wiadomość do wszystkich klientów w naszej liście
# tu moze byc blad
def broadcast(message):
    list(map(lambda x: x.send(message), clients))

# operowanie na klientach każdy na swoim wątku
def handle(client):
    while True:
        # probujemy otrzymać wiadomość od klienta i wysłać ją do wszystkich 
        try:
            message = client.recv(1024)
            broadcast(message)
        # jakikolwiek błąd - albo zakończenie połączenia - powoduje wyjątek 
        # usuwamy klienta z list dajemy o tym znać wszystkim użytkownikom i zamykamy połączenie
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            broadcast(f"Client: {nicknames[index]} left the chat!".encode('utf-8'))
            nicknames.remove(nicknames[index])
            break

def receive():
    while True:
        # akceptujemy połączenia
        # otrzymujemy client i address klienta
        client, address = server.accept()
        print(f"New connection from {str(address)}")
        # informuje klienta aby wysłał nam swój nickname
        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        print(f"Client Nickname is: {nickname}")
        broadcast(f"{nickname} joined the chat".encode('utf-8'))
        client.send("\nYou are connected to the server!".encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

if __name__ == "__main__":
    print("Server is listening...")
    receive()