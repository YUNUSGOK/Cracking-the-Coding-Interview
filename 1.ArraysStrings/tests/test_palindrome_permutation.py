import unittest
import palindromePermutation

class PalindromePermutationTest(unittest.TestCase):
    
    def test_empty(self):
        self.assertTrue(palindromePermutation.hashTableSolution(""))
        
    def test_all_space(self):
        self.assertTrue(palindromePermutation.hashTableSolution("     "))

    def test_true_input(self):
        self.assertTrue(palindromePermutation.hashTableSolution("aaavv"))
    
    def test_false_input(self):
        self.assertFalse(palindromePermutation.hashTableSolution("aaavvv"))
    
    def test_false_input_with_space(self):
        self.assertFalse(palindromePermutation.hashTableSolution("aaa    vvv"))
    
    def test_true_input_with_space(self):
        self.assertTrue(palindromePermutation.hashTableSolution("asd    asd"))
    
    def test_true_non_letters(self):
        self.assertTrue(palindromePermutation.hashTableSolution(".,:;;;;<>"))

    def test_false_input_with_nonletter(self):
        self.assertFalse(palindromePermutation.hashTableSolution("klme...,,"))

    def test_true_input_with_numeric(self):
        self.assertTrue(palindromePermutation.hashTableSolution("21654978"))

    def test_false_input_with_numeric(self):
        self.assertFalse(palindromePermutation.hashTableSolution("21654asd978"))