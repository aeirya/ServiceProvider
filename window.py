from PyQt5.QtWidgets import QMainWindow, QWidget, QDialog

import ui.fin
import ui.main
import ui.adduser
import ui.useradd 
# import menus

class WindowManager():
    def __init__(self) -> None:
        self.window = Window()
        
    def start(self):
        self.launch_main_menu()
        # self.launch_log_manager()

    def launch(self, menu):
        self.window.launch(menu)
    
    def launch_main_menu(self):
        import menus
        menus.MainMenu(self)

    def launch_log_manager(self):
        import menus
        menus.ReportMenu(self)

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
        # self.setFixedSize(800,600)
        self.show()

    def accept(self):
        pass

    def reject(self):
        pass
