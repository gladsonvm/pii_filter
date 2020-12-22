import time
from config_vars import watch_dir, compressed_files_dir, zip_file_extension
import unittest
from unittest import mock
from response_actions import compress_files, extract_all


class TestResponseActions(unittest.TestCase):

    diff = {'a.txt', 'b.txt', 'c.txt'}
    ctimes = [(1608535356,), (1608535356,), (1608535356,)]
    zipped_files = ['2020_12_21_12_52_36_PM.zip', '2020_12_21_12_52_36_PM.zip', '2020_12_21_12_52_36_PM.zip']

    @mock.patch('response_actions.os.stat', side_effect=ctimes)
    @mock.patch('response_actions.pyminizip')
    def test_compress_files(self, pyminizip_mock, os_stat_mock):
        print('{}'.format(self._testMethodName))
        result = compress_files(TestResponseActions.diff)
        os_stat_calls = [mock.call(watch_dir+'/'+fname) for fname in TestResponseActions.diff]
        os_stat_mock.assert_has_calls(os_stat_calls)
        zipped_files = [time.strftime('%Y_%m_%d_%H_%M_%S_%p',
                        time.localtime(ctime[0])) + '.' + zip_file_extension
                        for ctime in TestResponseActions.ctimes]
        assert pyminizip_mock.compress.call_count == len(TestResponseActions.diff)
        assert result == zipped_files

    @mock.patch('response_actions.zipfile')
    def test_extract_all(self, zipmock):
        print('{}'.format(self._testMethodName))
        result = extract_all(TestResponseActions.zipped_files)
        assert len(result) == len(TestResponseActions.diff)
        assert zipmock.ZipFile.call_count == len(TestResponseActions.diff)

