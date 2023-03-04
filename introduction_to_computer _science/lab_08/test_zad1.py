import unittest
from unittest import result

class Test_zad_10(unittest.TestCase):
    def gen_tabs(self):
        result = [52, 95, 26, 13, 0, 46, 39, 27, 45, 87, 80, 77, 77, 93, 17, 0, 43, 0]
        self.assertEqual(result, [7, 45, 45, 34, 53, 45, 4, 3, 11, 18, 30])