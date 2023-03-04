import random
import math
import sys

print("-----------")
print("Kalkulator")
print("-----------")
while True:
    print("Wpisz 2 liczby na ktorych chcesz wykonywac dzialanie, a nastepnie znak tego dzialania, jeśli chcesz poznac legendę dzialań, wpisz 'info'")
    first = input("Liczba nr 1 lub pomoc: ")
    while first == "info":
        print("dodawanie: + \nodejmowanie: - \nmnożenie: * \ndzielenie: / \npotegowanie: ** \npierwiastkowanie liczb: ^ \nlosowanie liczb: x \nzakoncz program: 8")
        print()
        first = input("Liczba nr 1: ", )
        break
    first = int(first)
    second = int(input("Liczba nr 2: "))
    third = input("znak działania: ")

    if(third == '+'):
        result = first + second
    elif(third == '-'):
        result = first - second
    elif(third == '*'):
        result = first * second
    elif(third == '/'):
        result = first / second
    elif(third == '**'):
        result = first ** second
    elif(third == '^'):
        result = first**(1/second)
    elif(third == 'x'):
        result = random.randrange(first, second)
    elif(third == "8"):
        sys.exit(0)
    else:
        print("niepoprawny znak. Spróbuj jeszcze raz:")
        continue

    print(f"Twój wynik to: {result}")
    print('Czy chcesz wprowadzić nowe dane? T-tak N-nie: ', end='')
    new = input(":")
    if(new == "T" or new == "t"):
        continue
    elif(new == "N" or new == "n"):
        break
