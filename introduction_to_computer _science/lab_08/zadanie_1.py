import random
from typing import Counter

def prime(a):  # funkcja sprawdzajaca czy liczba jest pierwsza
    if a == 2 or a == 3:
        return True
    elif a % 2 == 0 or a % 3 == 0 or a <= 1:
        return False
    i = 5
    while i*i < a:
        if a % i == 0 or a % (i+2) == 0:
            return False
        i += 6
    return True

def nwd(first, second):  # funkcja szukajaca NWD z dwoch liczb
    if second == 0:
        return first
    else:
        s = first % second
        return nwd(second, s)


def problem(tab):  # glowna funkcja dopisujaca oraz sumujaca
    long = len(tab)
    counter = 0  # licznik liczb pierwszych w danej liscie
    for i in range(long):  # pierwsza petla sprawdzajaca ilosc liczb pierwszych w tablicy
        if prime(tab[i]):
            counter += 1
    long += counter
    for i in range(long):  # druga petla dodajaca 0 po kazdej liczbie pierwszej
        a = tab[i]
        if prime(a):  # moduł .insert (miejsce w tablicy, wartosc) dodaje 0
            tab.insert(i + 1, 0)
        else:
            continue
    print(tab)  # print listy nr 1
    tab2 = []  # druga tablica ktora ma przechowywac sumy podzbiorów
    sum = 0
    for s in range(long):
        if tab[s] != 0:  # warunek na wykrycie 0 w tablicy
            sum += tab[s]
        else:
            # jesli nie bedzie 0 to dopisze wczesniej policzona sume do nowej tablicy
            tab2.append(sum)
            sum = 0  # wyzerowanie "licznika" sumy aby mozna bylo liczyc kolejny podzbior
    print(tab2)  # print listy nr 2
    if len(tab2) >= 2:  # warunek na dlugosc tablicy ktora ma byc sprawdzona nwd
        first = tab2[0]
        second = tab2[1]
        wynik = nwd(first, second)
        return print(f"NWD 2 pierwszych liczb to: {wynik}")

if __name__ == '__main__':
    # przypadki generowane poprzez losowanie liczb
    while True:
        try:
            n = int(input("Podaj ile liczb mam wpisac w tablice: "))
            if n<= 0:
                raise ValueError
            tab = [random.randint(1, 100) for i in range(n)]
            problem(tab)
        except ValueError:
            print("Podałeś złą wartość n, spróbuj ponownie")

    # przypadki testowe do sprawdzenia recznego.
    # tab = [7, 45, 45, 34, 53, 45, 4, 3, 11, 18, 30]
    # tab = [63, 60, 53, 1, 93, 2, 15, 4, 17, 80]
    # tab = [52, 95, 26, 13, 46, 39, 27, 45, 87, 80, 77, 77, 93, 17, 43]
    # problem(tab)


    ##### Przypadki testowe #####
    # Przypadek nr 1:
    # output: lista po dodaniu 0 [52, 95, 26, 13, 0, 46, 39, 27, 45, 87, 80, 77, 77, 93, 17, 0, 43, 0] Wynik: [186, 588, 43]
    # Przypadek nr 2:
    # output: lista po dodaniu 0 [7,0,45,45,34,53,0,45,4,3,0,11,0,18,30]. Wynik: [7, 177, 52, 11]
    # Przypadek nr 3:
    # output: lista po dodaniu 0 [63, 60, 53, 0, 1, 93, 2, 0, 15, 4, 17, 0, 80] Wynik: [176, 96, 36]
    # Przypadek nr 4: 
    # output: list po dodaniu 0 [65, 3, 0, 17, 0, 83, 0, 44, 23, 0, 43, 0, 15, 82, 49]  Wynik: [68, 17, 83, 67, 43]
    # Przypadki kolejne:
    # Program jako głowne zalozenie ma generowac liczby losowe i wpisywac je do tablicy, tak wiec reszta sprawdzen moze zostac wykonana na losowo dobranych tabliach:
    # Przypadek z problemem:
    # gdy n =1000000, progam ma problem.
