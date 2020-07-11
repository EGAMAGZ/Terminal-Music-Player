import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT']="hide"
from pygame import mixer
from typing import List

from music import SongFile
# https://www.thecodingpup.com/post_detailed/music-player-in-python
class MusicPlayer:

    _song_file:SongFile = None
    _playing:bool = False
    _queue_songs:List[SongFile]=[]

    def __init__(self):
        #Initialize pygame
        mixer.init()

    def set_song(self,song_file:SongFile):
        if not self._queue_songs:
            self._playing=True
            self._song_file=song_file
            mixer.music.load(self._song_file.get_file_path())
            mixer.music.play()
        self._queue_songs.append(song_file)

    def is_playing(self) -> bool:
        return self._playing
