Django-ManageWorkers  Building REST-API & Web Site that use the REST-API
=========================================

This Project is in Course Python in DevOpsExprts https://devopsexperts.co.il/%d7%a7%d7%95%d7%a8%d7%a1-%d7%a4%d7%99%d7%99%d7%aa%d7%95%d7%9f/

How to use it
-------------

In the toplevel directory of the project there is a requirements.txt file with all the python dependencies, required for this project to run. Install them with

`pip install -r requirements.txt`

You'll also need a working instance of MySql - install it as an apt package in your system with:

Update the file database.ini with your MySql parameters

MysqlDB host=localhost
MysqlDB port=3306
MysqlDB user=root
MysqlDB password=baBs5508179
MysqlDB database=ManageWorkers

also update ManageWorkers\api_workers\api_workers\settings.py  - change user and password
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ManageWorkers',
        'USER' : 'root',
        'PASSWORD' : 'baBs5508179',
        'HOST' : '127.0.0.1',
        'PORT' : '3306',
        'default-character-set' : 'utf8',
    }
}

After that you'll need to create a database in MySql caled manageworkers, 

run the class 'python createManageworkersDataBase.py' in the root of the project

if there are problems there is a backup of all database in directory backupmysql

run the commands

'cd api_workers'
`python manage.py makemigrations'
`python manage.py migrate' 
'python manage.py createsuperuser'

'cd ..'
to update new workers in Data Base run the file
run the class 'python updateDataBase.p' in the root of the project

'cd api_workers'
`python manage.py runserver`

and visit http://localhost:8000/api/ url, where you'll find the root of your REST api.


Project structure
-----------------

The toplevel directory contains a single django project, called, `api_workers`. Within it there are a per-project folder called `api_workers`,
In this  
where global settings are stored, and three django ,
The first `accounts` contains the user model.
The second application is `workers` and this is for the rest-api application
The third applications `HumanResource` this is WebSite that use The Rest-Api  

There are 3 Api 

    "jobs": "http://127.0.0.1:8000/jobs/",
    "workers": "http://127.0.0.1:8000/workers/",
    "departments": "http://127.0.0.1:8000/departments/"
	
To call the Web Site you have to call 

http://127.0.0.1:8000/HumanResource/
