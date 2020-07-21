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
    
    def load_users(self):
        self.users = self.data.allCustomers()

    def add_user(self, user : User):
        self.data.addCustomer(user.firstname, user.surname, user.phone, user.address)
        self.load_users()