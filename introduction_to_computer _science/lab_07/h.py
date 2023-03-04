def sito_eratostensa(n):
    tablica = [True for i in range(n + 1)] #Przypisanie do wszystkich elementów w tablicy false
    i = 2
    while i * i <= n:
        if tablica[i]: #Jeżeli liczba nie jest pierwsza, to nie wykonujemy już usuwania
            j = i + i
            while j <= n:
                tablica[j] = False
                j += i
        i+=1

    # Przypisanie liczb pierwszych do tablicy
    liczby_pierwsze = []
    for i in range(2, n):
        if tablica[i] == True:
            liczby_pierwsze.append(i)
    return liczby_pierwsze

def reszty_liczb_pierwszych(tab_liczb_pier):
    for i in range(1, len(tab_liczb_pier)):
        print(f"Dla liczb {tab_liczb_pier[i]}:{tab_liczb_pier[i - 1]} reszta wynosi: ", end = '')
        print(tab_liczb_pier[i] % tab_liczb_pier[i - 1])

try:
    liczba = int(input("Wprowadź liczbę: "))
except:
    print("Wprowadzone sformułowanie jest nieprawidłowe")

else:
    try:
        if liczba <= 1:
            raise ValueError

        else:
            liczby_pierwsze = sito_eratostensa(liczba)
            #print(liczby_pierwsze)
            reszty_liczb_pierwszych(liczby_pierwsze)

    except ValueError:
        print("Liczba jest mniejsza od 1")

################DANE TESTOWE#################
# tekst
# -1
# 1
# 2 i 3
# 4
# 100
# 1000000
############################################