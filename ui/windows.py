import py_cui

class LocalPlayerWindow:

    _colums:int = 5
    _rows:int = 7

    def __init__(self,root):

        self.root = root
        self.window=self.root.create_new_widget_set(self._rows,self._colums)

        #Added widgets
        self.status_bar=self.root.status_bar
        self.song_info=self.window.add_block_label("Sample",0,2,row_span=2,column_span=3,center=False)
        self.song_list=self.window.add_scroll_menu("Songs list",3,2,column_span=3)
        self.__config()

    def __config(self):
        self.status_bar.set_color(py_cui.BLACK_ON_WHITE)
        self.song_info.set_color(py_cui.BLACK_ON_WHITE)
        self.song_list.set_color(py_cui.BLACK_ON_WHITE)

        self.root.set_title("Local Music Player")

    def create(self):
        return self.window
