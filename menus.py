from user import User, UserManager
import ui.main as main
import ui.fin as report
import ui.useradd as user

from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QWidget, QDialog

class MainMenu:
    def __init__(self, window):
        self.menu = main.Ui_main()
        window.launch(self.menu)
        self.window = window
        self.setup()
    
    def setup(self):
        menu = self.menu
        menu.pushButton.clicked.connect(self.quit)
        menu.pushButton_2.clicked.connect(self.launch_log_manager)
        menu.pushButton_3.clicked.connect(self.launch_clients_menu)

    def launch_clients_menu(self):
        self.window.launch_clients_menu()

    def launch_log_manager(self):
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

class ClientsMenu:
    def __init__(self, window, usermanager : UserManager):
        from ui.clients import Ui_MainWindow
        self.menu = Ui_MainWindow()
        self.usermanager = usermanager
        window.launch(self.menu)
        self.window = window
        self.setup()

    def setup(self):
        menu = self.menu
        menu.addUserButton.clicked.connect(self.launch_add_user)
        self.fill_rows()

    def fill_rows(self):
        menu = self.menu
        um = self.usermanager
        users = um.get_users()
        table = menu.table
        table.clearContents()
        table.setColumnCount(5)
        table.setRowCount(len(users))

        r = 0
        for user in users:
            table.insertRow(r)  
            fill = lambda c, text : table.setItem(r, c, QTableWidgetItem(text))
            fill(0, user.id)
            fill(1, user.firstname)
            fill(2, user.surname)
            fill(3, user.phone)
            fill(4, user.address)
            r += 1
            

    def launch_add_user(self):
        self.window.launch_add_user_menu()
        print("refresh")
        self.fill_rows()

class AddUserMenu:
    def __init__(self, window, usermanager):
        self.users = usermanager
        from ui.useradd import Ui_Dialog
        self.menu = Ui_Dialog()
        self.setup()
        
        m = self.menu
        self.fname = m.lineEdit
        self.lname = m.lineEdit_2
        self.phone = m.lineEdit_3
        self.address = m.lineEdit_4

        self.exec()

    def setup(self):
        dialog = QDialog()
        self.menu.setupUi(dialog)
        dialog.accepted.connect(self.add_user)
        self.menu.pushButton.clicked.connect(self.add_button_clicked)
        self.exec = lambda: dialog.exec()

    def add_button_clicked(self):
        self.add_user()
        self.clear()

    def add_user(self):
        fname = self.fname.text()
        lname = self.lname.text()
        phone = self.phone.text()
        address = self.address.text()
        id = self.get_next_id()
        self.users.add_user(User(0, fname, lname, phone, address))


    def get_next_id(self):
        return 0
        
    def clear(self):
        cls = lambda lineEdit : lineEdit.setText("")
        cls(self.fname)
        cls(self.lname)
        cls(self.phone)
        cls(self.address)