import unittest
import URLify

class URLifyTest(unittest.TestCase):
    
    def test_empty(self):
        self.assertEqual(URLify.inplaceShifting(""), "")

    def test_three_space(self):
        self.assertEqual(URLify.inplaceShifting("   "), "%20")


    def test_valid_input(self):
        self.assertEqual(
            URLify.inplaceShifting("Mr John Smith    "), "Mr%20John%20Smith")

    def test_cumulated_spaces(self):
        self.assertEqual(
            URLify.inplaceShifting("    MR        "), "%20%20%20%20MR")

    