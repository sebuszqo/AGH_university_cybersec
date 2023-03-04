def fibonacci(n):
    pierwszy = 0
    drugi = 1
    for i in range(n):
        var = drugi
        drugi += pierwszy
        pierwszy = var
    return drugi

def szukanie_iloczynu(iloczyn):
    i = 1
    tablica_liczb = []
    while i <= iloczyn:
        tablica_liczb.append(fibonacci(i))
        i+=1
        if(i > 100):
            break
    #print(tablica_liczb)

    for k in range(0, i-1):
        for l in range(0, i-1):
            if(tablica_liczb[k] * tablica_liczb[l] == iloczyn):
                return print("Nasze liczby to ", tablica_liczb[k], " i ", tablica_liczb[l])
    print("Nie można stworzyć liczby z iloczynu dwóch liczb należących do ciągu fibonacciego")

while True:
    try:
        liczba_wyb = int(input("Wprowadź liczbę naturalną: "))
        if(liczba_wyb <= 0):
            raise

        else:
            szukanie_iloczynu(liczba_wyb)
    except:
        print("Wprowadzone sformułowanie jest nieprawidłowe!")

#Przypadki testowe
# liczba = -1    ODP: Wprowadzone sformułowanie jest nieprawidłowe!
# liczba = "cat"    ODP: Wprowadzone sformułowanie jest nieprawidłowe!
# liczba = 6     ODP: 2 i 3
# liczba = 104  ODP: 8 i 13
# liczba = 2322818928486048521598349680614446   ODP: 37889062373143906 i 61305790721611591
############################################################################################