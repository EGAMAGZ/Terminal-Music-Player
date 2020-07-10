import os
from dataclasses import dataclass

MUSIC_EXTENSIONS=(".mp3",".wav")

@dataclass
class SongFile:

    path:str
    file_name:str

    def get_name(self) -> str:
        return os.path.splitext(self.file_name)[0]

    def get_file_path(self) -> str:
        return os.path.join(self.path,self.file_name)

    def get_path(self) -> str:
        return self.path
