import ui.main as main
import ui.fin as report
import ui.useradd as user

from PyQt5.QtWidgets import QMainWindow, QWidget, QDialog

class MainMenu:
    def __init__(self, window):
        self.window = window
        menu = main.Ui_main()
        window.launch(menu)
        menu.pushButton_2.clicked.connect(self.launch_log_manager)
    def launch_log_manager(self):
        self.window.launch_log_manager()

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