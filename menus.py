from workers import Worker
from user import User, UserManager
import ui.main as main
import ui.fin as report
import ui.useradd as user

from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QWidget, QDialog, QInputDialog

class MainMenu:
    def __init__(self, window):
        self.menu = main.Ui_main()
        window.launch(self.menu)
        self.window = window
        self.setup()
    
    def setup(self):
        menu = self.menu
        menu.quitButton.clicked.connect(self.quit)
        menu.reportButton.clicked.connect(self.launch_log_manager)
        menu.clientsButton.clicked.connect(self.launch_clients_menu)
        menu.workersButton.clicked.connect(self.launch_workers_menu)

    def launch_clients_menu(self):
        self.window.launch_clients_menu()

    def launch_log_manager(self):
        self.window.launch_log_manager()

    def launch_workers_menu(self):
        self.window.launch_workers_menu()

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
        menu.backButton.clicked.connect(self.back)
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

    def back(self):
        self.window.launch_main_menu()

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

class WorkersMenu:
    def __init__(self, window, workers):
        self.workers = workers
        from ui.worker import Ui_MainWindow
        self.menu = Ui_MainWindow()
        window.launch(self.menu)
        self.window = window
        self.setup()
        self.refresh()
    
    def setup(self):
        m = self.menu
        m.addButton.clicked.connect(self.add)
        m.searchButton.clicked.connect(self.window.launch_worker_search)
        m.backButton.clicked.connect(self.window.launch_main_menu)
        m.deleteButton.clicked.connect(self.delete)

    def delete(self):
        title = 'حذف خدمات دهنده'
        message = 'شماره شناسه فرد مورد نظر'
        text, ok = QInputDialog.getText(self.window.window,title ,message )
        id = int(text)
        if ok:
            self.data.removeWorker(id)
        self.refresh()

    def add(self):
        self.window.launch_worker_add()
        self.refresh()

    def search(self):
        self.window.launch_worker_search()

    def refresh(self):
        items = self.workers.get_all_tuples()
        self.fill_rows(items)

    def fill_rows(self, items):
        table = self.menu.table
        table.clearContents()
        table.setColumnCount(len(items[0]))
        table.setRowCount(len(items))
        r = 0
        for item in items:
            table.insertRow(r)  
            fill = lambda c, text : table.setItem(r, c, QTableWidgetItem(text))
            i = 0
            for x in item:
                fill(i, x)
                i += 1
            r += 1

class WorkerEdit:

    def __init__(self, window, workers):
        self.workers = workers
        from ui.worker_edit import Ui_MainWindow
        self.menu = Ui_MainWindow()
        window.launch(self.menu)
        self.window = window
        self.setup()

    def setup(self):
        m = self.menu
        m.backButton.clicked.connect(self.window.launch_workers_menu)
        m.removeButton.clicked.connect(self.remove)
        m.searchButton.clicked.connect(self.search_btn_clicked)

    def search_btn_clicked(self):
        id = self.menu.idSearchText.text()
        id = int(id)
        self.search(id)

    def search(self, id):
        worker = self.get_worker(id)
        self.display_worker(worker)

    def get_worker(self, id):
        # edit
        worker = self.workers.search_worker(id)
        return Worker

    def display_worker(self, worker):
        m = self.menu
        m.nameLbl = worker.fname
        m.lnameLbl = worker.lname
        m.phoneLbl = worker.phone
        m.scoreLbl = worker.score

    def remove(self):
        m = self.menu
        m.listbox.removeItemWidget(m.listbox.item(m.listbox.currentIndex)) 

class WorkerAdd:

    def __init__(self, window, workers):
        self.workers = workers
        from ui.worker_add import Ui_Dialog
        self.menu = Ui_Dialog()
        window.pop_dialog(self.menu)
        self.setup()

    def setup(self):
        b = self.menu.buttonBox
        b.accepted.connect(self.add)

    def add(self):
        worker = self.get_worker()
        self.workers.add_worker(worker)

    def get_worker(self):
        m = self.menu
        fname = m.nameText.text()
        lname = m.lnameText.text()
        phone = m.phoneText.text()
        skills = self.get_skills()
        score = 0
        return Worker(0, fname, lname, phone, skills, score)

    def get_skills(self):
        skills = self.menu.skillsText.toPlainText()
        skills = "".join(skills)
        skills = skills.split("\n")
        skills = ",".join(skills)
        return skills