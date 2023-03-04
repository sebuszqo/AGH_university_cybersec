if __name__ == '__main__':
    print("Witaj w programie, prosze podac 2 liczby oraz znak dzialania jaki chcesz wykonac :)")
    number1 = int(input("prosze podac liczbe numer 1: "))
    sign = input("podaj znak dzialania: ")
    number2 = int(input("prosze podac liczbe numer 2: "))
    if number1 <= 0 and number2 <= 0:
        print("Niestety podane liczby nie spelniaja wymagan")
        SystemExit
    elif number1< 0:
        number1= number1*-1
    elif number2 <0:
        number2= number2*-1
        if sign == "+":
            operation = number1 + number2
            print(f"Twoj wynik dodawania to: {operation}")
        elif sign == "-":
            operation = number1 - number2
            print(f"Twoj wynik odejmowania to: {operation}")
        elif sign == "*":
            operation = number1 * number2
            print(f"Twoj wynik mnozenia to: {operation}")
            if operation == 10: 
                print("YAY")
        elif sign == "/":
            operation = number1 / number2
            print(f"Twoj wynik dzielenia to: {operation}")
        elif sign =="^":
            operation1 = number1*number1
            operation2 = number2*number2
            print(f"Liczby podniesione do kwadratu to: {operation1, operation2}")   
    
    
        


