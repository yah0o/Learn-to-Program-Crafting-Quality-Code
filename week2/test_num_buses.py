import a1
from a1 import num_buses
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

    # Add your test methods for a1.num_buses here.
    def test_bus_capacity_null(self):
        '''Test amount of buses with 0 people'''
        actual = num_buses(0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_bus_capacity_1(self):
        '''Test amount of buses for 1 bus capacity'''
        actual = num_buses(49)
        expected = 1
        self.assertEqual(actual, expected)

    def test_bus_capacity_full(self):
        '''Test amount of buses with full capacity (boundary)'''
        actual = num_buses(50)
        expected = 1
        self.assertEqual(actual, expected)

    def test_bus_capacity_more(self):
        '''Test amount of buses with 2 bus capacity'''
        actual = num_buses(51)
        expected = 2
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(exit=False)
