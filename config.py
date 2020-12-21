from config_vars import watch_dir, compressed_files_dir
from response_actions import compress_files, extract_all, replace_pii_in_files
from setup_actions import setup_dir
from config_vars import response_actions as ra

config = {
	watch_dir: {
		'setup_action': {'fn_name': setup_dir, 'args': (watch_dir, True)},
		ra: [{'fn_name': compress_files, 'input_data': 'file_diff'}]},
	compressed_files_dir: {
		'setup_action': {'fn_name': setup_dir, 'args': (compressed_files_dir, True)},
		ra: [
			{'fn_name': extract_all, 'save_ret_val': True, 'input_data': 'file_diff'},
			{'fn_name': replace_pii_in_files, 'input_data': extract_all}
		]}
}
