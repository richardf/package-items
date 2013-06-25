""" This file defines the programming languages supported by package-items,
and handles the module counting for each of them.
"""

import os


def get_counter_for_language(language):
	"""Returns the appropriated counter for a given language"""

	if(language != "java"): 
		raise ValueError("Unknown language name informed: {:s}".format(language))

	return Java()


class Java(object):
	"""Responsible for counting modules on Java projects"""
	
	FILE_EXTENSIONS = (".java",)

	def count(self, base_path):
		return len(self._get_files(base_path))


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
