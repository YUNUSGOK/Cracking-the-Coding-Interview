import stringCompression
import unittest

class StringCompressionTest(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(stringCompression.onePassSolution(""),"")

    def test_same_letters(self):
        self.assertEqual(stringCompression.onePassSolution("aaaa"),"a4")

    def test_no_compression(self):
        self.assertEqual(stringCompression.onePassSolution("abcavse"),"abcavse")

    def test_valid_input(self):
        self.assertEqual(stringCompression.onePassSolution("aaabbccca"),"a3b2c3a1")
        self.assertEqual(stringCompression.onePassSolution("aabcccccaaa"),"a2b1c5a3")

    


        


