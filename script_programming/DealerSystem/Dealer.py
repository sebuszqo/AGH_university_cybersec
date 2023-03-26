from datetime import date, timedelta
import json
import sys

# python3 Dealer.py data.json

# I'm fully aware that sell and rent methods should be done in DRY way
# I had to do this in that way cuz lecturer require it

# making my 2 own error classes 
class ThereIsNoCar(Exception):
    pass

class ThereIsNoCarToReturn(Exception):
    pass

# main class Car Dealer()
class Dealer():
    numOfTransactions = 0
    sumOfTransactions = 0 
    def __init__(self, dataFile):
        self.loadFile(dataFile)
    
    # method to load cars and clients from textFile
    def loadFile(self, dataFile):
        with open(dataFile, "r+") as file:
            jsonData = json.load(file)
            self.brands = jsonData["cars"]
            self.clients = jsonData["clients"]
        return

    #method to show The End Status of our transactions that were made
    def showTheEndStatus(self):
        print('-'*40)
        print(f'Number of all Dealer transactions: {Dealer.numOfTransactions}')
        print('-'*40)
        print(f'Sum of all Dealer transactions: {Dealer.sumOfTransactions}')
        for i in self.clients:
            sumOfAll = getattr(Dealer,f'{i["name"]}')
            if i["transaction"] == 'sell':
                print('-'*40)
                print(f'Client: {i["name"].capitalize()}, bought {i["brand"]} for {i["sum"]} (sum of all transactions: {sumOfAll})')
            elif i["transaction"] == 'rent':
                print('-'*40)
                print(f'Client: {i["name"].capitalize()}, rented {i["brand"]} for {i["sum"]} (sum of all transactions: {sumOfAll})')
                print(f'\nRent starts: {i["startDate"]}, ends: {i["endDate"]}. Summary: {i["days"]} days.')
        print('-'*40)
        print(f'Dostępne marki w naszym salonie: ')
        for i in self.brands:
            print(f'- {i["brand"].upper()} ({i["number"]} psc.), for {i["priceToSell"]} (sell), for {i["priceToRent"]} (rent.)')
        return  
        
    #method to sell cars 
    def sell(self, data):
        # print(self.brands)
        # print(data)
        flag = False # I think there is no need to use it cuz I break loop after selling the car
        for i in self.brands:
            if i["brand"] == data[1]: # checking if there is this brand in inventory
                if i["number"] > 0: # checking if there is enough cars to make a deal
                    i["number"] -= 1 # -= cars -1 car after sell 
                    flag = True
                    print(f'Udalo się dokonać sprzedazy za kwote {i["priceToSell"]}')
                    self.clients.append({ #appending new client and his/her data to array of clients
                        "name":f'{data[0]}',
                        "brand": f'{data[1]}',
                        "transaction": "sell",
                        "startDate": date.today(), 
                        "endDate": "",
                        "days": 0,
                        "sum": f'{i["priceToSell"]}'
                    })
                    # using class attributes to store sum of every client
                    if hasattr(Dealer,f'{data[0]}'): # checking is attribute exists
                        x = getattr(Dealer,f'{data[0]}') 
                        setattr(Dealer,f'{data[0]}', x + i["priceToSell"])
                    else:
                        setattr(Dealer,f'{data[0]}', i["priceToSell"])
                    # change of informations about whole Dealer stats 
                    Dealer.numOfTransactions += 1
                    Dealer.sumOfTransactions += i["priceToSell"]
                    # print(Dealer.numOfTransactions)
                    # print(Dealer.sumOfTransactions)
                    return True # to break function cuz she did what she had to - way to make it faster
                else:
                    raise ThereIsNoCar # raising error
            if(flag): # using 'flag' method to make is quicker - it is not because of using return
                break
        else:
            raise ThereIsNoCar
    
        # trying some different approaches    
        # print(self.brands)
        # print(i["number"])
        # print(type(data[2]))
        # if self.brands[data[2]][0] > 0 and data[2] in self.brands:
        #     self.names[data[1]] = [data[2], data[0]]
        #     self.names[data[1]].insert(0, self.brands[data[2]][1])
        #     self.brands[data[2]][0] -= 1
        #     print(self.brands)
        #     print(self.names)
        
    def rent(self, data):
        #[<name>, <brand>, days]
        flag = False
        for i in self.brands:
            if i["brand"] == data[1]: # checking if there is this brand in inventory
                if i["number"] > 0: # checking if there is enough cars to make a deal
                    i["number"] -= 1 # -= cars -1 car after sell 
                    flag = True
                    print(f'Udalo się dokonać wypozyczenia {i["brand"].upper()} za kwote {i["priceToRent"]*data[2]} ({i["priceToRent"]} per day)')
                    self.clients.append({ #appending new client to my array of clients with data
                        "name":f'{data[0]}',
                        "brand": f'{data[1]}',
                        "transaction": "rent",
                        "startDate": date.today(), 
                        "endDate": date.today() + timedelta(days=data[2]),
                        "days": data[2],
                        "sum": f'{i["priceToRent"]*data[2]}'
                    })
                    if hasattr(Dealer,f'{data[0]}'): #dealing with attributes as above in selling
                        x = getattr(Dealer,f'{data[0]}')
                        setattr(Dealer,f'{data[0]}', x + i["priceToRent"]*data[2])
                    else:
                        setattr(Dealer,f'{data[0]}', i["priceToRent"]*data[2])
                    # changing some informations about Dealer stats 
                    Dealer.numOfTransactions += 1
                    Dealer.sumOfTransactions += (i["priceToRent"]*data[2])
                    return True # to break function cuz it did what it should
                else:
                    raise ThereIsNoCar # raising errors
            if(flag): # using 'flag' method to make is quicker
                break
        else:
            raise ThereIsNoCar

        # trying some different approaches 
        # if self.brands[data[2]][0] > 0 and data[2] in self.brands:
        #     self.names[data[1]] = [data[2], data[0]]
        #     self.brands[data[2]][0] -= 1
        #     print(self.brands)

    def returnTheCar(self, data):
        # [<name>, <brand>]
        # print(len(self.clients))
        for i in range(len(self.clients)):
            if self.clients[i]["name"] == data[0] and self.clients[i]["transaction"] == "rent" and self.clients[i]["brand"] == data[1]:
                for car in self.brands:
                    if car["brand"] == data[1]:
                        car["number"] += 1
                # deleting the client who returned his car
                del self.clients[i]
                # changing some informations about Dealer stats 
                Dealer.numOfTransactions += 1
                print('Zakonczono proces zwortu')
                break
        else:
            raise ThereIsNoCarToReturn 
            



