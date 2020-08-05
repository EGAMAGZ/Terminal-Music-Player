from pymusicterm.ui.progressbar import LoadingBarWidget
import py_cui
import platform
import argparse

from pymusicterm.ui.windows import LocalPlayerWindow
from pymusicterm.util.system import on_wsl

__version__='0.0.2'

class ImpPyCUI(py_cui.PyCUI):
    
    def __init__(self,num_rows,num_cols) -> None:
        super().__init__(num_rows,num_cols)

    def add_progress_bar(self, title, row, column, row_span = 1, column_span = 1, padx = 1, pady = 0) -> LoadingBarWidget:
        id = 'Widget{}'.format(len(self._widgets.keys()))
        new_progress_bar=LoadingBarWidget(id,title,self._grid,row,column,row_span,column_span,padx,pady,self._logger)

        self._widgets[id]=new_progress_bar
        if self._selected_widget is None:
            self.set_selected_widget(id)
        self._logger.debug('Adding widget {} w/ ID {} of type {}'.format(title,id,str(type(new_progress_bar))))
        return new_progress_bar

class App:
    """ Main pymusicterm class. Sets the WidgetSet in the beginning
    """

    WINDOWS_OPTIONS=["Local Player","Soon.."]

    def __init__(self,root:ImpPyCUI):
        """ Constructor for App class
        """
        self.root=root

        #Added widgets
        self.status_bar=self.root.status_bar

        self.logo_text_block=self.root.add_block_label(self._get_logo(),0,0,column_span=3)

        #ScrollMenus
        self.menu=self.root.add_scroll_menu("Select a Window",1,1)
        self.root.add_progress_bar("HELLO",1,0)

        self.__config()

    def _set_widget_set(self):
        option_index=self.menu.get_selected_item_index()
        if option_index==0:
            if on_wsl():
                self.root.show_error_popup("Important","Your system is not supported for this feature")
            else:
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

    def _get_logo(self) -> str:
        """ Generates logo of program

        Returns
        -------
        logo : str
            Returns the logo to be place on a widget
        """
        logo="                                   _        _                   \n"
        logo+=" ___  _ _ ._ _ _  _ _  ___<_> ___ _| |_ ___  _ _ ._ _ _\n" 
        logo+="| . \| | || ' ' || | |<_-<| |/ | ' | | / ._>| '_>| ' ' |\n"
        logo+="|  _/`_. ||_|_|_|`___|/__/|_|\_|_. |_| \___.|_|  |_|_|_|\n"
        logo+="|_|  <___'                                              \n" 

        return logo

    def __config(self):
        """ Function that configure the widgets of the window
        """
        self.menu.add_item_list(self.WINDOWS_OPTIONS)
        self.menu.add_key_command(py_cui.keys.KEY_ENTER,self._set_widget_set)

        self.logo_text_block.set_color(py_cui.MAGENTA_ON_BLACK)

        self.status_bar.set_color(py_cui.BLACK_ON_GREEN)
        self.root.set_title("pymusicterm - {}".format(__version__))
        self.root.toggle_unicode_borders()
        self.root.set_status_bar_text("You're using: {} |q-Quit|Arrow keys to move|Enter - Focus mode".format(self._set_status_text()))

def main():
    """ Entry point for pymusicterm and initialize the CUI
    """
    parser=argparse.ArgumentParser()
    parser.add_argument('--version',action='version',version=__version__)
    args=parser.parse_args()

    root=ImpPyCUI(3,3)
    try:
        wrapper=App(root)
        root.start()
    except py_cui.py_cui.errors.PyCUIOutOfBoundsError:
        print("Your terminal is too small, try increasing it's size")
