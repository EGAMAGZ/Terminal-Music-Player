import os
from typing import List

from pymusicterm.music import SongFile,is_valid_extension
from pymusicterm.util.system import on_wsl,get_platform_name,get_user_name

class File:
    """ Class resposible to get the list of SongFile dataclasses for the LocalPlayerWindow

    This class contains functions that are use to search for song files with valid extensions
    and with them generate lists of SongFile dataclasses that will be used in the window of the
    local music player, and to change the path to search those files
    """

    _file_path:str
    _platform_name:str
    _user_name:str

    def __init__(self):
        self._platform_name=get_platform_name() # Gets platform name
        self._user_name=get_user_name() # Gets username
        self._file_path=self.__get_default_path() # By default will get the default path of each platform

    def set_file_path(self,file_path:str):
        """ Sets file path to load songs

        Parameters
        ----------
        file_path : str
            File path where song files will be searched
        """
        self._file_path=file_path

    def get_file_path(self) -> str:
        """ Get the actual file path

        Returns
        -------
        file_path : str
            Actual file path
        """
        return self._file_path

    def __get_default_path(self) -> str:
        """ Gets the default music path depending of the platform the program is runned

        Returns
        -------
        file_path : str
            Default music path
        """
        if not on_wsl():
            # If the user is not in wsl
            if self._platform_name == "linux":
                file_path="/home/{}/Music/".format(self._user_name)
            elif self._platform_name == "windows":
                file_path="C:\\Users\\{}\\Music".format(self._user_name)
        else:
            file_path="/mnt/c/Users/{}/Music".format(self._user_name)

        return file_path

    def _get_songs_file(self) -> List[str]:
        """ Funtion that return a list of song files that have a valid extension

        Returns
        -------
        songs_list : List[str]
            List of valid song files
        """
        songs_list=[] #List of song files
        files_list=os.listdir(self._file_path) # List of all files found in the file path
        for file_name in files_list:
            if is_valid_extension(file_name): # Check if is a valid extension
                songs_list.append(file_name)
        
        return songs_list

    def get_music_list(self) -> List[SongFile]:
        """ Function that returns a list of SongFile dataclasses

        Returns
        -------
        song_files_list : List[SongFile]
            List of dataclasses with information of the song file
        """
        songs_file_list:List[SongFile] = []
        songs_list=self._get_songs_file()

        for song in songs_list:
            # Will add SongFile dataclasses to song_files_list
            songs_file_list.append(SongFile(self._file_path,song))

        return songs_file_list
