from ManageDB.MngMongoDb import ManageDB
from ManageDB.MngMysqlDB import MngMysqlDB
from optparse import OptionParser
from IniFile import IniFile
import os
import sys
def main(options, args):
    ininame = os.getcwd() + '\\database.ini'
    host = 'localhost: 27017'
    if os.path.exists(ininame):
        ini = IniFile(ininame)

        # mongohost = ini._ReadString('General','MongooDB conection string','')
        # if mongohost == '':
        #     ini._WriteString('General', 'MongooDB conection string', mongohost)

        # mysqlhost = ini._ReadString('General', 'MysqlDB conection string', '')
        # if mysqlhost == '':
        #     mysqlhost = '\'localhost\', port=\'3306\', database=\'ManageWorkers\', user=\'root\', password=\'baBs5508179\''
        #     ini._WriteString('General', 'MysqlDB conection string', mysqlhost)
        mysqlhost = ini._ReadString('General', 'MysqlDB host', '')
        if mysqlhost == '':
            mysqlhost = 'localhost'
            ini._WriteString('General', 'MysqlDB host', mysqlhost)
        port = ini._ReadString('General', 'MysqlDB port', '')
        if port == '':
            port = '3306'
            ini._WriteString('General', 'MysqlDB port', port)

        user = ini._ReadString('General', 'MysqlDB user', '')
        if user == '':
            user = 'root'
            ini._WriteString('General', 'MysqlDB user', port)

        password = ini._ReadString('General', 'MysqlDB password', '')
        if password == '':
            password = 'baBs5508179'
            ini._WriteString('General', 'MysqlDB password', password)

        database = ini._ReadString('General', 'MysqlDB database', '')
        if port == '':
            database = 'ManageWorkers'
            ini._WriteString('General', 'MysqlDB database', database)
    # mngdb = ManageDB()
    mngdb = MngMysqlDB()
    mngdb.UpdateDataBase(mysqlhost,port,user,password,database)
    # mngdb.UpdateDataphone(mysqlhost, port, user, password, database)



if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-f", "--file",
                      dest="datafaile",
                      help="An csv file to load data",
                      metavar="FILE")
    (options, args) = parser.parse_args()
    parser = None
    main(options, args)

