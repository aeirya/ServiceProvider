from workers import WorkerManager
from data import Data
from user import UserManager
from window import WindowManager

class Modules():
    def __init__(self) -> None:
        self.data = Data()
        self.users = UserManager(self.data)
        self.workers = WorkerManager(self.data)
        self.window = WindowManager(self)
        self.start()

    def start(self):
        self.window.start()