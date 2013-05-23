from puzzle import *
import unittest

class TestAnagramIndex(unittest.TestCase):

    def test_AA(self):
        self.assertEqual(anagramIndex("AA"),1)

    def test_BA(self):
        self.assertEqual(anagramIndex("BA"), 2)

    def test_ABAB(self):
        self.assertEqual(anagramIndex("ABAB"), 2)

    def test_BAB(self):
        self.assertEqual(anagramIndex("BAB"), 2)

    def test_QUESTION(self):
        self.assertEqual(anagramIndex("QUESTION"), 24572)

    def test_BOOKKEEPER(self):
        self.assertEqual(anagramIndex("BOOKKEEPER"), 10743)

class TestAlphabetic(unittest.TestCase):

    def test_AA(self):
        self.assertEqual(alphabetically_before_first_char("AA"), set())

    def test_ABAB(self):
        self.assertEqual(alphabetically_before_first_char("ABAB"), set())

    def test_BAB(self):
        self.assertEqual(alphabetically_before_first_char("BAB"), set(['A']))


class TestPerms(unittest.TestCase):
    def test_BAB(self):
        self.assertEqual(perms("BAB"), 3)

    def test_BAB(self):
        self.assertEqual(perms("AB"), 2)

    def test_ABAB(self):
        self.assertEqual(perms("ABAB"), 6)


class TestStartingWith(unittest.TestCase):
    def test_AA_A(self):
        self.assertEqual(num_anagrams_starting_with("AA", "A"), 1)

    def test_AB_A(self):
        self.assertEqual(num_anagrams_starting_with("AB", "A"), 1)

    def test_AB_B(self):
        self.assertEqual(num_anagrams_starting_with("AB", "B"), 1)

    def test_BAB_A(self):
        self.assertEqual(num_anagrams_starting_with("BAB", "A"), 1)

    def test_BAB_B(self):
        self.assertEqual(num_anagrams_starting_with("BAB", "B"), 2)

if __name__ == '__main__':
    unittest.main()
