import a1
from a1 import stock_price_summary
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    # Add your test methods for a1.stock_price_summary here.
    def test_stock_price_summary_empty(self):
        '''Test with an empty list of price changes.'''
        actual = stock_price_summary([])
        expected = (0, 0)
        self.assertEqual(actual, expected)

    def test_stock_price_summary_one_positive(self):
        '''Test with a one single positive entry.'''
        actual = stock_price_summary([0.01])
        expected = (0.01, 0)
        self.assertEqual(actual, expected)

    def test_stock_price_summary_one_negative(self):
        '''Test with an a one single negative entry.'''
        actual = stock_price_summary([-0.01])
        expected = (0, -0.01)
        self.assertEqual(actual, expected)

    def test_stock_price_summary_several_positive(self):
        '''Test with several positive entries.'''
        actual = stock_price_summary([0.01, 0.02])
        expected = (0.03, 0)
        self.assertEqual(actual, expected)

    def test_stock_price_summary_several_negative(self):
        '''Test with several negative entries.'''
        actual = stock_price_summary([-0.01, -0.1, -0.11])
        expected = (0, -0.22)
        self.assertEqual(actual, expected)

    def test_stock_price_summary_mixed(self):
        '''Test with mixed list (positive, negative) of price changes.'''
        actual = stock_price_summary([0.01, 0.02, -0.01, -0.12, 0, 0, 0.17, -0.01, -0.02])
        expected = (0.2, -0.16)
        self.assertEqual(actual, expected)
        

if __name__ == '__main__':
    unittest.main(exit=False)
