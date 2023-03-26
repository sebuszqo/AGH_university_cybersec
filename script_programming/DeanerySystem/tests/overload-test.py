import unittest
from day import Day
from term import Term

# tests to test implemented overloading functions and operators 
# python3 -m unittest tests.overload-test

class Test_DSystem(unittest.TestCase):
    def setUp(self):
        global term1, term2, term3, term4
        term1 = Term(Day.MON, 8, 30)
        term2 = Term(Day.TUE, 9, 45, 30)
        term3 = Term(Day.TUE, 9, 45, 90)
        term4 = term3 - term1

    def test_overloading1(self):
        self.assertEqual(term1 < term2, True)

    def test_overloading2(self):
        self.assertEqual(term1 <= term2, True)

    def test_overloading3(self):
        self.assertEqual(term1 > term2, False)

    def test_overloading4(self):
        self.assertEqual(term1 >= term2, False)

    def test_overloading5(self):
        self.assertEqual(term2 == term2, True)

    def test_overloading6(self):
        self.assertEqual(term2 == term3, False)

    def test_sub(self):
        self.assertEqual(term4.__str__(),"Poniedziałek 8:30 [1605]")
        
if '__name__' == '__main__':
    unittest.main()