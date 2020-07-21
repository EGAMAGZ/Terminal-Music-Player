import py_cui
import platform

from pymusicterm.ui.windows import LocalPlayerWindow
from pymusicterm.util.system import on_wsl

class App:
    """ Main pymusicterm class. Sets the WidgetSet in the beginning
    """

    windows_options=["Local Player","Soon.."]

    def __init__(self,root):
        """ Constructor for App class
        """
        self.root=root

        #Added widgets
        self.status_bar=self.root.status_bar

        self.logo_text_block=self.root.add_block_label(self.get_logo(),0,1)

        #ScrollMenus
        self.menu=self.root.add_scroll_menu("Select a Window",1,1)

        self.__config()

    def _set_widget_set(self):
        option_index=self.menu.get_selected_item_index()
        if option_index==0:
            window=LocalPlayerWindow(self.root).create()
            self.root.apply_widget_set(window)
        elif option_index==1:
            self.root.show_message_popup("On development","This function is on development")

    def _set_status_text(self) -> str:
        """ Functions that returns the name of the system the program is runned
        """
        if on_wsl():
            return "WSL"
        else:
            return platform.system()

    def get_logo(self):
        text="                                   _        _                   \n"
        text+=" ___  _ _ ._ _ _  _ _  ___<_> ___ _| |_ ___  _ _ ._ _ _\n" 
        text+="| . \| | || ' ' || | |<_-<| |/ | ' | | / ._>| '_>| ' ' |\n"
        text+="|  _/`_. ||_|_|_|`___|/__/|_|\_|_. |_| \___.|_|  |_|_|_|\n"
        text+="|_|  <___'                                              \n" 

        return text

    def __config(self):
        """ Function that configure the widgets of the window
        """
        self.menu.add_item_list(self.windows_options)
        self.menu.add_key_command(py_cui.keys.KEY_ENTER,self._set_widget_set)

        self.logo_text_block.set_color(py_cui.MAGENTA_ON_BLACK)

        self.status_bar.set_color(py_cui.BLACK_ON_GREEN)
        self.root.set_title("Terminal Music Player")
        self.root.toggle_unicode_borders()
        self.root.set_status_bar_text("You're using: {} |q-Quit|Arrow keys to move|Enter - Focus mode".format(self._set_status_text()))

def main():
    """ Entry point for pymusicterm and initialize the CUI
    """
    root=py_cui.PyCUI(3,3)
    wrapper=App(root)
    root.start()
