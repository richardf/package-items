import unittest
from packageitems import *


class PackageItemsTestCase(unittest.TestCase):

    def test_calculate_average_with_empty_argument_should_raise_exception(self):
        dic = {}
        with self.assertRaises(ValueError):
        	calculate_average(dic)

    def test_calculate_average_with_valid_argument_should_return_1(self):
        dic = {'one.package' : 1}
       	result = calculate_average(dic)
       	self.assertEquals(1, result)

    def test_calculate_average_with_valid_argument_should_return_4_5(self):
        dic = {'one.package' : 7, 'other.package' : 2}
       	result = calculate_average(dic)
       	self.assertEquals(4.5, result)