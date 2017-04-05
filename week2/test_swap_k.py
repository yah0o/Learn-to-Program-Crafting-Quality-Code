import a1
from a1 import swap_k
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    # Add your test methods for a1.swap_k here.
    def test_swap_k_empty(self):
        '''Test with an empty list.'''
        actual = []
        swap_k(actual, 0)
        expected = []
        self.assertEqual(actual, expected)

    def test_swap_k_single_int(self):
        '''Test with a list of len 1. type int'''
        actual = ['7']
        swap_k(actual, 0)
        expected = ['7']
        self.assertEqual(actual, expected)
        
    def test_swap_k_single_str(self):
        '''Test with a list of len 1. type str'''
        actual = ['s']
        swap_k(actual, 0)
        expected = ['s']
        self.assertEqual(actual, expected)

    def test_swap_k_0(self):
        '''Test with k=0.'''
        actual = [1, 2, 3, 4, 5]
        swap_k(actual, 0)
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(actual, expected)

    def test_swap_k_1(self):
        '''Test with k=1.'''
        actual = [1, 2, 3, 4, 5]
        swap_k(actual, 1)
        expected = [5, 2, 3, 4, 1]
        self.assertEqual(actual, expected)

    def test_swap_k_half_odd(self):
        '''Test with k=len(L)//2, list w/ odd length'''
        actual = [111, 222, 333, 444, 555]
        swap_k(actual, 2)
        expected = [444, 555, 333, 111, 222]
        self.assertEqual(actual, expected)

    def test_swap_k_half_even(self):
        '''Test with an even-length list, k=len(L)//2, using str.'''
        actual = ['a', 'b', 'c', 'd', 'e', 'f']
        swap_k(actual, 3)
        expected = ['d', 'e', 'f', 'a', 'b', 'c']
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(exit=False)
