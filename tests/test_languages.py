import unittest
import os
from languages import *


TEST_DIR = os.path.join(os.curdir, "tests")
PYTHON_DATA_DIR = os.path.join(TEST_DIR, "data/python")
JAVA_DATA_DIR = os.path.join(TEST_DIR, "data/java")

class LanguagesTestCase(unittest.TestCase):

    def test_get_counter_for_language_with_java_param_should_return_java_counter(self):
        ret = get_counter_for_language("java")
        self.assertIsInstance(ret, Java)

    def test_get_counter_for_language_with_unknown_param_should_raise_exception(self):
        with self.assertRaises(ValueError):
        	get_counter_for_language("UnknownLanguage")


class JavaLanguageTestCase(unittest.TestCase):
    def setUp(self):
        self.counter = Java()

    def test_java_get_package_name_with_valid_data_should_return_package_name(self):
    	data = "package a.test.package;"
    	self.assertEquals("a.test.package", self.counter._get_package_name(data))

    def test_java_get_package_name_with_valid_data_with_linebreaks_should_return_package_name(self):
    	data = "//comment\n int foo = 3; \npackage a.test.package;"
    	self.assertEquals("a.test.package", self.counter._get_package_name(data))

    def test_java_get_package_name_without_package_should_return_default_package(self):
    	data = "//comment\n int foo = 3; \na.test.package;"
    	self.assertEquals(self.counter.DEFAULT_PACKAGE, self.counter._get_package_name(data))

    def test_java_get_files_in_test_dir_should_return_list_with_1_element(self):
    	expected =[".\\tests\\data\\java\\javaclass.java"]
    	self.assertEquals(expected, self.counter._get_files(TEST_DIR))

    def test_java_get_files_in_python_dir_should_return_empty_list(self):
    	self.assertEquals([], self.counter._get_files(PYTHON_DATA_DIR))

    def test_java_should_count_with_py_should_return_false(self):
    	self.assertEquals(False, self.counter._should_count(".py"))

    def test_java_should_count_with_caps_py_should_return_false(self):
    	self.assertEquals(False, self.counter._should_count(".PY"))

    def test_java_should_count_with_java_should_return_true(self):
    	self.assertEquals(True, self.counter._should_count(".java"))

    def test_java_should_count_with_caps_java_should_return_true(self):
    	self.assertEquals(True, self.counter._should_count(".JAVA"))

    def test_java_count_in_python_dir_should_return_0(self):
    	self.assertEquals(0, self.counter.count(PYTHON_DATA_DIR))

    def test_java_count_in_test_dir_should_return_1(self):
   		self.assertEquals(1, self.counter.count(TEST_DIR))