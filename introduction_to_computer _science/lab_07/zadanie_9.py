# Proszę napisać program, który pobierze od użytkownika 5 różnych liczb całkowitych i doda je do listy. 
# Program ma za zadanie uzupełnić listę liczbami całkowitymi znajdującymi się pomiędzy kolejnymi liczbami a następnie wypisać listę. 
# Należy obsłużyć wyjątek, w którym dwie sąsiadujące ze sobą wprowadzone przez użytkownika liczby są takie same. 

#1 funkcja sprawdzająca czy 2 liczby pod rząd nie są takie same
def check(results):
    try:
        print("Podaj 5 liczb, które mam wpisac do tablicy i ją uzupełnić:")
        results.append(int(input("Nr 1: ")))
        results.append(int(input("Nr 2: ")))
        results.append(int(input("Nr 3: ")))
        results.append(int(input("Nr 4: ")))
        results.append(int(input("Nr 5: ")))
        for i in range (0, (len(results) - 1)):
            if results[i] == results[i + 1]:
                results.clear()
                raise ValueError
        return True
    except ValueError:
        print("2 liczby sa takie same, spróbuj ponownie.")
        
        
# 2-gas funkcja wykonująca głowne zadanie tj. dopisywanie do listy brakujących elementów 
def add(results):
    for a in range(0, len(results) - 1): #głowna petla w zakresie dlugosci listy -1, tak zeby program nie pobierał kolejnego wyrazu z listy tj. [0]
        if results[a] > results[a+1]: #sprawdzenie czy dany element listy jest wiekszy niz nastepny
            l = results[a]      
            for l in range(results[a], results[a+1] + 1, - 1):  # petla w zakresie od wartosci liczby [...] do wartosci [...+1] dopisuje coraz to mniejsze liczby o 1 w dol (.../.../-1)
                results.append(l)

        elif results[a] < results[a+1]: # warunek odwrotny
            l = results[a]
            for l in range(results[a], results[a+1] + 1):
                results.append(l)
    del results[0:5] # usuniecie pierwszych 4 wyrazow 
    return results # zwrocenie listy z dopisanymi wyrazami

if __name__ == '__main__':
    results = [] # stworzenie pustej listy ktora bedzie dalej uzupelnniana 
    while True:
        if check(results) == True: #warunek czy 2 liczby sie nie powtarzaja
            add(results) # wywolanie funkcji
            print(results) #print returna tj. listy zwroconej
            results.clear() #wyczyszczenie listy i przygotowanie jej na nastepne dane
        else:
            continue

#####Przypadki testowe#####
# Przypadek 1:
# nr1 = 20 
# nr2 = 30 
# nr3 = 10 
# nr4 = 5 
# nr5 = 10
# return: [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 10, 9, 8, 7, 5, 6, 7, 8, 9, 10]
# Przypadek 2(Wyjątek):
# nr1 = 200 
# nr2 = 10
# nr3 = 150
# nr4 = 150
# nr5 = 100
# return : 2 liczby sa takie same, sprobuj ponownie
# Przypadek 3:
# nr1 = 10
# nr2 = 1005
# nr3 = 1010
# nr4 = 1000
# nr5 = 1015
# return:
# Przypadek 4 (problem?):
# nr1 = 10
# nr2 = 1000000
# nr3 = 100000
# nr4 = 15000
# nr5 = 15100
# return:
############################