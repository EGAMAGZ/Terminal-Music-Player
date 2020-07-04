class LocalPlayerWindow:

    _colums:int = 4
    _rows:int = 3

    def __init__(self,root):

        self.root = root
        self.window=self.root.create_new_widget_set(self._colums,self._rows)

        self._config()
    
    def _config(self):
        self.root.set_title("Local Music Player")

    def create(self):
        return self.window
