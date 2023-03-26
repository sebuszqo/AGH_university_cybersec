import unittest
from day import Day
from term import Term
from lesson import Lesson
from timeTableWithoutBreaks import TimetableWithoutBreaks

# tests to test apropriate implementation of lesson methods like: ealierDay, laterDay, ealierTime, laterTime
# python3 -m unittest tests.lesson-tests 

class Test_DSystem(unittest.TestCase):
    def setUp(self):
        global lesson1, lesson2, lesson3, lesson4
        global table
        global act
        table = TimetableWithoutBreaks()
        actions = ["t+", "d-", "t+", "d-"]
        act = table.parse(actions)
        lesson1 = Lesson(table, Term(Day.TUE, 9, 40), "Kryptografia", "Krzyszot Rzecki", 2)
        lesson2 = Lesson(table, Term(Day.SUN, 19, 40), "Programowanie skryptowe", "Stanisław Polak", 2)
        lesson3 = Lesson(table, Term(Day.FRI, 17, 40), "Systemy operacyjne", "Paweł Topa", 2)
        lesson4 = Lesson(table, Term(Day.FRI, 13, 40), "Wstęp do informatyki", "Michaił Drugi", 2)
        table.put(lesson1)
        table.put(lesson2)
        
        # print(table._lessons)
      
    def test_ealierDay(self):
        self.assertEqual(lesson1.ealierDay(), True)
        self.assertEqual(lesson2.ealierDay(), True)
        self.assertEqual(lesson3.ealierDay(), False)
        self.assertEqual(lesson4.ealierDay(), True)

    def test_laterDay(self):
        self.assertEqual(lesson1.laterDay(), True)
        self.assertEqual(lesson2.laterDay(), False)
        self.assertEqual(lesson3.laterDay(), True)
        self.assertEqual(lesson4.laterDay(), False)

    def test_printing1(self):
        self.assertEqual(lesson3.__str__(), f'{"-"*50}\nSystemy operacyjne (Piątek 17:40 [90]) \n2 rok studiów niestacjonarnych \nProwadzący: Paweł Topa\n{"-"*50}')
        self.assertEqual(lesson2.__str__(), f'{"-"*50}\nProgramowanie skryptowe (Niedziela 19:40 [90]) \n2 rok studiów niestacjonarnych \nProwadzący: Stanisław Polak\n{"-"*50}')

    def test_ealierTime(self):
        self.assertEqual(lesson1.ealierTime(), True)
        self.assertEqual(lesson2.ealierTime(), True)
        self.assertEqual(lesson3.ealierTime(), False)
        self.assertEqual(lesson4.ealierTime(), True)

    def test_laterTime(self):
        self.assertEqual(lesson1.laterTime(), True)
        self.assertEqual(lesson2.laterTime(), False)
        self.assertEqual(lesson3.laterTime(), True)
        self.assertEqual(lesson4.laterTime(), True)
    
    def test_act(self):
        global actions
        actions = ["t+", "t-", "t+", "d-", "kods-"]
        with self.assertRaises(ValueError):
            table.parse(actions)
    
    def test_arr(self):
        self.assertEqual(table.perform(act), None)

if '__name__' == '__main__':
    unittest.main()