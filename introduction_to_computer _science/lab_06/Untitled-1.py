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
        print("Sformułowanie jest nieprawidłowe")

# Przypadki testowe
# liczba = 6 odp: 2 i 3
# liczba = -1 odp: "nie jest naturalna dodatnia"
# liczba = "catanddog" odp: "wprowadzone sformułowanie jest nieprawidłowe"
# liczba = 104 odp: 8 i 13
# liczba = 6472224534451830
# liczba = 209448452121801024948543882840840
###################################################