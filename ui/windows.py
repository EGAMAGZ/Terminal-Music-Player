import os
import py_cui
from typing import List

from util.file import File
from music import SongFile
from music.player import MusicPlayer
from ui.labels import SongInfoBlockLabel

class LocalPlayerWindow(MusicPlayer):

    _colums:int = 5
    _rows:int = 7
    _file:File
    _songs_file:List[SongFile]

    def __init__(self,root):

        self.root = root
        self.window=self.root.create_new_widget_set(self._rows,self._colums)
        self._file=File()

        #Added widgets
        self.status_bar=self.root.status_bar
        self.song_info=SongInfoBlockLabel(self.window)
        self.song_list=self.window.add_scroll_menu("Songs list",3,2,row_span=3,column_span=3)
        self.settings=self.window.add_scroll_menu("Settings",3,0,row_span=3,column_span=2)
        self.song_queue=self.window.add_scroll_menu("Songs queue",0,0,row_span=3,column_span=2)

        self.__load_songs() #TODO: Modify this method to make it async
        self.__config()

        #Init of class MusicPlayer, that will initialiaze pygame.mixer
        super().__init__(self.song_queue)

    def _on_change_path(self,new_path:str):
        self._file.set_file_path(new_path)
        self.__load_songs()

    def _on_select_song(self):
        index=self.song_list.get_selected_item_index()
        song_file=self._songs_file[index]
        # self.song_info.set_song_info(song_file) FIXME: In next version py_cui will be fix
        self.add_song(song_file)

    def _show_popup_file_path(self):
        self.root.show_text_box_popup("Write the path:",self.__validate_path)

    def __validate_path(self,path:str) -> None:
        if os.path.exists(path):
            self._on_change_path(path)
        else:
            self._show_popup_file_path()

    def __load_songs(self):
        self._songs_file=self._file.get_music_list()
        if self._songs_file: #List is not Empty
            songs_name_list=[song.get_name() for song in self._songs_file]
            self.song_list.add_item_list(songs_name_list)
        else:   #List is empty
            self.song_list.clear()

    def __config(self):
        #TODO: Add a popup to confirm to quit when there is a song playing
        self.status_bar.set_color(py_cui.BLACK_ON_WHITE)

        self.window.add_key_command(py_cui.keys.KEY_S_LOWER,self._show_popup_file_path)
        self.song_list.add_key_command(py_cui.keys.KEY_ENTER,self._on_select_song)

        self.root.set_title("Local Music Player")

    def create(self):
        return self.window
