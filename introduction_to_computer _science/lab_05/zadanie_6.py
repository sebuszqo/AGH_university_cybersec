def prime(number):
    if number == 2:
        return True
    elif number % 2 == 0 or number <= 1: #wyrzucone liczby parzyste, wiec w dalszym kroku mozna nie sprawdzac podzielnosci przez l.parzyste
        return False
    for f in range(3, int(number/2)+1,2): 
        if number % f == 0:
            return False
    return True

while True:
    number = int(input("Podaj liczbe jaka mam sprawdzic: "))
    print()
    prime(number)
    if prime(number) == False:
        print("Twoja liczba nie jest pierwsza")
        while prime(number) == False:
            number += 1
        print(f'Najblizsza większa liczba pierwsza to: {number}')
        print()
    else:
        print("Podana liczba jest liczba pierwszą")
        print()




# b = int(input("Podaj koncowy przedzial: "))
# for number in range(2,b):
#     print(number, prime(number))











# number = int((input(":")))
# prime(number)

# if prime == True:
#     print("Podana liczba jest pierwsza")
# else:
#     print("Podana liczba nie jest pierwsza")


# if prime(number) == False:
#     print("Liczba nie jest pierwsza")
# else:
#     print("Liczba jest pierwsza")
