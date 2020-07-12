import unittest

from pymusicterm.util.system import get_user_name
from pymusicterm.util.file import File

class TestFile(unittest.TestCase):

    def setUp(self):
        self.username=get_user_name()
        self.win_path='C:\\Users\\{}\Music'.format(self.username)
        self.wsl_path='/mnt/Users/{}/Music'.format(self.username)
        self.linux_path='/home/{}/Music'.format(self.username)

    def test_set_file_path(self):
        file_class=File()
        file_class.set_file_path(self.win_path)
        self.assertEqual(file_class.get_file_path(),self.win_path)
        self.assertNotEqual(file_class.get_file_path(),self.wsl_path)
        self.assertNotEqual(file_class.get_file_path(),self.linux_path)

        file_class.set_file_path(self.wsl_path)
        self.assertEqual(file_class.get_file_path(),self.wsl_path)
        self.assertNotEqual(file_class.get_file_path(),self.win_path)
        self.assertNotEqual(file_class.get_file_path(),self.linux_path)

        file_class.set_file_path(self.linux_path)
        self.assertEqual(file_class.get_file_path(),self.linux_path)
        self.assertNotEqual(file_class.get_file_path(),self.win_path)
        self.assertNotEqual(file_class.get_file_path(),self.wsl_path)
        del(file_class)

    def tearDown(self):
        del(self.username)
        del(self.win_path)
        del(self.wsl_path)
        del(self.linux_path)

if __name__ == "__main__":
    unittest.main()
