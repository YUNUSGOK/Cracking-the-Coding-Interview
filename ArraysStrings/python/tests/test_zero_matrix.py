
import unittest
import zeroMatrix

class ZeroMatrixTest(unittest.TestCase):
    
    def test_empty(self):
        m = []
        zeroMatrix.onePass(m)
        self.assertEqual(m,[])

    def test_single_element_one(self):
        m = [1]
        zeroMatrix.onePass(m)
        self.assertEqual(m,[1])

    def test_single_element_zero(self):
        m = [0]
        zeroMatrix.onePass(m)
        self.assertEqual(m,[0])

    def test_two_by_two_no_zeros(self):
        m = [[1,2],[3,4]]
        zeroMatrix.onePass(m)
        self.assertEqual(m, [[1,2],[3,4]])

    def test_two_by_two_one_zero(self):
        m = [[1,0],[3,4]]
        zeroMatrix.onePass(m)
        self.assertEqual(m, [[0,0],[3,0]])

    def test_two_by_three_one_zero(self):
        m = [[1,0,2],[3,4,5]]
        zeroMatrix.onePass(m)
        self.assertEqual(m, [[0,0,0],[3,0,5]])

    def test_three_by_two_one_zero(self):
        m = [[1,2],[3,4],[7,0]]
        zeroMatrix.onePass(m)
        self.assertEqual(m, [[1,0],[3,0],[0,0]])

    def test_three_by_two_no_zero(self):
        m = [[1,2],[3,4],[7,5]]
        zeroMatrix.onePass(m)
        self.assertEqual(m, [[1,2],[3,4],[7,5]])

    def test_three_by_two_two_zero(self):
        m = [[1,2],[3,4],[0,0]]
        zeroMatrix.onePass(m)
        self.assertEqual(m, [[0,0],[0,0],[0,0]])






