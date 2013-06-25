""" This file defines the programming languages supported by package-items,
and handles the module counting for each of them.
"""

def get_counter_for_language(language):
	"""Returns the appropriated counter for a given language"""
	
	if(language != "java"): 
		raise ValueError("Unknown language name informed: {:s}".format(language))

	return Java()


class Java(object):
	"""Responsible for counting modules on Java projects"""
	pass
