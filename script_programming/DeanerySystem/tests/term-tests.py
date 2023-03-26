import unittest
from day import Day
from term import Term

#python3 -m unittest tests.term-tests

class Test_DSystem(unittest.TestCase):
    def setUp(self):
        global term1, term2, term3, term4
        term1 = Term(Day.TUE, 9, 45) #2
        term2 = Term(Day.WED, 11, 15, 30) #3
        term3 = Term(Day.TUE, 11, 15, 90) #2
        term4 = Term(Day.FRI, 17, 30, 110) #5

    def test_earlier(self):
        self.assertEqual(term1.earlierThan(term2), True)
        self.assertEqual(term2.earlierThan(term1), False)
        self.assertEqual(term4.earlierThan(term3), False)

    def test_later(self):
        self.assertEqual(term1.laterThan(term2), False)
        self.assertEqual(term2.laterThan(term1), True)
        self.assertEqual(term4.laterThan(term3), True)
        
    def test_equal(self):
        self.assertEqual(term1.equals(term2), False)
        self.assertEqual(term1.equals(term3), False)

if '__name__' == '__main__':
    unittest.main()