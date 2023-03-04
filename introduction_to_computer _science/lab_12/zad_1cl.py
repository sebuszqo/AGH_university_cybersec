import time


class Kalkulator:
    def __init__(self):
        pass
    
    def multiply(tab):
        result = (tab[0][0] * tab[1][0], tab[0][1] * tab[1][1])
        return result

    def division(tab):
        result = (tab[0][0] * tab[1][1], tab[0][1] * tab[1][0])
        return result

    def adding(tab):
        result = (tab[0][0]*tab[1][1] + tab[1][0]
                  * tab[0][1], tab[0][1]*tab[1][1])
        return result

    def subtract(tab):
        result = (tab[0][0]*tab[1][1] - tab[1][0]
                  * tab[0][1], tab[0][1]*tab[1][1])
        return result

    def exp(tab):
        result = ((tab[0][0]**tab[1][0])**(1/tab[1][1]),
                  (tab[0][1]**tab[1][0])**(1/tab[1][1]))
        return result

    def skr(result):

        def nwd(a, b):
            while b:
                a, b = b, a % b
            return a

        div = nwd(abs(result[0]), abs(result[1]))

        return(f"{result[0]//div}/{result[1]//div}")


def gen_tuples():
    n = 2
    tab = []
    tab_of_tuples = []
    for i in range(n):
        def inputs():
            try:
                print(f"Podaj licznik oraz mianownik {i+1}-ego ułamka:")
                x, y = map(int, input().split())
                tab.append(x)
                tab.append(y)
                if y == 0:
                    raise ZeroDivisionError
            except ValueError:
                print("Wpisales cos nie tak sprobuj ponownie, ale np. ze spacja")
                inputs()
            except ZeroDivisionError:
                print("Wpisałeś zero jako mianownik, sprobuj ponownie")
                inputs()
        inputs()
        # a = int(input(f"Podaj licznik {i+1}-ego ułamka: "))
        # tab.append(a)
        # b = int(input(f"Podaj mianownik {i+1}-ego ułamka: "))
        # tab.append(b)
        tuple1 = tuple(tab)
        tab_of_tuples.append(tuple1)
        tab.clear()

    def printing(tab):
        if tab[0][0] < 0 or tab[0][1] < 0:
            print(f"Twój pierwszy ułamek ma postać: -{tab[0][0]}/{-tab[0][1]}")
        else:
            print(f"Twój pierwszy ułamek ma postać: {tab[0][0]}/{tab[0][1]}")
        print(f"Twój drugi ułamek ma postać: {tab[1][0]}/{tab[1][1]}")
    printing(tab_of_tuples)
    return tab_of_tuples


def check(tab):
    try:
        if tab[0][0] < 0 or tab[0][1] < 0 and tab[1][1] % 2 == 0:
            raise ValueError
        else:
            result = Kalkulator.exp(tab)
            print(
                f"Wynik potegowania tych 2 ułamków to: {tuple(result)}, w postaci skróconej {Kalkulator.skr(result)}, a w postaci zmiennoprzecinkowej: {round(result[0]/result[1],4)}")

    except ValueError:
        print("liczba ujemna pod pierwiastkiem, sprobuj ponownie ")
        time.sleep(2)
    return


if __name__ == "__main__":
    print()
    print("Witaj w Kalkulatorze ulamkow".center(200, " "))
    time.sleep(0.5)
    operation = None
    reset = True
    result = None
    calcOperations = ["+", "-", "*", "/", "**"]

    while True:

        if reset == True:
            tab = gen_tuples()
            reset = False

        operation = input(
            f"Podaj operacja jaka chcesz wykonać {str(calcOperations)} lub wpisz exit, jeśli chcesz zakończyć lub reset:")
        if operation == 'exit':
            break
        if operation == "reset":
            reset = True
            continue

        if not operation in calcOperations:
            print("Wprowadziłeś błędną operację.".center(200, " "))
            print()
            continue

        if operation == "+":
            result = Kalkulator.adding(tab)
            print(
                f"Wynik dodawania tych 2 ułamków to: {tuple(result)}, w postaci skróconej {Kalkulator.skr(result)}, a w postaci zmiennoprzecinkowej: {round(result[0]/result[1],4)}")
        elif operation == "-":
            result = Kalkulator.subtract(tab)
            print(
                f"Wynik odejmowania tych 2 ułamków to: {tuple(result)}, w postaci skróconej {Kalkulator.skr(result)},   a w postaci zmiennoprzecinkowej: {round(result[0]/result[1],4)}")
        elif operation == "*":
            result = Kalkulator.multiply(tab)
            print(
                f"Wynik mnożenia tych 2 ułamków to: {tuple(result)}, w postaci skróconej {Kalkulator.skr(result)}, a w postaci zmienno przecinkowej: {round(result[0]/result[1],4)}")
        elif operation == "/":
            result = Kalkulator.division(tab)
            print(
                f"Wynik dzielenia tych 2 ułamków to: {tuple(result)}, w postaci skróconej {Kalkulator.skr(result)}, a w postaci zmiennoprzecinkowej: {round(result[0]/result[1],4)}")
        elif operation == "**":
            print(check(tab))
        e = input(
            f"Jesli chcesz zakonczyc program to wpisz 'exit' lub kliknij 'enter': ")
        if e == "exit":
            break
        else:
            reset = True
            continue


## T