import unittest
from languages import *

class LanguagesTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_get_counter_for_language_with_java_param_should_return_java_counter(self):
        ret = get_counter_for_language("java")
        self.assertIsInstance(ret, Java)

    def test_get_counter_for_language_with_unknown_param_should_raise_exception(self):
        with self.assertRaises(ValueError):
        	get_counter_for_language("UnknownLanguage")
        