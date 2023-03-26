import re, sys

def reg(text):
    for num in re.findall('[-]?[0-9]+',text):
        # print(num)
        # print(type(num))
        yield(int(num))
    for word in re.findall('[a-zżźćńąśłęóA-ZŻŹĆŃĄŚŁĘÓ]+', text):
        yield(str(word))

def start():
    while True:
        try:

            for element in reg(str(sys.stdin.readline())):
                if type(element) == int:
                    print(f'\tLiczba: {element}')
                elif type(element) == str:
                    print(f'\tWyraz: {element}')
        except KeyboardInterrupt:
            print("Error/Exit msg")
            break

if __name__ == "__main__":
    start()
