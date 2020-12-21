import os
import time
from config_vars import interval


def watchman(watch_target, file_ext, response_actions, setup_action=None):
	"""
	watchman is a listener which listens to changes to all files of type file_ext in a given directory watch_target
	watch_dir man executed chain of response actions specified in response_actions when any changes are found
	param watch_target: directory to listen
	param file_ext: extension of files to watch_dir
	param response_actions: chain of response actions to execute on detection of change in watch_dir target
	"""

	original_files = \
		{item for item in os.listdir(watch_target) if os.path.isfile(watch_target+'/'+item) and
			item.split('.')[-1] == file_ext}
	print("watchman running for {watch_target}".format(watch_target=watch_target))
	while True:
		time.sleep(interval)
		modified_files = \
			{item for item in os.listdir(watch_target) if os.path.isfile(watch_target+'/'+item) and
				item.split('.')[-1] == file_ext}
		if (diff := modified_files - original_files):
			print('{count} new files detected in {folder}'.format(count=len(diff), folder=watch_target))
			ra_return_value_dict = {}
			for func_dict in response_actions:
				ret_val = None
				input_data = func_dict.get('input_data')
				if input_data == 'file_diff':
					ret_val = func_dict['fn_name'](diff)
				elif input_data:
					input_data = input_data.__name__
					ret_val = func_dict['fn_name'](ra_return_value_dict[input_data])
				elif input_data is None:
					ret_val = func_dict['fn_name']()
				if func_dict.get('save_ret_val'):
					ra_return_value_dict.update({func_dict['fn_name'].__name__: ret_val})
				original_files = modified_files
