import sys # import sys --> aby uzyskac dostep do argumentow wiersza polecen 

# python3 skrypt.py 3 2 ala

def is_prime(number):
    try:
        number = int(number)
        if number <= 1:
            return False
        for i in range(2,int(number / 2 + 1)):
            if (number % i) == 0:
                return False
        return True
    except:  # lapanie errow --> spowodowanych napisami
        # print('Error has occured, probably string not an int')
        return False 

if __name__ == '__main__':
    for arg in sys.argv[1:]: # --> biore argumenty od 1 dalej poniewaz arg 0 to 'skrypt.py'
        if is_prime(arg):
            print(arg)

