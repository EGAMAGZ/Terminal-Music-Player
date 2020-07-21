import py_cui
from typing import List

from pymusicterm.ui.popups import local_player_help_popup

class LocalPlayerSettingsMenu:

    MENU_OPTIONS:List[str]=[]
    TITLE:str="Settings"
    ROW:int=3
    COLUMN:int=0
    ROW_SPAN:int=3
    COLUMN_SPAN:int=2

    def __init__(self,window,root):
        self.window=window
        self.root=root

        self.menu=self.window.add_scroll_menu(self.TITLE,self.ROW,self.COLUMN,
        self.ROW_SPAN,self.COLUMN_SPAN)

        self.__config()

    def _selected_item(self):
        pass

    def __config(self):
        self.menu.add_item_list(self.MENU_OPTIONS)

        self.menu.add_key_command(py_cui.keys.KEY_ENTER,self._selected_item)