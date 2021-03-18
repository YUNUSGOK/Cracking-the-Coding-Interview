import unittest
import rotateMatrix
class RotateMatrixTest(unittest.TestCase):

    def test_empty(self):
        m = []
        rotateMatrix.layered(m)
        self.assertEqual(m,[])

    def test_single_element(self):
        m = [1]
        rotateMatrix.layered(m)
        self.assertEqual(m,[1])


    def test_two_by_two(self):
        m = [[1,2],[3,4]]
        rotateMatrix.layered(m)
        self.assertEqual(m,[[3,1],[4,2]])

    def test_three_by_three(self):
        m = [[1,2,3],[4,5,6],[7,8,9]]
        rotateMatrix.layered(m)
        self.assertEqual(m,[[7,4,1],[8,5,2],[9,6,3]])

    def test_same_elemets(self):
        m = [[1,1],[1,1]]
        rotateMatrix.layered(m)
        self.assertEqual(m,[[1,1],[1,1]])

    def test_no_square_matrix(self):
        m = [[3,2,1],[5,7]]
        rotateMatrix.layered(m)
        self.assertEqual(m,[[3,2,1],[5,7]])
