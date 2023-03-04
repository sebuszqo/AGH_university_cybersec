# Do funkcji przekazywana jest lista z dowolną liczbą elementów. Drugim argumentem funkcji jest nowy alfabet. Ustal, czy słowa w liście są ułożone zgodnie z tym nowym alfabetem.
# is_sorted(["hello", "emma"], "hlabcdefgijkmnopqrstuvwxyz") ➞ True
# is_sorted(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz") ➞ False
# is_sorted(["apple", "app"], "abcdefghijklmnopqrstuvwxyz") ➞ False
# is_sorted(["down", "funny", "carrot", "vote"], "abdefghijklmnopqrstcuvwxyz") ➞ True

from typing import Type
import sys

def is_sorted(lista, alfabet):
   # Sprawdzamy dla kolejnych dwóch słów 
    for i in range(len(lista) - 1):
      indeks1 = 0
      indeks2 = 0
      licznik = 0
      # Zapętluj dopóki kolejne litery się powtarzają
      while indeks1 == indeks2:
         # Jeżeli np. app i apple, to dla 3. zapętlenia wyjdzie poza zakres, więc wtedy wybieramy krótsze słowo
         if licznik == len(lista[i]) or licznik == len(lista[i + 1]):
            if len(lista[i]) <= len(lista[i + 1]):
               return True
            else:
               return False

         # Szukamy, jaką wartość w alfabecie ma nowa litera
         indeks1 = alfabet.find(lista[i][licznik])
         indeks2 = alfabet.find(lista[i + 1][licznik])

         # Sprawdzamy czy nie są to te same litery, jeżeli nie, to czy są w odpowiedniej kolejności alfabetycznej
         if indeks1 != indeks2:
            if indeks1 <= indeks2:
               continue
            else:
               return False
         else:
            licznik+=1
    return True

try:
   ilosc_elem = int(input("Ile chcesz mieć elementów w liście: "))
   if ilosc_elem <= 0:
      raise ValueError
except ValueError:
   print("Wprowadzone sformułowanie jest nieprawidłowe!!!")

else:
   lista = []
   for i in range(ilosc_elem):
      try:
         temp = input(f"{i+1} element: ")
         temp.lower()
         for j in range(len(temp)):
            if temp[j] in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
               continue
            else:
               raise TypeError
         lista.append(temp)
      except TypeError:
         print("Wprowadzone słowo zawiera intruzów!!!")
         sys.exit()

   alfabet = input("Wpisz swój alfabet: ")
   print(is_sorted(lista, alfabet))

###############Przypadki testowe################
# n = -1
# n = sth
# temp = 131fe
# temp = {]:few}
# is_sorted(["b", "a"], "hlbacdefgijkmnopqrstuvwxyz") ➞ True
# is_sorted(["hello", "emma"], "hlabcdefgijkmnopqrstuvwxyz") ➞ True
# is_sorted(["apple", "app"], "abcdefghijklmnopqrstuvwxyz") ➞ False
# is_sorted(["down", "funny", "carrot", "vote"], "abdefghijklmnopqrstcuvwxyz") ➞ True
# is_sorted(["down", "funny", "cat", "validation"], "abdecfghijklmnopqrstuvwxyz") ➞ True
################################################