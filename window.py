from PyQt5.QtWidgets import QMainWindow, QDialog
import menus

class WindowManager():
    def __init__(self, modules) -> None:
        self.window = Window()
        self.modules = modules
        
    def start(self):
        self.launch_main_menu()
 
    def launch(self, menu):
        self.window.hide()
        self.window = Window()
        self.window.launch(menu)
    
    def launch_main_menu(self):
        self.menu = menus.MainMenu(self)

    def launch_clients_menu(self):
        self.menu = menus.ClientsMenu(self, self.modules.users)
        
    def launch_log_manager(self):
        self.menu = menus.ReportMenu(self)

    def launch_add_user_menu(self):
        self.pop = menus.AddUserMenu(self, self.modules.users)

    def launch_workers_menu(self):
        self.menu = menus.WorkersMenu(self, self.modules.workers)

    def launch_worker_search(self):
        self.menu = menus.WorkerEdit(self, self.modules.workers)

    def launch_worker_add(self):
        self.pop = menus.WorkerAdd(self, self.modules.workers)

    def pop_dialog(self, menu):
        self.dialog = QDialog()
        menu.setupUi(self.dialog)
        self.dialog.show()
        # self.dialog.exec()

class Window(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

    def launch(self, menu):
        menu.setupUi(self)
        self.setFixedSize(800,600)
        self.show()