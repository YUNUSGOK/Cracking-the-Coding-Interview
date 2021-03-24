import unittest
import isUnique

class IsUniqueTest(unittest.TestCase):
    
    def test_empty(self):
        isUnique.hashTableSolution("")
        self.assertTrue(isUnique.hashTableSolution(""))

    def test_all_spaces(self):
        self.assertFalse(isUnique.hashTableSolution("      "))

    def test_unique_true(self):
        self.assertTrue(isUnique.hashTableSolution("asdghj"))
    
    def test_unique_true_with_space(self):
        self.assertTrue(isUnique.hashTableSolution("asd nbv"))

    def test_unique_true_with_non_letters(self):
        self.assertTrue(isUnique.hashTableSolution("1235.,:"))

    def test_unique_false(self):
        self.assertFalse(isUnique.hashTableSolution("qweiqwelqwe"))
    
    def test_unique_false_with_space(self):
        self.assertFalse(isUnique.hashTableSolution("asd  nbv"))

    def test_unique_false_with_non_letters(self):
        self.assertFalse(isUnique.hashTableSolution("1235..,:"))
