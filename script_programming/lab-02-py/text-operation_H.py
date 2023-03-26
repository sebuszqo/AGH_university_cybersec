#-*-coding: utf-8-*-

#1.2
lancuch1 = '''
Jaka wielka jest Warszawa!
Ile domów, ile ludzi!
Ile dumy i radości
W sercach nam stolica budzi!
'''

lancuch2 = " Ja tylko jestem kamieniem \n \
I jako niemowlę tu, \n \
Objęty matki ramieniem, \n \
Cichego używam snu. \n \
"
 
# 1.3
print('\nZADANIE: 3')
print((lancuch1 + lancuch2)*3)

# 1.4
lancuch = "zażółć gęślą jaźń"

# 5.1{1-6}
# 1.pierwszy znak łańcucha
# 2. dwa pierwsze znaki
# 3. wszystkie znaki, za wyjątkiem dwóch pierwszych znaków
# 4. przedostatni znak łańcucha
# 5. trzy ostatnie znaki
# 6. wszystkie znaki na pozycjach parzystych

print('\nZADANIE: 5')
# 1.5.1
print(lancuch[0])
# 1.5.2
print(lancuch[0:2])
# 1.5.3
print(lancuch[2:])
# 1.5.4
print(lancuch[-2])
# 1.5.5
print(lancuch[-3:])
# 1.5.6
print(lancuch[::2])

# 1.6
# lancuch[1] = "ó"
# print(lancuch)
# Nie mogą być modyfikowane --> TypeError





# if __name__ == '__main__':
