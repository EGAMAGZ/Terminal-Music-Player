import os
import py_cui
from typing import List

from pymusicterm.util.file import File
from pymusicterm.music import SongFile
from pymusicterm.music.player import MusicPlayer
from pymusicterm.ui.labels import SongInfoBlockLabel

class LocalPlayerWindow(MusicPlayer):

    _colums:int = 5
    _rows:int = 7
    _file:File
    _songs_file:List[SongFile]

    def __init__(self,root):
        """ Constructor for LocalPlayerWindow
        """
        #Init of class MusicPlayer, that will initialiaze pygame.mixer
        super().__init__()

        self.root = root
        self.window=self.root.create_new_widget_set(self._rows,self._colums)
        self._file=File()

        #Added widgets
        self.status_bar=self.root.status_bar
        self.title_bar=self.root.title_bar

        #BlockLabels
        self.song_info=SongInfoBlockLabel(self.window)

        #Scroll Menus
        self.song_list=self.window.add_scroll_menu("Songs list",3,2,row_span=3,column_span=3)
        self.settings=self.window.add_scroll_menu("Settings",3,0,row_span=3,column_span=2)
        self.song_queue=self.window.add_scroll_menu("Songs queue",0,0,row_span=3,column_span=2)

        self.__load_songs() #TODO: Modify this method to make it async
        self.__config()

    def change_path(self,new_path:str):
        """ Changes file path to search songs
        """
        self._file.set_file_path(new_path)
        self.__load_songs()

    def add_song(self):
        """Override of base class function. Adds a new song to the queue
        """
        index=self.song_list.get_selected_item_index()
        song_file=self._songs_file[index]
        # self.song_info.set_song_info(song_file) FIXME: In next version py_cui will be fix
        if self.not_in_queue_songs(song_file):
            self.song_queue.add_item(song_file.get_name()) #Adds song to the scroll menu
            super().add_song(song_file) # Method of MusicPLayer class

    def play_song(self):
        """Override of base class function. Plays a song in queue songs
        """
        index=self.song_queue.get_selected_item_index()
        super().play_song(index) # Method of MusicPlayer class

    def pause_song(self):
        """ Override of base class function. Pauses the song playing and change
            the color of status bar and title bar
        """
        if self.is_playing():
            super().pause_song() # First it paused
            if self.paused: # Then check if is paused
                self.status_bar.set_color(py_cui.WHITE_ON_RED)
                self.title_bar.set_color(py_cui.WHITE_ON_RED)
            else:
                self.status_bar.set_color(py_cui.BLACK_ON_WHITE)
                self.title_bar.set_color(py_cui.BLACK_ON_WHITE)

    def remove_song(self):
        """ Override of base class function. Removes song from queue
        """
        index=self.song_queue.get_selected_item_index()
        self.song_queue.remove_selected_item()
        super().remove_song(index) # Method of MusicPlayer class

    def previous_song(self):
        """ Override of base class function. Plays previous song in queue
        """
        song_index=self.get_song_index()
        if  song_index > 0:
            super().previous_song() # Method of MusicPlayer class
            song_index=song_index - 1
        self.song_queue.set_selected_item_index(song_index)

    def next_song(self):
        """ Override of base class function. Plays next song in queue
        """
        song_index=self.get_song_index()
        if song_index < len(self.get_queue_songs())-1:
            song_index=song_index + 1
            super().next_song() # Method of MusicPlayer class
        self.song_queue.set_selected_item_index(song_index)


    def _show_popup_file_path(self):
        self.root.show_text_box_popup("Write the path:",self.__validate_path)

    def __validate_path(self,path:str):
        """ Function to validate the path

        Parameters
        ----------
        path : str
            Path to search song files
        """
        if os.path.exists(path):
            self.change_path(path)
        else:
            # Show popup to ask for file path
            self._show_popup_file_path()

    def __load_songs(self):
        """ Function that loads songs
        """
        self._songs_file=self._file.get_music_list()
        if self._songs_file: #List is not Empty
            songs_name_list=[song.get_name() for song in self._songs_file]
            self.song_list.add_item_list(songs_name_list)
        else:   #List is empty
            self.song_list.clear()

    def __config(self):
        """ Function that configure the widgets of the window (WidgetSet)
        """
        #TODO: Add a popup to confirm to quit when there is a song playing
        self.status_bar.set_color(py_cui.BLACK_ON_WHITE)

        self.window.add_key_command(py_cui.keys.KEY_S_LOWER,self._show_popup_file_path)
        self.window.add_key_command(py_cui.keys.KEY_SPACE,self.pause_song)
        self.window.add_key_command(py_cui.keys.KEY_P_LOWER,self.previous_song)
        self.window.add_key_command(py_cui.keys.KEY_N_LOWER,self.next_song)

        self.song_list.add_key_command(py_cui.keys.KEY_ENTER,self.add_song)
        self.song_queue.add_key_command(py_cui.keys.KEY_ENTER,self.play_song)
        self.song_queue.add_key_command(py_cui.keys.KEY_BACKSPACE,self.remove_song)

        self.root.set_title("Local Music Player")

    def create(self):
        """ Function that returns a window (a widgetset)

        Returns
        -------
        window : WidgetSet
            Returns a widgetset
        """

        return self.window
