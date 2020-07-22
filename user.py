from data import Data

class User():
    def __init__(self, id, firstname, surname, phone, address) -> None:
        self.id = id
        self.firstname = firstname
        self.surname = surname
        self.phone = phone
        self.address = address

class UserManager():
    def __init__(self, data : Data):
        self.data = data
        self.load_users()
    
    def load_users(self):
        self.users = self.data.allCustomers()

    def get_users(self):
        return self.users

    def add_user(self, user : User):
        self.data.addCustomer(user.firstname, user.surname, user.phone, user.address)
        self.load_users()