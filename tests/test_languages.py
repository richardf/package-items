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

    def test_java_process_data_with_only_default_package_should_return_one_package(self):
        data = ["//no package", "class Foo() {}"]
        self.counter._process_data(data)
        self.assertEquals(1, len(self.counter.package_stats))
        self.assertEquals(1, self.counter.package_stats[self.counter.DEFAULT_PACKAGE])

    def test_java_process_data_twice_with_only_default_package_should_return_one_package(self):
        data = ["//no package", "class Foo() {}"]
        self.counter._process_data(data)
        self.counter._process_data(data)
        self.assertEquals(1, len(self.counter.package_stats))
        self.assertEquals(2, self.counter.package_stats[self.counter.DEFAULT_PACKAGE])

    def test_java_process_data_with_test_package_should_return_one_package(self):
        data = ["//comment" ,"package a.test.package;", "class Foo() {}"]
        self.counter._process_data(data)
        self.assertEquals(1, len(self.counter.package_stats))
        self.assertEquals(1, self.counter.package_stats['a.test.package'])

    def test_java_process_data_with_two_test_packages_should_return_two_packages(self):
        data = ["//comment" ,"package a.test.package;", "class Foo() {}"]
        another_data = ["package another.test;"]
        self.counter._process_data(data)
        self.counter._process_data(another_data)
        self.assertEquals(2, len(self.counter.package_stats))
        self.assertEquals(1, self.counter.package_stats['a.test.package'])
        self.assertEquals(1, self.counter.package_stats['another.test'])

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
        expected = [os.path.join('.', 'tests', 'data', 'java', 'javaclass.java')]
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

    def test_java_get_packages_size_in_python_dir_should_return_0_elements(self):
        self.assertEquals(0, len(self.counter.get_packages_size(PYTHON_DATA_DIR)))

    def test_java_get_packages_size_in_test_dir_should_return_1_element(self):
        ret = self.counter.get_packages_size(TEST_DIR)
        self.assertEquals(1, len(ret))
        self.assertEquals(1, ret['a.sample.testpackage'])

        
