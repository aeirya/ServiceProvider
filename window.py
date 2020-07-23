from PyQt5.QtWidgets import QMainWindow
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
        menus.ReportMenu(self)

    def launch_add_user_menu(self):
        menus.AddUserMenu(self, self.modules.users)

    def launch_workers_menu(self):
        menus.WorkersMenu(self)

    def launch_worker_search(self):
        menus.WorkerEdit(self)

class Window(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

    def launch(self, menu):
        menu.setupUi(self)
        self.setFixedSize(800,600)
        self.show()