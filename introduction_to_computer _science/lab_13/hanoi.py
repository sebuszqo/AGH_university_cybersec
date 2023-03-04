
'''
def hanoi(n, A, B, C):

    if n > 0:
        hanoi(n-1, A, C, B)
        print(A, "-->", C)
        hanoi(n-1, B, A, C)

n=3
hanoi(n,"A", "B", "C")
print(f"Ilość ruchów: {(n**2)-1}")      
'''
# mozliwe miejsca numerycznie to : 1 2 3 
#poczatkowe + tymczasowe + docelowe = 1 + 2 + 3 = 6
# tymczasowe = 6 - poczatkowe - docelowe = 3
# dla przełożenia 1 2 miejsce tymczasowe = 6 - 1 - 2 = 3
# dla przełożenia 1 oraz 3 miejsce tymczasowe = 6 - 1 - 3 = 2
# dla przełozenia 2 oraz 3 miejsce tymczasowe = 6 - 2 - 3 = 1
def hanoi(n,m_pocz,m_docelowe): 
    if n ==1:
        print(f"element nr 1:  {m_pocz} --> {m_docelowe}")
    else:
        m_tymcza = 6 - m_docelowe - m_pocz
        # 3 kroki
        # 1 krok przeniesienie wiezy o 1 mniejszej z miejsca poczatkowego na miejsce docelowe
        hanoi(n-1,m_pocz,m_tymcza)
        # 2 krok najwiekszy element na miejsce docelowe (numer najwiekszego = aktualny rozmiar)
        print(f"element nr {n}: {m_pocz} --> {m_docelowe}")
        # 3 krok przeniesienie wiezy o 1 mniejszej z miejsca tymczasowego na docelowe
        hanoi(n-1,m_tymcza,m_docelowe)


n = int(input("Podaj liczbe krążków: "))
hanoi(n,m_pocz=1,m_docelowe=2)
print(f"liczba ruchów to: {(n**2)-1}")