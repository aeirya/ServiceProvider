from modules import Modules
from PyQt5.QtWidgets import QApplication
import sys

class Main():
    def __init__(self) -> None:
        self.modules = Modules()
        self.modules.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Main()
    sys.exit(app.exec_())