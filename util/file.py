import os
import music
from typing import List
from music import SongFile

from .system import on_wsl,get_platform_name,get_user_name

class File:

    _file_path:str
    _platform_name:str
    _user_name:str

    def __init__(self):
        self._platform_name=get_platform_name()
        self._user_name=get_user_name()
        self._file_path=self.__get_default_path()

    def set_file_path(self,file_path:str):
        self._file_path=file_path

    def get_file_path(self,file_path=None) -> str:
        return self._file_path

    def __get_default_path(self) -> str:
        if not on_wsl():
            if self._platform_name == "linux":
                file_path="/home/{}/Music/".format(self._user_name)
            elif self._platform_name == "windows":
                file_path="C:\\Users\\{}\\Music".format(self._user_name)
        else:
            file_path="/mnt/c/Users/{}/Music".format(self._user_name)

        return file_path

    def _get_songs_file(self) -> List[str]:
        songs_list=[]
        files_list=os.listdir(self._file_path)
        for file_name in files_list:
            if file_name.endswith(music.MUSIC_EXTENSIONS):
                songs_list.append(file_name)
        
        return songs_list

    def get_music_list(self) -> List[SongFile]:
        songs_file_list=[]
        songs_list=self._get_songs_file()

        for song in songs_list:
            songs_file_list.append(SongFile(self._file_path,song))
        
        return songs_file_list
