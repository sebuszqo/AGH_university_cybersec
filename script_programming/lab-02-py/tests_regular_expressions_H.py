import regular_expressions_H
import unittest
#python3 -m unittest tests_regular_expressions_H.py

class RegTests(unittest.TestCase):
    def test_word_numer(self):
        for answer in regular_expressions_H.reg("Że nie wiem #2, gdzie się w mogiłę%122 położę"):
            self.assertIn(answer, ["Że", 122, 2, "nie", "wiem", "gdzie", "się", "w", "mogiłę", "położę" ])
    
    def test_only_word(self):
        for answer in regular_expressions_H.reg("c02c1448bc17d8b972c5"):
            self.assertIn(answer, ["c", "b", "d", "bc", 2, 1448, 17, 8, 972, 5])

    def test_only_nums(self):
        for answer in regular_expressions_H.reg("Jola lojalna ma 22 lata, Jola nielojalna ma #19"):
            self.assertIn(answer, ["Jola", "lojalna","ma", 22, 19, "lata", "nielojalna"])

    def test_combine_all(self):
        for answer in regular_expressions_H.reg("Kościuszki 4/52 Opole 30-403"):
            self.assertIn(answer, ["Kościuszki", 4, 52, "Opole", 30, -403])

if __name__ == '__main__':
    unittest.main()