from exceptions import SetupNotComplete
import threading
from config import config
from config_vars import watch_dir, compressed_files_dir, \
	text_file_extension, zip_file_extension
from config_vars import response_actions as ra 
from watcher import watchman
from setup_actions import setup_dir
from config_vars import directory


if __name__ == '__main__':
	"""
	Using threads since time.sleep in watchman is a blocking call
	"""
	# setup directory structure before starting threads
	watch_directory = setup_dir(watch_dir, True)
	compressed_files_directory = setup_dir(compressed_files_dir, True)
	if watch_directory == watch_dir and compressed_files_directory == compressed_files_dir:
		watch_dir_thread = threading.Thread(
			target=watchman, args=(watch_dir, text_file_extension, config[watch_dir][ra]))
		compressed_dir_thread = \
			threading.Thread(
				target=watchman, args=(compressed_files_dir, zip_file_extension, config[compressed_files_dir][ra]))

		watch_dir_thread.start()
		compressed_dir_thread.start()
	else:
		raise SetupNotComplete('watch dir and compressed_files_dir not setup')