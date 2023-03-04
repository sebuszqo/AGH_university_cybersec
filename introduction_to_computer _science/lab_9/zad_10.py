from random import randint

def gen_tab(n):
    tab = [[randint(1, 100) for _ in range(n)]for _ in range(n)] # generowanie listy n x n
    tab = [
        [52, 68, 35, 9, 91, 1, 79, 86], 
        [76, 43, 27, 62, 2, 64, 9, 47], 
        [22, 83, 53, 17, 24, 27, 26, 36], 
        [82, 78, 43, 46, 18, 38, 1, 58], 
        [71, 22, 40, 15, 55, 94, 89, 26], 
        [63, 93, 51, 18, 23, 59, 57, 27], 
        [90, 24, 45, 79, 53, 29, 33, 80], 
        [31, 35, 21, 86, 29, 32, 77, 24]
        ]
    print(tab)
    
    return tab

def is_prime(n):  # funkcja sprawdzajaca prime
    if n==2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0 or n < 2:
        return False
    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6
    return True

def has_prime(num):
    while num != 0:
        if is_prime(num % 10): # spradzamy czy jest to liczba pierwsza
            return True
        num //= 10 # dzielimy przez 10 calkowicie zeby "Obciac" prawa strone i sprawdzic nastepna cyfre
    return False

def problem_15(tab):
    long  = len(tab)
    for i in range(long): # range long jako dlugosc tablicy 2 petle 
        flag = False
        for j in range(long):
            if has_prime(tab[i][j]): # wybieramy wedlug iteracji i oraz j sprawdzajac czy jest ona liczba pierwsza
                flag = True
            else:
                flag = False # jesli dana liczba w tablicy nie bedzie miala liczby pierwszej to sprawdzimy kolejna liczbe w tablicy 
                break
        if flag:
            return True, tab[i] # zwracamy tablice ktora posiada te liczby pierwsze
    return False, "nie ma takiego wiersza" # brak tablicy oznacza ze nie ma takiego wiersza i jest fałsz
        
if __name__ == "__main__":
    try:
        n = int(input("podaj wymiar n x n tablicy: "))
        if n <= 0:
            raise ValueError
    except ValueError:
        print("wprowadziłeś niepoprawne n, spróbuj ponownie:")
    Tabliczkaa= gen_tab(n)
    one, two = problem_15(Tabliczkaa)
    print(one, two)


   