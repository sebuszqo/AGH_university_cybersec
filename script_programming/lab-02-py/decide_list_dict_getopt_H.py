import getopt
import sys, lista_H, slownik_H

if __name__ == "__main__":
    opts, args = getopt.getopt(sys.argv[1:], "x", ['module='])

    if opts[0][1] == "lista":
        for num in args:
            lista_H.save(int(num))
        print("Liczby to: {}".format(lista_H.show()))
    elif opts[0][1] == "slownik": 
        for num in args:
            slownik_H.save(int(num))
        print("Liczby to: {}".format(slownik_H.show()))
    else:
        print("Mozliwe opcje: --m=lista lub --m=slownik")

# python3 decide_list_dict_getopt_H.py --m=lista 1 1 11 11 3 5 5 4
# python3 decide_list_dict_getopt_H.py --m=slownik 1 1 22 22 3 4 5 5