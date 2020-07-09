import os
import py_cui
from typing import List

from util.file import File
from music import SongFile

class LocalPlayerWindow:

    _colums:int = 5
    _rows:int = 7
    _file:File
    _song_files:List[SongFile]

    def __init__(self,root):

        self.root = root
        self.window=self.root.create_new_widget_set(self._rows,self._colums)
        self._file=File()

        #Added widgets
        self.status_bar=self.root.status_bar
        self.song_info=self.window.add_block_label("Sample",0,2,row_span=2,column_span=3,center=False)
        self.song_list=self.window.add_scroll_menu("Songs list",3,2,row_span=3,column_span=3)
        self.settings=self.window.add_scroll_menu("Settings",3,0,row_span=3,column_span=2)

        self.__load_songs()
        self.__config()

    def _on_change_path(self,new_path:str):
        self._file.set_file_path(new_path)
        self.__load_songs()

    def _show_popup_file_path(self):
        self.root.show_text_box_popup("Write the path:",self.__validate_path)

    def __validate_path(self,path:str) -> None:
        if os.path.exists(path):
            self._on_change_path(path)
        else:
            self._show_popup_file_path()

    def __load_songs(self):
        #FIXME: When is selected a path without must clear the song_list
        self._song_files=self._file.get_music_list()

        songs_name_list=[song.get_name() for song in self._song_files]
        
        self.song_list.add_item_list(songs_name_list)

    def __config(self):
        self.status_bar.set_color(py_cui.BLACK_ON_WHITE)
        self.song_info.set_color(py_cui.BLACK_ON_WHITE)
        # self.song_list.set_color(py_cui.BLACK_ON_WHITE)

        self.window.add_key_command(py_cui.keys.KEY_S_LOWER,self._show_popup_file_path)

        self.root.set_title("Local Music Player")

    def create(self):
        return self.window