# function that deal with errors s
# to make code cleaner and easier to read
def errors(error):
    match error:
        case 'FileNotFoundError':
            return 'You gave me wrong filename sorry, try again'
        case 'ThereIsNoCar':
            return 'Sorry, There is no car in inventory, try again. '
        case 'ThereIsNoCarToReturn':
            return 'Sorry you can\'t return this car try again. '
        case 'ValueError':
            return 'You`ve made a mistake try again. '
        case 'IndexError':
            return 'You did something wronge, try again'


if __name__ == "__main__":
    try:
        if len(sys.argv) <= 1: # guarantee that user has to give right fileName
            raise FileNotFoundError
        x = sys.argv[1]
        # FileNotFoundError is raised by a 'system' when it can't find a file
        dealer = Dealer(sys.argv[1])
    except FileNotFoundError:
            print(errors('FileNotFoundError'))
            exit()
    print("Proper usage: <operation> <clientName> <brand> ")       
    while True:
        try:    
            # [operacja, imie, marka]
            data = input().split()
            # data[1].capitalize()
            if (len(data) != 3): # guarantee that user gave us apropriate data
                raise IndexError
            if data[0] == 'sell':
                dealer.sell(data[1:])
            elif data[0] == 'rent':
                data.append(int(input("Tell me how long you want to rent? ")))
                dealer.rent(data[1:])
            elif data[0] == 'return':
                dealer.returnTheCar(data[1:])
            else:
                print('Sorry there is no transaction like yours')
        except ThereIsNoCar:
            print(errors('ThereIsNoCar'))
            continue
        except ThereIsNoCarToReturn:
            print(errors('ThereIsNoCarToReturn'))
            # print('Sorry you can\'t return this car try again. ')
            continue
        except ValueError:
            print(errors('ValueError'))
            # print('You`ve made a mistake try again. ')
            continue
        except IndexError:
            print(errors('IndexError'))
            continue
        except KeyboardInterrupt:
            dealer.showTheEndStatus()
            break
        # dealer.showAll()
        except EOFError:
            dealer.showTheEndStatus()
            break
        
            
   
        
            
        
    


