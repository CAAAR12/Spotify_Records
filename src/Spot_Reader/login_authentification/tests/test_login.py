import unittest
from unittest.mock import patch
from .. import login

class TestLogin(unittest.TestCase):
    @patch('builtins.input')
    def test_variable(self,mock_value):
        test_Value = "caaar12"
        mock_value.return_value = test_Value
        result = login.login_uzer().current_user()['id']
        self.assertEqual(result, test_Value)

    @patch('builtins.input')
    def test_login_someone_else(self,mock_value):
        someone_elses_username = "alexiskbr"
        mock_value.return_value = someone_elses_username
        with self.assertRaises(TypeError):
            result = login.login_uzer().current_user()['id']


if __name__ == "__main__":
    unittest.main()