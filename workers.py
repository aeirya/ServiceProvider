class Worker:
    def __init__(self, id , fname, lname, phone, skills, score):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.phone = phone
        self.skills = skills
        self.score = score

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