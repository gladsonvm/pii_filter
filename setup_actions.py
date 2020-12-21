import os
from config_vars import compressed_files_dir


def setup_compressed_files_dir():
	"""
	This function creates a directory named todecode as per use case if it does not exist.
	Else will delete all files in todecode
	"""
	created = False
	if os.path.isdir(compressed_files_dir):
		files_in_todecode = os.listdir(compressed_files_dir)
		if files_in_todecode:
			for file_name in files_in_todecode:
				os.remove(compressed_files_dir+'/'+file_name)
	else:
		os.mkdir(compressed_files_dir)
		created = True
	return {compressed_files_dir: created}
