class Worker:
    id = None
    fname = None
    lname = None
    phone = None
    score = None
    skills = None

    def __init__(self, items):
        self.id = items[0]
        self.fname = items[1]
        self.lname = items[2]
        self.phone = items[3]
        self.score = items[4]
        self.skills = items[5]

    def __str__(self) -> str:
        return str((self.id, self.fname, self.lname, self.phone, self.score, self.skills))

class WorkerManager:
    
    def __init__(self, data):
        self.data = data
        self.workers = data.allWorkers()

    def add_worker(self, worker : Worker):
        self.data.addWorker(worker.fname, worker.lname, worker.phone, worker.skills)

    def search_worker(self, id):
        worker = self.data.findWorker(id)
        print(Worker(worker))

    def get_all_tuples(self):
        return self.workers