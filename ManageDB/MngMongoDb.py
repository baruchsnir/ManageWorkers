# Getting the database instance
import pymongo
import pandas




class ManageDB():

    def UpdateDataBase(self, hostip):
        # Creating a pymongo client
        host = 'localhost:27017'
        empty = True
        if hostip != '':
            host = hostip
        conectionstring = "mongodb://{}/".format(host)

        try:
            client = pymongo.MongoClient(conectionstring)

            # Getting the database instance
            mydb = client['ManageWorkers']
            print("Database created........")

            # Verification
            print("List of databases after creating new one")
            list = client.list_database_names()
            print(list)
            mytable = mydb["Workers"]
            mydoc = mytable.find()
            for x in mydoc:
                empty = False
                break
            if empty:
                worker_list = self.load_workers_data_from_csv()
                self.insertDataToTable(mytable, self.worker_list)
                mytable = mydb["Jobs"]
                jobs = self.load_jobs_data_from_csv()
                self.insertDataToTable(mytable, jobs)
                mytable = mydb["Departments"]
                departments = self.load_departments_data_from_csv()
                self.insertDataToTable(mytable, departments)
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print('Exception - ', message)

    def load_jobs_data_from_csv(self):
        jobs_list = []
        df = pandas.read_csv('jobs.csv', index_col='job_id',
                             parse_dates=['hire_date'],
                             header=0,
                             names=['job_id', 'name'])
        for it in df.iterrows():
            j = it[1]
            worker = {"job_id": int(it[0]),
                      "name": j['name']}
            jobs_list.append(worker)
        return jobs_list
    def load_workers_data_from_csv(slef):
        worker_list = []
        df = pandas.read_csv('workerslist.csv', index_col='emploee_id',
                             parse_dates=['hire_date'],
                             header=0,
                             names=['emploee_id', 'first_name', 'last_name', 'email', 'phone_number', 'hire_date',
                                    'job_id', 'salary', 'commission_pct', 'manager_id', 'department_id', 'picture'])
        for it in df.iterrows():
            j = it[1]
            worker = {"emploee_id": int(it[0]),
                      "first_name": j['first_name'],
                      "last_name": j['last_name'],
                      "email": j['email'],
                      "phone_number": int(j['phone_number']),
                      "hire_date": j['hire_date'],
                      "job_id": j['job_id'],
                      "salary": int(j['salary']),
                      "commission_pct": float(j['commission_pct']),
                      "manager_id": int(j['manager_id']),
                      "department_id": int(j['department_id']),
                      "picture": int(j['picture'])
                      }
            worker_list.append(worker)
        return worker_list


    def insertDataToTable(self,mytable, worker_list):
        mytable.insert_many(worker_list)
        mydoc = mytable.find()
        for x in mydoc:
            print(x)


    def load_departments_data_from_csv(self):
        jobs_list = []
        df = pandas.read_csv('departments.csv', index_col='department_id',
                             parse_dates=['department_id'],
                             header=0,
                             names=['department_id', 'name'])
        for it in df.iterrows():
            j = it[1]
            worker = {"job_id": int(it[0]),
                      "name": j['name']}
            jobs_list.append(worker)
        return jobs_list
