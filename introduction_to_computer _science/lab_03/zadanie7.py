if __name__ == '__main__':
    a = int(input("Podaj liczbe 1 z zakresu: "))
    b = int(input("Podaj liczbe 2 z zakresu: "))
    if b-a <20:
        for i in range (a,b):
            print(i)
    elif b-a >20:
        c = int((b+a)/2)
        for i in range (c-3,c+3):
            print(i)
            
    