import os
import unittest

from pymusicterm.music import SongFile

def join_path(path,file_name) -> str:
    return os.path.join(path,file_name)

class TestSongFile(unittest.TestCase):
    
    def setUp(self):
        self.path='C:\\Users\\MyName\Music'
        self.file_name='song.mp3'
        self.song_file=SongFile(self.path,self.file_name)

    def test_get_name(self):
        self.assertEqual(self.song_file.get_name(),'song')

    def test_get_file_path(self):
        self.assertEqual(self.song_file.get_file_path(),join_path(self.path,self.file_name))

    def test_get_path(self):
        self.assertEqual(self.song_file.get_path(),self.path)

if __name__ == "__main__":
    unittest.main()
