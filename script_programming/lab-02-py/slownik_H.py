# >>> import slownik_H
# Ładowanie modułu "slownik_H"
# Załadowano moduł "slownik_H"

# >>> slownik_H.wypisz()
# Wywołano funkcję "wypisz()" modułu "slownik_H"

# python3 slownik_H.py 2 2 3 5 10 2 3        

import sys

global slownik
slownik = {}

def save(num):
    try:
        slownik[int(num)] += 1
    except KeyError:
        slownik[int(num)] = 1
    return slownik

def show(): 
    toPrint  = ""
    for number, occurs in zip(slownik.keys(), slownik.values()):
        toPrint += ''.join(str(" {}:{}".format(number,occurs)))
    return toPrint
    

if __name__ == '__main__':
    for num in sys.argv[1:]:
        save(num)
    print(show())


# # ------------------------------------ # 
# print('Ładowanie modułu "{0}"'.format(__name__))
# ############################################
# def wypisz():
#     print('Wywołano funkcję "wypisz()" modułu "{0}"'.format(__name__))
# ############################################
# print('Załadowano moduł "{0}"'.format(__name__))