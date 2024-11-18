import unittest
import group

class TestCases(unittest.TestCase):
    pass

    def test_groups_of_3(self):
        input = [1,2,3,4,5,6,7]
        result = group.groups_of_3(input)
        expected = [[1,2,3],[4,5,6],[7]]
        self.assertEqual(expected,result)

    def test_groups_of_3(self):
        input = [1, 2]
        result = group.groups_of_3(input)
        expected = [[1, 2]]
        self.assertEqual(expected, result)
