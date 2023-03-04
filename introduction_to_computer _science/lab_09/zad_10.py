# Proszę napisać program wczytujący tablicę dwuwymiarową o ustalonym wymiarze n×n wypełnioną liczbami naturalnymi.
# Dla danej tablicy należy napisać funkcję, która odpowiada na pytanie,
# czy w tablicy istnieje wiersz, w którym każda liczba zawiera co najmniej jedną cyfrę będącą liczbą pierwszą.
# Wymiar tablicy powinien być definiowany przez użytkownika.


from random import randint


def gen_tab(n):

    tab = [[randint(1, 100) for _ in range(n)]
           for _ in range(n)]  # generowanie listy n x n
    # tab = [
    #     [52, 68, 35, 9, 91, 1, 79, 86],
    #     [76, 43, 27, 62, 2, 64, 9, 47],
    #     [22, 83, 53, 17, 24, 27, 26, 36],
    #     [82, 78, 43, 46, 18, 38, 1, 58],
    #     [71, 22, 40, 15, 55, 94, 89, 26],
    #     [63, 93, 51, 18, 23, 59, 57, 27],
    #     [90, 24, 45, 79, 53, 29, 33, 80],
    #     [31, 35, 21, 86, 29, 32, 77, 24]
    #     ]
    # tab = [
    #     [36, 22, 88],
    #     [79, 83, 16],
    #     [45, 42, 86]
    #     ]
    print(tab)

    return tab


def is_prime(n):  # funkcja sprawdzajaca prime
    if n == 2 or n == 3:
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
    while num != 0:  # petla dziala dopóki liczba nie będzie 0
        if is_prime(num % 10):  # sprawdzanie czy druga cyfra jest l.pierwsza
            return True
        num //= 10  # dzielenie calkowite aby moc sprawdzic pierwsza liczbe
    return False


def problem_15(tab):
    long = len(tab)
    for i in range(long):  # range long jako dlugosc tablicy 2 petle
        flag = False
        for j in range(long):
            # sprawdzenie dla danego numeru tablicy oraz danego elementu
            if has_prime(tab[i][j]):
                flag = True  # jesli has_prime zwroci prawde to oczywiscie flaga jest na true, czyli istnieje taki wiersz
            else:
                flag = False
                break
        # jesli flaga jest true to oczywiscie istenieje taki rzad w tablicy[N][N]
        if flag:
            # zwracamy True oraz zwracamy tablice ktora spelnia warunki zadania
            return True, tab[i]
    return False, "Sorri, takiego wiersza brak :("


if __name__ == "__main__":
    while True:
        # wyjątek dla wprowadzonego n <= 1, (taka tablica, jest bezsensowna)
        try:
            n = int(input("Podaj wymiar n x n tablicy: "))
            if n <= 1:
                raise ValueError
        except ValueError:
            print("Sorri, Wprowadziłeś niepoprawne n, spróbuj ponownie:")
            continue
        Tabliczkaa = gen_tab(n)
        one, two = problem_15(Tabliczkaa)
        print(one, two)

#### Przypadki testowe ####
# Przykład nr 1:
# # tab = [
#     [52, 68, 35, 9, 91, 1, 79, 86],
#     [76, 43, 27, 62, 2, 64, 9, 47],
#     [22, 83, 53, 17, 24, 27, 26, 36],
#     [82, 78, 43, 46, 18, 38, 1, 58],
#     [71, 22, 40, 15, 55, 94, 89, 26],
#     [63, 93, 51, 18, 23, 59, 57, 27],
#     [90, 24, 45, 79, 53, 29, 33, 80],
#     [31, 35, 21, 86, 29, 32, 77, 24]
#     ]
# output: True [22, 83, 53, 17, 24, 27, 26, 36]
# Przykład nr 2:
# tab =[
#         [36, 22, 88],
#         [79, 83, 16],
#         [45, 42, 86]
#     ]
# output: False Sorri, takiego wiersza brak :(
# Przykład nr 3:
#               losowe liczby: n <= 0
# Przykład nr 4:
#       n = 1000 (PROBLEM?)
