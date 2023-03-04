def fibonacci(n):
    pierwszy = 0
    drugi = 1
    for i in range(n):
        var = drugi
        drugi += pierwszy
        pierwszy = var
    return pierwszy

def wpisywanie(tab):
    # Start
    akt_elemx = int((len(tab)-1)/2)
    akt_elemy = int((len(tab)-1)/2)

    # Poruszanie się
    # lewo = 0
    # dół = 1
    # prawo = 2
    # góra = 3
    liczba_ruchow = 1
    temp = liczba_ruchow # Przypisanie wartości, gdyż zmienna "liczba_ruchów" jest zmienna
    pocz_kierunku = 1 # w jakim kierunku zaczniemy się poruszać

    # Przypisanie początkowych wartości
    nr_fib = 1
    tab[akt_elemx][akt_elemy] = fibonacci(nr_fib)
    for i in range(1 + 2 * (len(tab) - 1)): # Ile zmian kierunku dokonamy
        akt_ruch = pocz_kierunku % 4 # Aktualny kierunek
        while liczba_ruchow > 0:
            nr_fib += 1
            if akt_ruch == 0:
                akt_elemy -= 1
                if akt_elemx < len(tab) and akt_elemy < len(tab) and akt_elemx >= 0 and akt_elemy >= 0: # By nie wyszło poza tablicę
                    tab[akt_elemx][akt_elemy] = fibonacci(nr_fib)
            elif akt_ruch == 1:
                akt_elemx += 1
                if akt_elemx < len(tab) and akt_elemy < len(tab) and akt_elemx >= 0 and akt_elemy >= 0:
                    tab[akt_elemx][akt_elemy] = fibonacci(nr_fib)
            elif akt_ruch == 2:
                akt_elemy += 1
                if akt_elemx < len(tab) and akt_elemy < len(tab) and akt_elemx >= 0 and akt_elemy >= 0:
                    tab[akt_elemx][akt_elemy] = fibonacci(nr_fib)
            elif akt_ruch == 3:
                akt_elemx -= 1
                if akt_elemx < len(tab) and akt_elemy < len(tab) and akt_elemx >= 0 and akt_elemy >= 0:
                    tab[akt_elemx][akt_elemy] = fibonacci(nr_fib)
            liczba_ruchow -= 1

        temp += 1/2 # Bo liczbę ruchów zmieniamy, co 2 pętle
        liczba_ruchow = int(temp)
        pocz_kierunku += 1
    return tab

try:
    roz_tab = int(input("Wprowadź rozmiar tabeli: "))
    if roz_tab <= 0:
        raise ValueError

    tabela = [[0 for i in range(roz_tab)]for j in range(roz_tab)]
    tabela = wpisywanie(tabela)
    for i in range(len(tabela)):
        for j in range(len(tabela)):
            print(tabela[i][j], end = ' ')
        print()

except ValueError:
    print("Sformułowanie jest niepoprawne!!!")

###############Przypadki Testowe###############
# roz_tab = -1
# roz_tab = "abcd"
# roz_tab = 1
# roz_tab = 4
# roz_tab = 70
###############################################

