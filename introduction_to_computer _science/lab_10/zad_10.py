
def words(str, s):
    if s == "Y" or s == "y":
        print(str)
    elif s == "N" or s == "n":
        pass
    split = list(str.split())
    print()
    return f"Plik ten zawiera: {len(split)} słów"


if __name__ == "__main__":
    while True:
        f_names = {"1": "lorem.txt", "2": "opis_kota.txt",
                   "3": "opis_psa.txt", "4": "opis_małpy.txt"}
        print()
        n = input(f"Witaj użytkowniku, wybierz który plik chcesz sprawdzić:\n {f_names} \n:")
        try:
            key_to_lookup = f"{n}"
            if key_to_lookup in f_names:
                file_r = f_names[n]
                s = input("Czy chcesz wyświetlić ten plik ? (Y/N): ")
                with open(file_r, "r", encoding="utf-8") as f:
                    str = f.read()
                print()
                print(words(str, s))
            else:
                raise KeyError
        except KeyError:
            print()
            print("podany klucz nie istnieje, spróbuj ponownie")
            continue

### Przypadki testowe ###
# Plik nr 1 (lorem.txt):
# Ilość słów: 117
# Plik nr 2 (opis_kota.txt):
# Ilość słów: 39
# Plik nr 3 (opis_psa.txt):
# Ilość słów: 359 (359 słów zamiast 361 ?)
# Plik nr 4 (opis_małpy.txt):
# Ilość słów: 275
