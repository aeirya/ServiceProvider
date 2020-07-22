from PyQt5.QtWidgets import QMainWindow
import menus

class WindowManager():
    def __init__(self) -> None:
        self.window = Window()
        
    def start(self):
        self.launch_main_menu()
        # self.launch_log_manager()
        # self.l()

    def launch(self, menu):
        self.window.launch(menu)
    
    def launch_main_menu(self):
        menus.MainMenu(self)

    def launch_log_manager(self):
        menus.ReportMenu(self)

    def l(self):
        menus.UserAddDialog()

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
