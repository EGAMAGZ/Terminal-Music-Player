import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT']="hide"
import threading
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
    _queue_songs:List[SongFile] = []
    _song_index:int = 0
    _stopped:bool=False
    _main_thread:threading.Thread
    paused:bool=False

    def __init__(self):
        """ Constructor for MusicPLayer
        """
        mixer.init() #Initialize pygame

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
            self._song_file=song_file # Sets actual SongFile playing
            mixer.music.load(self._song_file.get_file_path()) # Loads the song and play it automatically
            mixer.music.play()
            self._check_player()

        self._queue_songs.append(song_file) # Song added to queue songs

    def remove_song(self, index:int):
        """ Removes song from queue

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
        else:
            mixer.music.rewind()

    def previous_song(self):
        """ Plays previous song in queue
        """
        index = self._song_index - 1
        self.play_song(index)

    def next_song(self):
        """ Plays next song in queue
        """
        index= self._song_index + 1
        self.play_song(index)

    def pause_song(self):
        """ Pauses the song playing
        """
        if self.paused:
            self.paused=False
            mixer.music.unpause()
        else:
            self.paused=True
            mixer.music.pause()

    def is_playing(self) -> bool:
        """ Return the current state of the mixer (if is busy)

        Return
        ------
        get_busy : bool
            Check if the music stream is playing
        """
        return mixer.music.get_busy()

    def get_song_index(self) -> int:
        """ Gets actual index of the list of queue songs

        Returns
        -------
        song_index : int
            Actual index
        """
        return self._song_index

    def get_queue_songs(self) -> List[str]:
        """ Gets the list of queue songs

        Returns
        -------
        queue_songs : List[str]
            Queue songs
        """
        return self._queue_songs

    def stop_song(self):
        """ Function that stops actual song
        """
        self._stopped=True
        self._main_thread.join()
        mixer.music.fadeout(self.FADE_OUT_TIME)

    def auto_play(self):
        if not self.is_playing():
            if self._song_index < len(self._queue_songs)-1:
                self.next_song()

    def _check_player(self):
        def check_player_thread():
            while not self._stopped:
                self.auto_play()

        self._main_thread=threading.Thread(target=check_player_thread)
        self._main_thread.start()
