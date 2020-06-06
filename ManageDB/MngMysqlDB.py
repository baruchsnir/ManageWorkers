import pandas
import mysql.connector


class MngMysqlDB():

    def UpdateDataBase(self, host, port, user, password, database):
        # Creating a pymongo client
        empty = True
        connection = ''
        try:
            connection_config_dict = {
                'user': user,
                'password': password,
                'host': host,
                'port': port,
                'database': database,
                'raise_on_warnings': True,
                'use_pure': False,
                'autocommit': True,
                'pool_size': 5
            }
            connection = mysql.connector.connect(**connection_config_dict)
            thereisone = False
            cursor = connection.cursor()
            empty = self.test_list_is_empty(cursor, 'SELECT  * FROM `manageworkers`.`workers_job`;')
            if empty:
                sql = 'INSERT INTO `manageworkers`.`workers_job` (job_id,name) VALUES (%s,%s);'
                jobs = self.load_jobs_data_from_csv()
                self.insertDataToTable(sql, jobs, cursor, connection)
            empty = self.test_list_is_empty(cursor, 'SELECT  * FROM `manageworkers`.`workers_department`;')
            if empty:
                sql = 'INSERT INTO `manageworkers`.`workers_department` (department_id,name) VALUES (%s,%s);'
                departments = self.load_departments_data_from_csv()
                self.insertDataToTable(sql, departments, cursor, connection)
            empty = self.test_list_is_empty(cursor, 'SELECT  * FROM `manageworkers`.`workers_worker`;')
            if empty:
                worker_list = self.load_workers_data_from_csv()
                self.insert_new_workers(worker_list, cursor, connection)
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print('Exception - ', message)
        finally:
            if connection != '':
                if (connection.is_connected()):
                    connection.close()
                    cursor.close()
                    print("MySQL connection is closed")

    def load_jobs_data_from_csv(self):
        jobs_list = []
        df = pandas.read_csv('jobs.csv', index_col='job_id',
                             parse_dates=['job_id'],
                             header=0,
                             names=['job_id', 'name'])
        for it in df.iterrows():
            j = it[1]
            worker = (int(it[0]), j['name'])
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
                      "hire_date": str(j['hire_date']),
                      "job_id": j['job_id'],
                      "salary": int(j['salary']),
                      "commission_pct": float(j['commission_pct']),
                      "manager_id": int(j['manager_id']),
                      "department_id": int(j['department_id']),
                      "picture": j['picture']
                      }
            worker_list.append(worker)
        return worker_list

    def insertDataToTable(self, sql, worker_list, cursor, connection):
        cursor.executemany(sql, worker_list)
        connection.commit()
    def insertRowToTable(self, sql,cursor, connection,get_last=False):
        try:
            cursor.execute(sql)
            connection.commit()
            if get_last:
                sql = "SELECT LAST_INSERT_ID();"
                cursor.execute(sql)
                record = cursor.fetchone()
                return record[0]
        except Exception as ex:
            return ''

    def test_list_is_empty(self, cursor, sql):
        try:
            cursor.execute(sql)
            records = cursor.fetchall()
            empty = len(records) < 2
            return empty
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print('Exception - ', message)
            return True

    def load_departments_data_from_csv(self):
        departments_list = []
        df = pandas.read_csv('departments.csv', index_col='department_id',
                             parse_dates=['department_id'],
                             header=0,
                             names=['department_id', 'name'])
        for it in df.iterrows():
            j = it[1]
            department = (int(it[0]), j['name'])
            departments_list.append(department)
        return departments_list

    def insert_new_workers(self, worker_list, cursor, connection):


        sql_job = 'INSERT INTO `manageworkers`. `workers_worker_job_id`  (worker_id,job_id) VALUES ({},{});'
        sql = ''' INSERT INTO `manageworkers`.`workers_worker` (`emploee_id`,`first_name`,`last_name`,`email`,`phone_number`,
        `hire_date`, `salary`, `commission_pct`, `manager_id`,`picture`,`department_id_id`)
        VALUES ( {},'{}','{}','{}','{}','{}',{},{},{},'{}',{} ); '''
        # VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
        data = []
        for employee in worker_list:
            temp = str(employee["job_id"])
            jobs = [temp]
            try:
                if temp.index(';') > 0:
                    temp = temp.replace('\"','')
                    jobs = temp.split(';')
            except Exception as ex2:
                jobs = [temp]
                # print('Did not find ;')
            dep_id = self.get_department_id_from_departments(cursor,str(employee["department_id"]))
            sql_inasert = sql.format(employee["emploee_id"],employee["first_name"],employee["last_name"],employee["email"],\
                 employee["phone_number"],employee["hire_date"],employee["salary"],employee["commission_pct"],\
                 employee["manager_id"],employee["picture"],str(dep_id))
            if employee["emploee_id"] == 110:
                print('find 110 find ;')
            id = self.insertRowToTable(sql_inasert, cursor, connection,True)
            for job in jobs:
                jobid = self.get_job_id_from_jobs_by_job_id(job,cursor)
                sql_inasert = sql_job.format(id,jobid)
                self.insertRowToTable(sql_inasert, cursor, connection,False)

    def get_job_id_from_jobs_by_job_id(self, job, cursor):
        sql = 'SELECT id FROM `manageworkers`.`workers_job` where job_id = ' +job+';'
        cursor.execute(sql)
        record = cursor.fetchone()
        return record[0]

    def get_department_id_from_departments(self, cursor, dep_id):
        sql = 'SELECT id FROM `manageworkers`.`workers_department` where department_id = ' +dep_id+';'
        cursor.execute(sql)
        try:
            record = cursor.fetchone()
            return record[0]
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print('Exception - ', message)
            return 0

    def UpdateDataphone(self, host, port, user, password, database):
        connection = ''
        try:
            connection_config_dict = {
                'user': user,
                'password': password,
                'host': host,
                'port': port,
                'database': database,
                'raise_on_warnings': True,
                'use_pure': False,
                'autocommit': True,
                'pool_size': 5
            }
            connection = mysql.connector.connect(**connection_config_dict)
            cursor = connection.cursor()
            cursor.execute('SELECT  * FROM `manageworkers`.`workers_worker`;')
            records = cursor.fetchall()
            for rex in records:
                phone_number = str(rex[5]);
                if not phone_number.startswith('0'):
                    phone_number = '0'+ phone_number
                    sql = 'UPDATE `manageworkers`.`workers_worker` SET phone_number = {}  WHERE `id` = {};'.format(phone_number,rex[0])
                    cursor.execute(sql)
                    connection.commit()

        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print('Exception - ', message)
        finally:
            if connection != '':
                if (connection.is_connected()):
                    connection.close()
                    cursor.close()
                    print("MySQL connection is closed")

    def createDataBaase(self, host, port, user, password, database):
        sql_create_db = "CREATE DATABASE  IF NOT EXISTS "+database + ';'
        try:
            connection_config_dict = {
                'user': user,
                'password': password,
                'host': host,
                'port': port,
                'database': database,
                'raise_on_warnings': True,
                'use_pure': False,
                'autocommit': True,
                'pool_size': 5
            }
            connection = mysql.connector.connect(**connection_config_dict)
            print("MySQL connection is Open")
            cursor = connection.cursor()
            cursor.execute(sql_create_db)
            connection.commit()
            print("We creeate the DB",database)
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print('Exception - ', message)
        finally:
            if connection != '':
                if (connection.is_connected()):
                    connection.close()
                    cursor.close()
                    print("MySQL connection is closed")