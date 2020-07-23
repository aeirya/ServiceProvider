import datetime

class Date:
    def __init__(self):
        self.format = "%m/%d/%Y, %H:%M:%S"

    def to_date(self, string : str):
        return datetime.strptime(string, self.format)

    def to_string(self, date):
        return date.strftime(self.format)