

class Client(object):
    listOfClients = []
    def __init__(self, clientId, name, surname,address):
        self.SetClientID = clientId
        self.SetName = name
        self.SetSurname = surname
        self.SetAddress = address

    
    @property
    def clientID(self):
        return self._clientId

    @clientID.setter
    def SetClientID(self, clientId):
        if not isinstance(clientId, int):
            raise ValueError
        self._clientId = clientId

    @property
    def name(self):
        return self.__name

    @name.setter
    def SetName(self, name):
        if not isinstance(name, str):
            raise ValueError
        self.__name = name

    @property
    def surname(self):
        return self.__surname 

    @surname.setter
    def SetSurname(self, surname):
        if not isinstance(surname, str):
            raise ValueError
        self.__surname = surname

    @property
    def address(self):
        return self.__address

    @address.setter
    def SetAddress(self, address):
        if not isinstance(address, str):
            raise ValueError
        self.__address = address

    def put(self):
        Client.listOfClients.append(self.name)

    def __str__(self) -> str:
        return f'{self.name} {self.surname} {self.address} ID: {self.clientID}'
    
    @staticmethod
    def printClients():
        return Client.listOfClients

client = Client(2,'hubert', 'lazaik', 'agh')
client2 = Client(2,'hubert', 'lazaik', 'agh')
client.put
print(client)



