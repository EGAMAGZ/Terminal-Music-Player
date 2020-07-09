import os
from dataclasses import dataclass

MUSIC_EXTENSIONS=(".mp3",".wav")

@dataclass
class SongFile:
    position:int
    path:str
    file_name:str

    def get_position(self):
        return self.position

    def get_name(self):
        pass

    def get_file_path(self):
        pass
