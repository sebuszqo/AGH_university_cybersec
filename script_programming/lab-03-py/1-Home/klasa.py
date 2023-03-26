# everything from this lab is in DealerSystem or DeanerySystem

import sys
##################################
# python3 -i klasa.py

# obiekt = Klasa() --> Wywołano metodę '__init__()' obiektu '4307696176'
# obiekt = None
# obiekt = Klasa() --> Wywołano metodę '__init__()' obiektu            '4307684416'
#  --> Wywołano metodę '__del__()' obiektu             '4307696176'
# obiekt = Klasa() --> Wywołano metodę '__init__()' obiektu            '4307695984'
#  --> Wywołano metodę '__del__()' obiektu             '4307684416'
# obiekt --> Wywołano metodę '__repr__()' obiektu            '4307695984'
# print(obiekt) --> Wywołano metodę '__str__()' obiektu             '4307695984'
# obiekt.metodaInstancyjna() --> Wywołano metodę 'metodaInstancyjna()' obiektu   '4307695984'
# Klasa.metodaKlasowa() --> Wywołano metodę 'metodaKlasowa()' klasy         'Klasa'
# Klasa.metodaStatyczna() --> Wywołano metodę 'metodaStatyczna()' klasy       'Klasa'

##################################

def color(id):
    return "38:5:{}".format(id % 15)

##################################

class Klasa():
    tab = [1,2,3]

    def __init__(self,tab = tab, zmienna1 = 0, zmienna2 = 0):
        self.tab = tab
        self._zmienna1 = zmienna1
        self.__zmienna2 = zmienna2
        print("Wywołano metodę '{name}()' obiektu\t\t'\033[{color}m{id}\033[0m'".format(name=sys._getframe().f_code.co_name, color = color(id(self)), id = id(self)))

    def __del__(self):
        print("Wywołano metodę '{name}()' obiektu\t\t'\033[{color}m{id}\033[0m'".format(name=sys._getframe().f_code.co_name, color = color(id(self)), id = id(self)))

    def __str__(self):
        return "Wywołano metodę '{name}()' obiektu\t\t'\033[{color}m{id}\033[0m'".format(name=sys._getframe().f_code.co_name, color = color(id(self)), id = id(self))

    def __repr__(self):
        return "Wywołano metodę '{name}()' obiektu\t\t'\033[{color}m{id}\033[0m'".format(name=sys._getframe().f_code.co_name, color = color(id(self)), id = id(self))

    def metodaInstancyjna(self):
        print("Wywołano metodę '{name}()' obiektu\t'\033[{color}m{id}\033[0m'".format(name=sys._getframe().f_code.co_name, color = color(id(self)), id = id(self)))

    @classmethod
    def metodaKlasowa(cls):
        print("Wywołano metodę '{name}()' klasy\t\t'\033[1m{cls}\033[0m'".format(name=sys._getframe().f_code.co_name, cls=cls.__name__))

    @staticmethod
    def metodaStatyczna():
        print("Wywołano metodę '{name}()' klasy\t'\033[1m{cls}\033[0m'".format(name=sys._getframe().f_code.co_name, cls=__class__.__name__))
    
    def metodaInstancyjna(self):
        print(f"tab klasowa: {Klasa.tab}\ntab instancyjna = {self.tab}")
print("Załadowano zawartość pliku '{name}'".format(name=__file__))


obiekt = Klasa([4, 5, 6], 10, 20)
obiekt.metodaInstancyjna()
print(obiekt.tab)
print(obiekt._zmienna1)
print(obiekt._Klasa__zmienna2)