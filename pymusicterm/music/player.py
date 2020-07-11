import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT']="hide"
from pygame import mixer
from typing import List

from music import SongFile
# https://www.thecodingpup.com/post_detailed/music-player-in-python
class MusicPlayer:

    FADE_OUT_TIME:int = 500
    _song_file:SongFile = None
    _playing:bool = False
    _queue_songs:List[SongFile] = []
    _song_index:int = 0
    _is_paused:bool=False

    def __init__(self,menu_widget):
        #Initialize pygame
        mixer.init()
        self.song_queue=menu_widget

    def add_song(self,song_file:SongFile):
        if not self._queue_songs:
            self._playing=True
            self._song_file=song_file
            mixer.music.load(self._song_file.get_file_path())
            mixer.music.play()

        if not any(song.get_file_path()==song_file.get_file_path() for song in self._queue_songs):
            self._queue_songs.append(song_file)
            self.song_queue.add_item(song_file.get_name())

    def play_song(self,index:int):
        if self._song_index != index:
            self._song_index=index
            mixer.music.fadeout(self.FADE_OUT_TIME)
            mixer.music.load(self._queue_songs[index].get_file_path())
            mixer.music.play()

    def pause(self):
        if self._is_paused:
            self._is_paused=False
            mixer.music.unpause()
        else:
            self._is_paused=True
            mixer.music.pause()

    def is_playing(self) -> bool:
        return mixer.music.get_busy()

    def stop_song(self):
        pass

    def stop_song_on_quit(self):
        mixer.music.unload()
        mixer.music.stop()
