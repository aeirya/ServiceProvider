from modules import Modules
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class Main():
    def __init__(self) -> None:
        self.modules = Modules()
        self.modules.start()
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Main()
    # w = QMainWindow()
    # w.setFixedSize(800, 400)
    # w.show()
    sys.exit(app.exec_())