import py_cui

class SongInfoBlockLabel:

    _row:int=0
    _column:int=2
    _row_span:int=2
    _column_span:int=3
    _center:bool=False

    def __init__(self,window):
        self.window=window
        self.block_label=self.window.add_block_label("Sample",self._row,self._column,
        row_span=self._row_span,column_span=self._column_span,center=self._center)

        self.__config()

    def _initial_state(self):
        pass

    def set_song(self):
        pass

    def __config(self):
        self._initial_state()
        self.block_label.set_color(py_cui.BLACK_ON_WHITE)
