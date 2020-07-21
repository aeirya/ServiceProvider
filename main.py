from PyQt5.QtWidgets import QMainWindow, QApplication
from form import Ui_main
from log import Ui_MainWindow
import sys

class Main():
    def __init__(self) -> None:
        app = QApplication(sys.argv)
        self.window = QMainWindow()
        self.launch(Ui_main())
        self.launch(Ui_MainWindow())
        sys.exit(app.exec_())

    def launch(self, ui):
        ui.setupUi(self.window)
        self.window.show()
        # self.window.close()

if __name__ == "__main__":
    Main()