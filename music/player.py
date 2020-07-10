import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT']="hide"
from pygame import mixer

from music import SongFile

class MusicPlayer:

    _song_file:SongFile = None
    _playing:bool = False

    def __init__(self):
        # mixer.init()
        pass

    def set_song(self,song_file:SongFile):
        self._song_file=song_file
        self.__change_song()

    def __change_song(self):
        if self._song_file is not None:
            pass

    def is_playing(self) -> bool:
        return self._playing
