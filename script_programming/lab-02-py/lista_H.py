# >>> import lista_H
# Ładowanie modułu "lista_H"
# Załadowano moduł "lista_H"

# >>> lista_H.wypisz()
# Wywołano funkcję "wypisz()" modułu "lista_H"

#  python3 lista_H.py 2 2 3 5 10 2 3        

from itertools import count
import sys
from collections import Counter, OrderedDict

global lista
lista = []

def save(arg):
    return lista.append(int(arg))

def show():
    countedList = Counter(tuple(lista))    
    toPrint  = ""
    for number, occurs in zip(countedList.keys(), countedList.values()):
        toPrint += ''.join(str(" {}:{}".format(number,occurs)))
    return toPrint
    

    
if __name__ == '__main__':
    for arg in sys.argv[1:]:
        save(arg)
    print(show())

# print('Ładowanie modułu "{0}"'.format(__name__))
# ############################################
# def wypisz():
#     print('Wywołano funkcję "wypisz()" modułu "{0}"'.format(__name__))
# ############################################
# print('Załadowano moduł "{0}"'.format(__name__))