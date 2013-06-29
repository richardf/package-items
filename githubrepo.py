from github import Github
import configparser

def main():
	username, password = get_github_credentials()


def get_github_credentials():
	"""Read GitHub credentials from config file"""
	
	config = get_credentials_file_contents()

	if not "username" in config['default'].keys():
		raise ValueError("Key username not found in credentials.txt")
	elif not "password" in config['default'].keys():
		raise ValueError("Key password not found in credentials.txt")

	return (config['default']['username'], config['default']['password'])


def get_credentials_file_contents():
	"""Get the contents from credentials.txt file and returns it in a dict"""

	try:
		file = open('credentials.txt')
		config = configparser.ConfigParser()
		config.read_file(add_section_header(file), source='credentials.txt')

	except FileNotFoundError:
		raise FileNotFoundError("Cannot find file credentials.txt."
			" Please create it with your GitHub credentials.")

	return config


def add_section_header(file):
	"""configparser requires at least one section header in properties file.
	This add a header to it on the fly"""

	yield '[default]\n'
	for line in file:
		yield line


if __name__ == '__main__':
	main()