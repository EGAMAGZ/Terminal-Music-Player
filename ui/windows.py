import py_cui

class LocalPlayerWindow:

    _colums:int = 3
    _rows:int = 4

    def __init__(self,root):

        self.root = root
        self.window=self.root.create_new_widget_set(self._rows,self._colums)

        #Added elements
        self.status_bar=self.root.status_bar

        self.__config()
    
    def __config(self):
        self.status_bar.set_color(py_cui.BLACK_ON_WHITE)
        self.root.set_title("Local Music Player")

    def create(self):
        return self.window
