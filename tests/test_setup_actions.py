import unittest
from unittest import mock
from setup_actions import setup_dir
import sys

class TestSetup(unittest.TestCase):
    setup_dir_param = '/pwd'
    list_dir = ['a', 'b']

    @mock.patch('setup_actions.os')
    def test_setup_action_delete_if_exists(self, os_mock):
        """
        Scenario: Called setup_dir with delete_files_if_exists as True
        Specified directory exists
        """
        print('{}'.format(self._testMethodName))
        os_mock.path.isdir.return_value = True
        os_mock.listdir.return_value = TestSetup.list_dir
        return_value = setup_dir(TestSetup.setup_dir_param, False)
        assert os_mock.listdir.call_count == 1
        assert os_mock.remove.call_count == 0
        assert return_value == TestSetup.setup_dir_param

    @mock.patch('setup_actions.os')
    def test_setup_action_no_delete(self, os_mock):
        """
        Scenario: Called setup_dir with delete_files_if_exists as False
        Specified directory exists
        """
        print('{}'.format(self._testMethodName))
        os_mock.path.isdir.return_value = True
        os_mock.listdir.return_value = TestSetup.list_dir
        return_value = setup_dir(TestSetup.setup_dir_param, False)
        assert os_mock.listdir.call_count == 1
        assert os_mock.remove.call_count == 0
        assert return_value == TestSetup.setup_dir_param

    @mock.patch('setup_actions.os')
    def test_setup_action_directory_does_not_exist(self, os_mock):
        """
        Scenario: Called setup_dir with delete_files_if_exists as False
        Specified directory does not exist and needs to be created
        """
        print('{}'.format(self._testMethodName))
        os_mock.path.isdir.return_value = True
        os_mock.listdir.return_value = TestSetup.list_dir
        return_value = setup_dir(TestSetup.setup_dir_param, True)
        assert os_mock.listdir.call_count == 1
        assert os_mock.remove.call_count == len(TestSetup.list_dir)
        assert return_value == TestSetup.setup_dir_param


if __name__ == '__main__':
    unittest.main()
