
if __name__ == '__main__':
    balance = 2894
    print("Witaj użytkowniku")
    print("Podaj kod PIN:")
    PIN = int(input(":"))
    if PIN == 1122:
        print("Podałeś prawidłowy PIN")
        print("Z ktorej funkcji chcesz skorzystac, wybierz numer: \n 1)Wplatomat \n 2)Bankomat \n 3)Sprawdz saldo \n 4)Wyjscie")
        no = int(input(":"))
    else:
        print("Podałeś nieprawidłowy PIN")
        SystemExit
    counter = 0
    while counter == 0:
            if no == 1:
                print("Jaką sumę pieniędzy chcesz wpłacić na swoje konto")
                into = int(input(":"))
                print(f"Po tej wpłacie twój aktualny stan konta wynosi: {balance + into}")
                counter += 1
            if no == 2:
                ntry = 0
                while ntry == 0:
                    print(f"Aktualny stan konta wynosi: {balance}")
                    print("Jaka sumę pieniedzy chcesz wypłacić?") 
                    withdraw = int(input(":"))
                    if withdraw < balance:
                        print("Posiadasz tyle srodków na koncie. Za chwile zostaną wypłacone pieniądze. Dzię1kujemy za skorzystanie z bankomatu. Miłego Dnia")
                        ntry += 1
                        counter += 1
                    else:
                        print("Nie posiadasz tyle dostępnych srodków na koncie. Spróbuj ponownie wykonać całą operację.")              
            if no == 3:
                print(f"Twoj aktualny stan salda wynosi:{balance}")
                counter += 1
            if no == 4:
                print("Dziekujemy za skorzystanie z naszych uslug. Transakcja zostala anulowana.")
                counter +=1
                SystemExit
            if no == "exit" and into=="exit" and withdraw == "exit":
                break

