import unittest
import checkPermutation


class checkPalindromeTest(unittest.TestCase):

    def test_two_empty(self):
        self.assertTrue(checkPermutation.hashTableSolution("",""))

    def test_one_empty(self):
        self.assertFalse(checkPermutation.hashTableSolution("bmntof", ""))
        self.assertFalse(checkPermutation.hashTableSolution("", "asdhfghert"))

    def test_identical(self):
        self.assertTrue(checkPermutation.hashTableSolution(
            "Lorem ipsum dolor sit amet.", 
            "Lorem ipsum dolor sit amet."))

    def test_different(self):
        self.assertFalse(checkPermutation.hashTableSolution(
            "Lorem ipsum dolor sit amet.", 
            "Curabitur posuere tempor dui, sed."))

    def test_same_letters_different_lenght(self):
        self.assertFalse(checkPermutation.hashTableSolution(
            "aaaaaaaaaaa", 
            "aaaaaaaaaaaa"))

    def test_same_letters_same_lenght(self):
        self.assertTrue(checkPermutation.hashTableSolution(
            "aaaaaaaaaaa", 
            "aaaaaaaaaaa"))
