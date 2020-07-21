from PyQt5.QtWidgets import QMainWindow, QWidget, QDialog
# from PySide2 import QtCore

import ui.fin
import ui.main
import ui.adduser
import ui.useradd 

class WindowManager():
    def __init__(self) -> None:
        self.window = Window()

    def launch(self, menu):
        self.window.launch(menu)
    
    def launch_main_menu(self):
        current = ui.main.Ui_main()
        self.launch(current)
        current.pushButton_2.clicked.connect(self.launch_log_manager)

    def launch_log_manager(self):
        current = ui.fin.Ui_MainWindow()
        self.launch(current)

    def launch_add_user(self):
        current = ui.adduser.Ui_Frame()
        self.launch(current)

    def l(self):
        current = ui.useradd.Ui_Dialog()
        # self.launch(current)

        dialog = QDialog()
        dialog.ui = current
        dialog.ui.setupUi(dialog)
        # dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        dialog.exec_()

class Window(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

    def launch(self, menu):
        menu.setupUi(self)
        self.setFixedSize(800,600)
        self.show()

    def accept(self):
        pass

    def reject(self):
        pass
