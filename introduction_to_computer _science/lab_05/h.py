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
    tablica_liczb1 = []
    while i <= iloczyn:
        tablica_liczb1.append(fibonacci(i))
        i+=1
        if(i > 100):
            break
    print(tablica_liczb1)

    for k in range(0, i-2):
        if(tablica_liczb1[k] * tablica_liczb1[k+1] == iloczyn):
            return print("Nasze liczby to ", tablica_liczb1[k], " i ", tablica_liczb1[k+1])
    print("Nie można stworzyć liczby z iloczynu dwóch liczb należących do ciągu fibonacciego")                    
liczba_wyb = int(input("Wprowadź liczbę naturalną: "))
if(liczba_wyb <= 0):
    print("Liczba nie jest naturalna!")

else:
    szukanie_iloczynu(liczba_wyb)