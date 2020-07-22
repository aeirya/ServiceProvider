from sqlite3 import connect

class Data():
    
    def __init__(self, path = 'data.db'):
        self.path = path
        self.startup()
    
    def __create_connection(self):
        connection = None

        try:
            connection = connect(self.path)
            return connection
        except:
            raise Exception('Database connection failed!')

    def __empty_check(self, var, text):
        if str(var).strip() == '':
            return text
        else:
            return var

    def __remove_empty_items(self, li):
        output = []
        for i in li:
            if str(i).strip() != '':
                output.append(str(i).strip().lower())
        return output



    #! Skill
    def allSkills(self):
        try:
            connection = self.__create_connection()
            cursor = connection.cursor()

            cursor.execute('SELECT * FROM "skills"')
            skills = list(cursor.fetchall())

            return skills
        except:
            return False

    def addSkill(self, name):
        connection = self.__create_connection()
        cursor = connection.cursor()

        name = str(name).strip().lower()

        cursor.execute('SELECT count FROM "skills" WHERE name=?', (name,))
        skill = cursor.fetchone()[0]

        if skill:
            cursor.execute('UPDATE "skills" SET count=? WHERE name=?', (skill+1, name))
            connection.commit()
        else:
            cursor.execute('INSERT INTO "skills" VALUES(NULL, ?, 1)', (name,))
            connection.commit()

    def removeSkill(self, name):
        connection = self.__create_connection()
        cursor = connection.cursor()

        name = str(name).strip().lower()

        cursor.execute('SELECT count FROM "skills" WHERE name=?', (name,))
        skill = cursor.fetchone()[0]

        if skill:
            if skill <= 1:
                cursor.execute('DELETE FROM "skills" WHERE name=?', (name,))
                connection.commit()
            else:
                cursor.execute('UPDATE "skills" SET count=? WHERE name=?', (skill-1, name))
                connection.commit()



    
    #! Requests
    def allRequests(self):
        try:
            connection = self.__create_connection()
            cursor = connection.cursor()

            cursor.execute('SELECT * FROM "requests"')
            requests = list(cursor.fetchall())

            return requests
        except:
            return False

    def addRequest(self, date, skill, customer, worker, score, cost, income):
        try:
            connection = self.__create_connection()
            cursor = connection.cursor()

            cursor.execute('INSERT INTO "requests" VALUES(NULL, ?, ?, ?, ?, ?, ?, ?)',
            (date, skill, customer, worker, score, cost, income))
            connection.commit()

            w = self.findWorker(userid= worker)
            cursor.execute('UPDATE "workers" SET score=? WHERE id=?', (w[5]+score, worker))
            connection.commit()

            return True
        except:
            return False



    #! Customer
    def allCustomers(self):
        try:
            connection = self.__create_connection()
            cursor = connection.cursor()

            cursor.execute('SELECT * FROM "customers"')
            customers = list(cursor.fetchall())

            return customers
        except:
            return False

    def findCustomer(self, userid='', name='', phone='', address=''):
        connection = self.__create_connection()
        cursor = connection.cursor()

        if str(userid).strip() != '':
            cursor.execute('SELECT FROM "customers" WHERE id=?', (int(userid),))
            return cursor.fetchone()[0]

        elif str(name).strip() != '':
            cursor.execute('SELECT FROM "customers" WHERE firstname LIKE "%?%" OR lastname LIKE "%?%"', (name, name))
            return cursor.fetchall()

        elif str(phone).strip() != '':
            cursor.execute('SELECT FROM "customers" WHERE phone LIKE "%?%"', (phone,))
            return cursor.fetchall()

        elif str(address).strip() != '':
            cursor.execute('SELECT FROM "customers" WHERE address LIKE "%?%"', (address,))
            return cursor.fetchall()

        else:
            pass

    def addCustomer(self, fname, lname, phone, address):
        try:
            connection = self.__create_connection()
            cursor = connection.cursor()

            cursor.execute('INSERT INTO "customers" VALUES(NULL, ?, ?, ?, ?)', (fname, lname, phone, address))
            connection.commit()
            return True
        except:
            return False
    
    def editCustomer(self, userid, fname='', lname='', phone='', address=''):
        try:
            connection = self.__create_connection()
            cursor = connection.cursor()

            cursor.execute('SELECT FROM "customers" WHERE id=?', (userid,))
            user = cursor.fetchone()[0]

            fname = self.__empty_check(fname, user[1])
            lname = self.__empty_check(lname, user[2])
            phone = self.__empty_check(phone, user[3])
            address = self.__empty_check(address, user[4])

            cursor.execute('UPDATE "customers" SET firstname=?, lastname=?, phone=?, address=? WHERE id=?',
            (fname, lname, phone, address, userid))
            connection.commit()
            return True
        except:
            return False

    def removeCustomer(self, userid):
        try:
            connection = self.__create_connection()
            cursor = connection.cursor()

            cursor.execute('DELETE FROM "customers" WHERE id=?', (userid,))
            connection.commit()
            return True
        except:
            return False


    
    #! Worker
    def allWorkers(self):
        try:
            connection = self.__create_connection()
            cursor = connection.cursor()

            cursor.execute('SELECT * FROM "workers"')
            workers = list(cursor.fetchall())

            return workers
        except:
            return False

    def findWorker(self, userid='', name='', phone='', skill=''):
        connection = self.__create_connection()
        cursor = connection.cursor()

        if str(userid).strip() != '':
            cursor.execute('SELECT FROM "workers" WHERE id=?', (int(userid),))
            return cursor.fetchone()[0]

        elif str(name).strip() != '':
            cursor.execute('SELECT FROM "workers" WHERE firstname LIKE "%?%" OR lastname LIKE "%?%"', (name, name))
            return cursor.fetchall()

        elif str(phone).strip() != '':
            cursor.execute('SELECT FROM "workers" WHERE phone LIKE "%?%"', (phone,))
            return cursor.fetchall()

        elif str(skill).strip() != '':
            cursor.execute('SELECT FROM "workers" WHERE skills LIKE "%?%"', (skill,))
            return cursor.fetchall()

        else:
            pass

    def addWorker(self, fname, lname, phone, skills, score=0):
        try:
            connection = self.__create_connection()
            cursor = connection.cursor()

            skillNames = self.__remove_empty_items(str(skills).split(','))
            skills = skills[1:]

            cursor.execute('INSERT INTO "workers" VALUES(NULL, ?, ?, ?, ?, ?)', (fname, lname, phone, skills, score))
            connection.commit()

            for item in skillNames:
                self.addSkill(item)

            return True
        except:
            return False
    
    def editWorker(self, userid, fname='', lname='', phone='', skills=''):
        try:
            connection = self.__create_connection()
            cursor = connection.cursor()

            cursor.execute('SELECT FROM "workers" WHERE id=?', (userid,))
            user = cursor.fetchone()[0]

            fname = self.__empty_check(fname, user[1])
            lname = self.__empty_check(lname, user[2])
            phone = self.__empty_check(phone, user[3])
            skills = self.__empty_check(skills, user[4])

            cursor.execute('UPDATE "workers" SET firstname=?, lastname=?, phone=?, skills=? WHERE id=?',
            (fname, lname, phone, skills, userid))
            connection.commit()

            oldSkills = str(user[4]).split(',')
            for item in oldSkills:
                self.removeSkill(item)

            skills = str(skills).split(',')
            for item in skills:
                self.addSkill(item)

            return True
        except:
            return False

    def removeWorker(self, userid):
        try:
            connection = self.__create_connection()
            cursor = connection.cursor()

            cursor.execute('SELECT skills FROM "workers" WHERE id=?', (userid,))
            skills = str(cursor.fetchone()[0]).split(',')

            cursor.execute('DELETE FROM "workers" WHERE id=?', (userid,))
            connection.commit()

            for item in skills:
                self.removeSkill(item)

            return True
        except:
            return False



    #! Startup
    def startup(self):
        connection = self.__create_connection()
        cursor = connection.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS "customers" (
                "id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                "firstname"	TEXT NOT NULL,
                "lastname"	TEXT NOT NULL,
                "phone"	TEXT,
                "address"	TEXT
            );
        ''')
        connection.commit()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS "workers" (
                "id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                "firstname"	TEXT NOT NULL,
                "lastname"	TEXT NOT NULL,
                "phone"	TEXT,
                "skills"	TEXT NOT NULL,
                "score"	INTEGER NOT NULL DEFAULT 0
            );
        ''')
        connection.commit()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS "skills" (
                "id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                "name"	TEXT NOT NULL,
                "count"	INTEGER NOT NULL DEFAULT 0
            );
        ''')
        connection.commit()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS "requests" (
                "id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                "date"	TEXT NOT NULL,
                "skill"	TEXT NOT NULL,
                "customer"	INTEGER NOT NULL,
                "worker"	INTEGER NOT NULL,
                "score"	INTEGER NOT NULL DEFAULT 1,
                "cost"	INTEGER NOT NULL,
                "income"	INTEGER NOT NULL
            );
        ''')
        connection.commit()
