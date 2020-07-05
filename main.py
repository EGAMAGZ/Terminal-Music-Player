import py_cui

from ui.windows import LocalPlayerWindow

class App:

    windows_options=["Local Player","Spotify Player"]

    def __init__(self,root):
        self.root=root

        self.menu=self.root.add_scroll_menu("Select a Window",1,1)
        self.menu.add_item_list(self.windows_options)
        self.menu.add_key_command(py_cui.keys.KEY_ENTER,self._set_widget_set)

        self._config()

    def _config(self):
        self.root.set_title("Terminal Music Player")

    def _set_widget_set(self):
        option_index=self.menu.get_selected_item_index()
        if option_index==0:
            window=LocalPlayerWindow(self.root).create()
            self.root.apply_widget_set(window)
        elif option_index==1:
            self.root.show_message_popup("On development","This function is on development")

if __name__ == "__main__":
    root=py_cui.PyCUI(3,3)
    wrapper=App(root)
    root.start()
