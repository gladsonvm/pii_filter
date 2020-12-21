import os
from config_vars import directory


def setup_dir(directory, delete_files_if_exists):
	"""
	This function creates a directory named todecode as per use case if it does not exist.
	Else will delete all files in todecode
	"""
	if os.path.isdir(directory):
		files_in_dir = os.listdir(directory)
		if delete_files_if_exists:
			if files_in_dir:
				for file_name in files_in_dir:
					os.remove(directory+'/'+file_name)
	else:
		os.mkdir(directory)
	return directory
