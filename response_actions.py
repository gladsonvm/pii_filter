import os
import time
import datetime
import zipfile
import pyminizip
from pii_regex import pii_regex_list
from config_vars import date_stamp_format, watch_dir, text_file_extension, interval, compressed_files_dir


def compress_files(diff):
	"""
	Given an iterable of files, this method compress all files in the iterable.
	diff is the set of files
	"""
	compressed_files = []
	for item in diff:
		ctime = os.stat(item)[-1]
		zip_filename = time.strftime('%Y_%m_%d_%H_%M_%S_%p', time.localtime(ctime)) + '.zip'
		pyminizip.compress(watch_dir + '/' + item, None, compressed_files_dir + "/" + zip_filename, str(ctime), int(1))
		compressed_files.append(zip_filename)
	return compressed_files


def extract_all(diff, path=compressed_files_dir):
	"""
	extract all files in diff to path specified in variable path
	param diff: a set of files
	param path: location where files should be extracted
	"""
	files_in_all_zips = []
	for entry in diff:
		password = str(datetime.datetime.strptime(entry.split('.')[0], date_stamp_format).timestamp()).split('.')[0]
		zip_handle = zipfile.ZipFile(compressed_files_dir+'/'+entry)
		files_in_all_zips += [compressed_files_dir+'/'+file_name for file_name in zip_handle.namelist()]
		zip_handle.extractall(path=path, pwd=password.encode())
	return files_in_all_zips


def replace_pii_in_files(file_list, regex_list=pii_regex_list):
	"""
	replace all pii information in all files in file_list
	param file_list: list of files
	param regex_list: list of compiled regexes to identify pii information
	"""
	pii_filtered_files = []
	for filename in file_list:
		file_handle = open(filename,'r')
		file_contents = file_handle.read()
		original_file_size = file_handle.tell()
		file_handle.close()
		for pii_regex in regex_list:
			file_contents = pii_regex.sub('[masked]', file_contents).strip()
		file_handle = open(filename, 'w')
		file_handle.write(file_contents)
		if original_file_size != file_handle.tell():
			pii_filtered_files.append(filename)
		file_handle.close()
	return pii_filtered_files
