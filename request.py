from data import Data
from workers import Worker, WorkerManager

class Request:
    def __init__(self, user_id : int, skill : str):
        self.user_id = user_id
        self.skill = skill

class RequestManager:

    def __init__(self, data : Data, workers : WorkerManager):
        self.data = data
        self.request_history = self.load_requests()
        self.workers = workers

    def load_requests(self):
        # return [Request(x[0]self.data.allRequests()
        return None

    def get_top(self, workers : list):
        result = None
        for w in workers:
            if result == None:
                result = w
            else:
                if w.score > result.score:
                    result = w
        return result

    def find_match(self, request : Request):
        matches = self.data.findWorker(skill = request.skill)
        result = self.get_top(matches)
        return result

    def get_history(self):
        return self.request_history 
        #change this