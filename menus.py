import ui.main as main
import ui.fin as report
from window import Window

class MainMenu:
    def __init__(self, window : Window):
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

