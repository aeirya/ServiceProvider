from modules import Modules
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class Main:

    def __init__(self) -> None:
        app = QApplication(sys.argv)
        self.modules = Modules()
        sys.exit(app.exec_())

if __name__ == "__main__":
    Main()
