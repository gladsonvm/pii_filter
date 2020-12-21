import threading
from config import config
from config_vars import watch_dir, compressed_files_dir, \
	text_file_extension, zip_file_extension
from config_vars import response_actions as ra 
from watcher import watchman


if __name__ == '__main__':
	"""
	Using threads since time.sleep in watchman is a blocking call
	"""
	watch_dir_thread = threading.Thread(
		target=watchman, args=(watch_dir, text_file_extension, config[watch_dir][ra]))
	compressed_dir_thread = \
		threading.Thread(
			target=watchman, args=(compressed_files_dir, zip_file_extension, config[compressed_files_dir][ra]))

	watch_dir_thread.start()
	compressed_dir_thread.start()
