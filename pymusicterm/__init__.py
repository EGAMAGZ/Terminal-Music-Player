import py_cui
import platform

from pymusicterm.ui.windows import LocalPlayerWindow
from pymusicterm.util.system import on_wsl

class App:

    windows_options=["Local Player","Soon.."]

    def __init__(self,root):
        self.root=root

        #Added widgets
        self.status_bar=self.root.status_bar
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
        if on_wsl():
            return "WSL"
        else:
            return platform.system()

    def __config(self):
        self.menu.add_item_list(self.windows_options)
        self.menu.add_key_command(py_cui.keys.KEY_ENTER,self._set_widget_set)

        self.status_bar.set_color(py_cui.BLACK_ON_GREEN)
        self.root.set_title("Terminal Music Player")
        self.root.toggle_unicode_borders()
        self.root.set_status_bar_text("You're using: {} |q-Quit|Arrow keys to move|Enter - Focus mode".format(self._set_status_text()))

def main():
    root=py_cui.PyCUI(3,3)
    wrapper=App(root)
    root.start()
