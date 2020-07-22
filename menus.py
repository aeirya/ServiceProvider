import ui.main as main
import ui.fin as report
import ui.useradd as user

from PyQt5.QtWidgets import QMainWindow, QWidget, QDialog

class MainMenu:
    def __init__(self, window):
        self.menu = main.Ui_main()
        window.launch(self.menu)
        self.window = window
        self.setup()
    
    def setup(self):
        menu = self.menu
        menu.pushButton.clicked.connect(self.f)
        menu.pushButton_2.clicked.connect(self.launch_log_manager)
        menu.pushButton_3.clicked.connect(self.quit)

    def f(self):
        print("Fuck")

    def launch_log_manager(self):
        print("clieck")
        # print(win)
        self.window.launch_log_manager()

    def quit(self):
        quit()

class ReportMenu:
    def __init__(self, window):
        menu = report.Ui_MainWindow()
        window.launch(menu)

class UserAddDialog:
    def __init__(self):
        current = user.Ui_Dialog()
        dialog = QDialog()
        dialog.ui = current
        dialog.ui.setupUi(dialog)
        # dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        dialog.exec_()