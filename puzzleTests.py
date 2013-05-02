from puzzle import *
import unittest

class TestAnagramIndex(unittest.TestCase):

    def test_AA(self):
	    self.assertEquals(anagramIndex("AA"),1)

    def test_BA(self):
        self.assertEquals(anagramIndex("BA"), 2)

    def test_ABAB(self):
        self.assertEquals(anagramIndex("ABAB"), 2)

    def test_BAB(self):
        self.assertEquals(anagramIndex("BAB"), 2)


class TestPerms(unittest.TestCase):
    def test_BAB(self):
        self.assertEquals(perms("BAB"), 3)

    def test_BAB(self):
        self.assertEquals(perms("AB"), 2)

if __name__ == '__main__':
    unittest.main()