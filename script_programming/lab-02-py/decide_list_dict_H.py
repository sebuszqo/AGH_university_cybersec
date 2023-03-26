from ast import arg
import sys, lista_H, slownik_H

if __name__ == "__main__":
    args = sys.argv[1:]

    if args[0] == "--lista":
        for num in args[1:]:
            lista_H.save(int(num))
        print(lista_H.show())
    elif args[0] == "--slownik":
        for num in args[1:]:
            slownik_H.save(int(num))
        print(slownik_H.show())
    else:
        print("Avalible options: --lista --slownik")

# python3 decide_list_dict_H.py --lista 1 1 11 11 3 5 5 4
# python3 decide_list_dict_H.py --slownik 1 1 22 22 3 4 5 5