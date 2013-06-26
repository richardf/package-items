""" This file defines the programming languages supported by package-items,
and handles the module counting for each of them.
"""

import os
import re

def get_counter_for_language(language):
	"""Returns the appropriated counter for a given language"""

	if(language != "java"): 
		raise ValueError("Unknown language name informed: {:s}".format(language))

	return Java()


class Java(object):
	"""Responsible for counting modules on Java projects"""
	
	FILE_EXTENSIONS = (".java",)
	DEFAULT_PACKAGE = "DEFAULT"

	def __init__(self):
		self.package_stats = {}
		self.regexp = re.compile(r"package[\s](?P<package_name>[a-zA-Z0-9._]+)[;]")


	def count(self, base_path):
		return len(self._get_files(base_path))


	def get_packages_size(self, base_path):
		filenames = self._get_files(base_path)

		for filename in filenames:
			data = self._read_file(filename)
			self._process_data(data)

		return package_stats


	def _read_file(self, path):
		"""Read a file, returning a list with its contents"""

		input_file = open(path, 'r')
		data = list(input_file)
		input_file.close()
		return data


	def _process_data(self, data):
		str_data = data.join(' ')


	def _get_package_name(self, data):
		"""Returns a package name for a given file (data) using a regexp. 
		If none is found, returns DEFAULT_PACKAGE"""

		result = self.regexp.search(data)
		if result == None:
			return self.DEFAULT_PACKAGE
		else:
			return result.group('package_name')


	def _get_files(self, base_path):
		"""Returns a list of filenames (with path) that contains one of FILE_EXTENSIONS"""

		return_files = []
		for root, dirs, files in os.walk(base_path, followlinks=False):
			selected_files = \
				[filename for filename in files if self._should_count(filename)]

			files_with_path = \
				[os.path.join(root, filename) for filename in selected_files]

			return_files += files_with_path

		return return_files


	def _should_count(self, filename):
		"""Tells if the current file should be counted based on FILE_EXTENSIONS"""

		return filename.lower().endswith(self.FILE_EXTENSIONS)
