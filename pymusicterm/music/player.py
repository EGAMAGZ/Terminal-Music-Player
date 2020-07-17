import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT']="hide"
from pygame import mixer
from typing import List

from pymusicterm.music import SongFile
# https://www.thecodingpup.com/post_detailed/music-player-in-python
class MusicPlayer:
    """ Music player using pygame

    This class uses pygame as a player, which contains functions to control the music. Some 
    of this actions are pause, stop, volume up or down, add or remove song in queue, etc.
    """

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
        """Fuction to check if a SongFile that's added already exists in queue songs

        Parameters
        ----------
        song_file : SongFile
            Dataclass where the info of the song file

        Returns
        -------
        exists : bool
            returns if exists
        """
        if not any(song.get_file_path()==song_file.get_file_path() for song in self._queue_songs):
            return True
        return False

    def add_song(self,song_file:SongFile):
        """Adds a SongFile to the queue songs

        Parameters
        ----------
        song_file : SongFile
            Dataclass where the info of the song file
        """
        if not self._queue_songs:
            self._playing=True
            self._song_file=song_file # Sets actual SongFile playing
            mixer.music.load(self._song_file.get_file_path()) # Loads the song and play it automatically
            mixer.music.play()

        self._queue_songs.append(song_file) # Song added to queue songs

    def remove_song(self, index:int):
        """ Functions that removes song from queue song

        Parameters
        ----------
        index : int
            Index of item in queue songs menu
        """
        try:
            if index == self._song_index:
                pass
            else:
                del self._queue_songs[index]
        except IndexError:
            pass

    def play_song(self,index:int):
        """ Function that plays a song in queue songs

        Parameters
        ----------
        index : int
            Index of item in queue songs menu
        """
        # Validate if actual song is playing
        if self._song_index != index:
            self._song_index=index # Sets new index of new song playing
            mixer.music.fadeout(self.FADE_OUT_TIME) # Fadeout until it stops
            mixer.music.load(self._queue_songs[index].get_file_path()) # Loads the song and play it automatically
            mixer.music.play()

    def pause(self):
        """ Function that pauses the song playing
        """
        if self._is_paused:
            self._is_paused=False
            mixer.music.unpause()
        else:
            self._is_paused=True
            mixer.music.pause()

    def is_playing(self) -> bool:
        """ Return the current state of the mixer (if is busy)

        Return
        ------
        get_busy : bool
            Check if the music stream is playing
        """
        return mixer.music.get_busy()

    def stop_song(self):
        """ Function that stops actual song
        """
        pass

    def stop_song_on_quit(self):
        mixer.music.unload()
        mixer.music.stop()
