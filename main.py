import py_cui

class App:

    def __init__(self,root):
        self.root=root

        self.root.set_title('Terminal Music PLayer')

        self._on_start()

    def _on_start(self):
        pass

if __name__ == "__main__":
    root=py_cui.PyCUI(3,3)
    wrapper=App(root)
    root.start()