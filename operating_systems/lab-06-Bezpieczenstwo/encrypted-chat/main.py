import socket 
import threading
import rsa

# function to send messages        
def message_send(client):
    while True:
        message = input("")
        client.send(rsa.encrypt(message.encode(),public_partner))
        print(f"You've send {message}")

# function to receive messages        
def message_receive(client):
    while True:
        print(f"You've received: {rsa.decrypt(client.recv(1024), private_key).decode()}")
    
public_key, private_key = rsa.newkeys(1024)
public_partner = None


choise = input("What you want to do here: *1* host or *2* connect: ")

# choosing way to solve hosting or connecting
if choise == "1":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # binding sockets
    server.bind(("127.0.0.1", 9093))
    # listening to the socket
    server.listen()
    # accepting client
    client, _ = server.accept()
    client.send(public_key.save_pkcs1("PEM"))
    # taking public key from received message
    public_partner = rsa.PublicKey.load_pkcs1(client.recv(1024))
elif choise == "2":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connecting to socket 
    client.connect(("127.0.0.1", 9093))
    # taking public key from received message
    public_partner = rsa.PublicKey.load_pkcs1(client.recv(1024))
    client.send(public_key.save_pkcs1("PEM"))
else:
    exit()

# start threads
threading.Thread(target=message_send, args=(client,)).start()
threading.Thread(target=message_receive, args=(client,)).start()