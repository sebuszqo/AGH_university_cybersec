# metody magiczne --> __...__ - to są metody magiczne !
# mają specjalne zastosowanie
# przeladowywanie metod
import math 

class Punkt2D:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.odl = math.sqrt( x**2 + y**2 )

    def __add__(self, point):
        return Punkt2D(self.x + point.x, self.y + point.y)
    
    def __str__(self) -> str:
        return f'{self.x} {self.y}'
    
    # def __sub__(self)

    def __lt__(self, point) -> bool:
        return self.odl < point.odl
    
    def __eq__(self, point) -> bool:
        return self.x == point.x and self.y == point.y
    
    def __len__(self):
        return int(round(self.odl,0))


p1 = Punkt2D(2,4)
p2 = Punkt2D(1,6)
p3 = p1 + p2
print(p1 < p2)
print(p1 == p2)
print(p3)


# dziedziczenie
class Animal:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

class Dog(Animal):
    def getDogVoice(self):
        print('hau hau')

class Wolf(Dog):
    def getWolfVoice(self):
        print('Jestem wilkiem,')
        super().getDogVoice() 

class Cat(Animal):
    def getCatVoice(self):
        print('miau miau')

cat = Cat('kotek', 3)
cat.getCatVoice()
dog = Dog('reksio', 2)
dog.getDogVoice()
wolf = Wolf('Wilk', 2)
wolf.getWolfVoice()

