import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT']="hide"
from pygame import mixer
from typing import List

from pymusicterm.music import SongFile
# https://www.thecodingpup.com/post_detailed/music-player-in-python
class MusicPlayer:

    FADE_OUT_TIME:int = 500
    _song_file:SongFile = None
    _playing:bool = False
    _queue_songs:List[SongFile] = []
    _song_index:int = 0
    _is_paused:bool=False

    def __init__(self):
        #Initialize pygame
        mixer.init()

    def not_in_queue_songs(self,song_file:SongFile) -> bool:
        if not any(song.get_file_path()==song_file.get_file_path() for song in self._queue_songs):
            return True
        return False

    def add_song(self,song_file:SongFile):
        if not self._queue_songs:
            self._playing=True
            self._song_file=song_file
            mixer.music.load(self._song_file.get_file_path())
            mixer.music.play()

        self._queue_songs.append(song_file)

    def remove_song(self, index:int):
        try:
            if index == self._song_index:
                pass
            else:
                del self._queue_songs[index]
        except IndexError:
            pass

    def play_song(self,index:int):
        if self._song_index != index:
            self._song_index=index
            mixer.music.fadeout(self.FADE_OUT_TIME)
            mixer.music.load(self._queue_songs[index].get_file_path())
            mixer.music.play()

    def previous_song(self):
        index = self._song_index - 1
        self.play_song(index)

    def next_song(self):
        index= self._song_index + 1
        self.play_song(index)

    def pause(self):
        if self._is_paused:
            self._is_paused=False
            mixer.music.unpause()
        else:
            self._is_paused=True
            mixer.music.pause()

    def is_playing(self) -> bool:
        return mixer.music.get_busy()

    def get_song_index(self) -> int:
        return self._song_index

    def get_queue_songs(self) -> List[str]:
        # TODO: Change this method to return the maximum of index
        return self._queue_songs

    def stop_song(self):
        mixer.music.fadeout(self.FADE_OUT_TIME)

    def stop_song_on_quit(self):
        mixer.music.unload()
        mixer.music.stop()
