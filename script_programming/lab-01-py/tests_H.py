
import main_H
import unittest
from fractions import Fraction
# how to run:
# python3 -m unittest tests_H.py

class Test_TestSum(unittest.TestCase):
    def test_sum_integer_integer(self): # 2 int .
        self.assertEqual(main_H.sum(2, 2), 4)

    def test_sum_integer_float(self):   # int + float .
        self.assertEqual(main_H.sum(2, 1.5), 3.5)

    def test_sum_integer_string(self): # int + string . dopiero po zmianie string --> float
        self.assertEqual(main_H.sum(2, '2'), 4)

    def test_sum_string_string(self):   # string + string . dopiero po zmianie string --> float
        self.assertEqual(main_H.sum('2.1', '2.0'), 4.1)

    def test_sum_fraction_fraction(self):  # fraction + fraction . 
        self.assertEqual(main_H.sum(Fraction(2,7), Fraction(2,7)), Fraction(4,7))

    def test_sum_complex_int(self):  # complex + complex --> . po dodaniu if z complex ( rzeczywista, urojona)
        self.assertEqual(main_H.sum(complex(2.3, 3.7), complex(-0.3, -0.7)), complex(2,3))
    
    def test_sum_integer_wrong_number_in_string(self): # int + string --> . dopiero po asserRaises - ValueError
        with self.assertRaises(ValueError):
            self.assertEqual(main_H.sum(2,'Ala ma kota'), 2)
    
    def test_sum_integer_list(self): # int + array --> . dopiero po asserRaises - TypeError
        with self.assertRaises(TypeError):
            self.assertEqual(main_H.sum(1, [2, 3]), 1)

    
   

if '__name__' == '__main__':
    unittest.main()