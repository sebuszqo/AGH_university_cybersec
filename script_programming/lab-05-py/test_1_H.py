# import unittest
# from dekoratory_H import Operacje


# class Test_Zad1(unittest.TestCase):
#     def setUp(self):
#         global op
#         op=Operacje()
        
#     def test_operation_sum(self):
#         self.assertEqual(op.suma(1,2,3), 4)
#         self.assertEqual(op.suma(1,2), 5)
#         self.assertEqual(op.suma(1), None)

#     def test_operation_error(self):
#         with self.assertRaises(TypeError):
#             op.suma()

#     def test_operation_roznica(self):
#         self.assertEqual(op.roznica(2,1), 4)
#         self.assertEqual(op.roznica(2), 5)
#         self.assertEqual(op.roznica(), 6)

#     def test_change_sum(self):
#         op['suma']=[1,2]
#         self.assertEqual(op.suma(1), None)
#         self.assertEqual(op.suma(1, 1), 5)
#         self.assertEqual(op.suma(1, 1, 1), 4)

#     def test_change_roznica(self):
#         op['roznica']=[1,2,3]
#         self.assertEqual(op.roznica(), 6)
#         self.assertEqual(op.roznica(1), 5)
#         self.assertEqual(op.roznica(1, 1), 4)

# if __name__ == "__main__":
#     unittest.main()

from dekoratory_H import Operacje
import unittest, sys, os

class Test_Operacje(unittest.TestCase):

    def setUp(self):
        global op
        op=Operacje()

    def test_suma_3arg(self):
        self.assertEqual(op.suma(1, 2, 3), 4)
        self.assertEqual(op.suma(1, 2), 5)
        self.assertEqual(op.suma(1), None)

    def test_suma_0arg(self):
        with self.assertRaises(TypeError):
            op.suma()
    
    def test_roznica_2arg(self):
        self.assertEqual(op.roznica(2, 1), 4)
        self.assertEqual(op.roznica(2), 5)
        self.assertEqual(op.roznica(), 6)
  
    def test_zmiana_suma(self):
        op['suma']=[1,2]
        self.assertEqual(op.argumentySuma, [1, 2])
        self.assertEqual(op.suma(1), None)
        self.assertEqual(op.suma(1, 1), 2)
        self.assertEqual(op.suma(1, 1, 1), 1)

    def test_zmiana_roznica(self):
        op['roznica']=[1, 2, 3]
        self.assertEqual(op.argumentyRoznica, [1, 2, 3])
        self.assertEqual(op.roznica(), 3)
        self.assertEqual(op.roznica(1), 2)
        self.assertEqual(op.roznica(1, 1), 1)


if __name__ == '__main__':
    sys.stdout = open(os.devnull, 'w')
    unittest.main()