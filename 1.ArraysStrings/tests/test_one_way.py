import unittest
import oneWay

class oneWayTest(unittest.TestCase):

    def test_two_empty(self):
        self.assertTrue(oneWay.onePassSolution(
                "",
                ""))

    def test_one_empty(self):
        self.assertFalse(oneWay.onePassSolution(
                "asdasd",
                ""))
    
        self.assertFalse(oneWay.onePassSolution(
                "",
                "asefgh"))  
    
    def test_examples(self):
        self.assertTrue(oneWay.onePassSolution(
            "pale", 
            "ple"))
        self.assertTrue(oneWay.onePassSolution(
            "pales", 
            "pale"))
        self.assertTrue(oneWay.onePassSolution(
            "pale", 
            "bale"))
        self.assertFalse(oneWay.onePassSolution(
            "pale", 
            "bake"))
    
    def test_different_lenght_false(self):
        self.assertFalse(oneWay.onePassSolution(
            "Lorem ipsum dolor sit amet.", 
            "Lorem ipsum dolor"))

    def test_different_lenght_true(self):
        self.assertTrue(oneWay.onePassSolution(
            "Lorem ipsum dolor sit amet.", 
            "Lorem ipsum olor sit amet."))

    def test_same_lenght_false(self):
        self.assertFalse(oneWay.onePassSolution(
            "Lorem ipsum dolor sit amet.", 
            "klxiz ipsum dolor sit amet."))

    def test_same_lenght_true(self):
        self.assertTrue(oneWay.onePassSolution(
            "Lorem ipsum dolor sit amet.", 
            "Lorem ipsum dolor sit amet."))
 
