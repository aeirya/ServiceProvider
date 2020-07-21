from PyQt5.QtWidgets import QMainWindow, QApplication
from ui.main import Ui_main
from ui.fin import Ui_MainWindow
from window import WindowManager
import sys

class Main():
    def __init__(self) -> None:
        app = QApplication(sys.argv)
        self.window = WindowManager()
        self.window.launch_main_menu()
        self.window.l()
        # self.window.launch_add_user()
        sys.exit(app.exec_())

    def launch(self, ui):
        ui.setupUi(self.window)
        self.window.show()

if __name__ == "__main__":
    Main()