import py_cui

from ui.windows import LocalPlayerWindow

class App:

    def __init__(self,root):
        self.root=root

        self._on_start()

    def _on_start(self):
        window=LocalPlayerWindow(self.root).create()

        self.root.apply_widget_set(window)

if __name__ == "__main__":
    root=py_cui.PyCUI(3,3)
    wrapper=App(root)
    root.start()
