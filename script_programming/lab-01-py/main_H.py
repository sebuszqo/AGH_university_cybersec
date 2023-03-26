
from fractions import Fraction
import main_H
# 1.
# def sum(arg1, arg2):
#     return arg1 + arg2

# 2.
def sum(arg1, arg2):
    if type(arg1) is complex or type(arg2) is complex:
        return complex(round(arg1.real + arg2.real, 10), round(arg1.imag + arg2. imag, 10)) # round bo python musi zaokraglic 
    
    if isinstance(arg1, Fraction) or isinstance(arg2, Fraction):  # problem z ulamkami zwyklymi niecalkowitymi czyli np 2/7
        return Fraction(arg1 + arg2)
    
    return float(arg1) + float(arg2)


# print(f'__name__ = {__name__}')
# __name__ = main --> przy import main

# 9
if __name__ == "__main__":
    print(f'suma = {sum(2,3)}')
    print(f'__name__ = {__name__}')

    
# typowanie silne i dynamiczne --> 2 + '2' = error

#  2 + 2  - 4 int
#  2 + 2.0 - 4.0 float
#  2 + '2' - TypeError: unsupported operand type(s) for +: 'int' and 'str'
#  
# zmienna = 2 
# type(zmienna) - <class 'int'>
# 
# zmienna = '2'
# type(zmienna) - <class 'str'>

