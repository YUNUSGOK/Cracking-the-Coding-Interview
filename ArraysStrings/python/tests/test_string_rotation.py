import unittest
from stringRotation import stringRotation




class StringRotationTest(unittest.TestCase):

    def test_empty(self):
        self.assertFalse(stringRotation("",""))

    def test_one_empty(self):
        self.assertFalse(stringRotation("waterbottle",""))
        self.assertFalse(stringRotation("","waterbottle"))
    
    def test_identical(self):
        self.assertTrue(stringRotation("waterbottle","waterbottle"))

    def test_rotated(self):
        self.assertTrue(stringRotation("waterbottle","erbottlewat"))
        self.assertTrue(stringRotation("Lorem ipsum dolor sit amet."," amet.Lorem ipsum dolor sit"))

    def test_one_char(self):
        self.assertTrue(stringRotation("aaaaaaaaaaa","aaaaaaaaaaa"))

    def test_different_size(self):
        self.assertFalse(stringRotation("waterbottle","waterbottl"))



