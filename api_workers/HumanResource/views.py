from django.shortcuts import render,redirect
# from ..workers.models import Job,Department,Worker
from .models import Job,Worker,Department
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.db.models import Q
from django.contrib.auth.models import User, auth
import math
import requests
import json
from datetime import date


headers = {
  'Authorization': 'Basic YmFydWNoOjU1MDgxNzk=',
  'Content-Type': 'application/json'
}
url_jobs = "http://127.0.0.1:8000/jobs/"
url_workers = "http://127.0.0.1:8000/workers/"
url_departments = "http://127.0.0.1:8000/departments/"
@csrf_protect
def index(request):
    data = {}
    if request.user.is_authenticated:
        data = {'username': request.user.get_username()}
    if request.method == 'GET':
        title = request.GET.get('title')
        if title:
            return render(request, 'HumanResource/search/?q=' + title)
    showuserspictures = True
    data['showuserspictures'] = showuserspictures
    return render(request, 'base.html', data)

def get_employees_under_me(id,workers):
    employees = []
    for worker in workers:
        if str(worker.manager_id) == str(id):
            employees.append(worker)
    return employees


def worker_detail(request):
    # http://127.0.0.1:8000/HumanResource/worker_detail/?id=103
    id = 1
    if request.method == 'GET':
        id = int(request.GET.get('id'))
    try:
        try:
            allworkers, departments_names, departments = get_Workers(0,request)
            workers,department = get_workersbyquery(id,allworkers)
            worker = workers[0]
            employees = get_employees_under_me(id,allworkers)
            worker.emploee_json = buildjsonfromworker(worker, request)
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)

            print('Exception in worker_detail',message)
            worker = None
        if worker:
            data = {'worker': worker,'employees':employees}
            data['workers_in_line'] = 6
            return render(request, "HumanResource/worker_detail.html",data)
        else:
            return render(request, "HumanResource/404.html")
    except:
        return render(request, "HumanResource/404.html")


def redirect_to_workers_list(request,page, workers, department, departments_names):
    if page is None:
        page = 1
    if department is None:
        department = 0

    workers_in_line = 6
    page = int(page)
   # print('Total Movies - ', len(objects))
    count_in_page = 10 * workers_in_line
    # print('count_in_page - ', count_in_page)
    total_page = int(math.ceil(len(workers) / count_in_page))
    if page > total_page:
        return render(request, "HumanResource/404.html")
    # print('total_page - ', total_page)
    last_item_index = count_in_page * page if page != total_page else len(workers)
    pages = []
    end_distance = total_page - page
    start_page_num = page - 5 if end_distance >= 5 else page - count_in_page + end_distance
    end_page_num = page + 5 if page > 5 else count_in_page
    for i in range(start_page_num, end_page_num + 1):
        if 1 <= i <= total_page:
            pages.append(i)
    data = {'items': workers[count_in_page * (page - 1):last_item_index], 'current_page': page,
            'page_number': total_page,
            'pages': pages, 'workers_in_line': workers_in_line}
    data['departments'] = departments_names
    data['department'] = department
    return render(request, "HumanResource/workers_list.html", data)


def workers_list(request):
    page = 1
    if request.method == 'GET':
        page = request.GET.get('page')
        department = request.GET.get('department')
        # There is a problem with R&D - Django looks as it is new paramater
        if str(department).upper() == 'R':
            department = 'R&D'
        title = request.GET.get('title')
    if page is None:
        page = 1
    if department is None:
        department = 0
    showuserspictures = True
    page = int(page)
    workers,departments_names,departments = get_Workers(department,request)
    # print( 'workers',len(workers))
    if len(workers) == 0:
        return redirect('/HumanResource/',{'showuserspictures':showuserspictures})
    return redirect_to_workers_list(request, page,workers,department,departments_names)

def get_departments():
    departments = []
    departments_names = []
    new_list = ['ALL']
    payload = {}
    response = requests.request("GET", url_departments, headers=headers, data=payload)
    data = json.loads(response.text.encode('utf8'))
    find_dict = {}
    find_dict["departments"] = data
    for dep in find_dict["departments"]:
        departmnt = Department()
        departmnt.name = dep['name']
        departmnt.department_id = dep['department_id']
        departmnt.url = dep['url']
        departments.append(departmnt)
        if dep['name'] not in departments_names:
            departments_names.append(dep['name'])
    departments_names.sort(reverse = False)
    for s in departments_names:
        new_list.append(s)
    return new_list,departments


def get_jobs():
    jobs = []
    payload = {}
    response = requests.request("GET", url_jobs, headers=headers, data=payload)
    data = json.loads(response.text.encode('utf8'))
    find_dict = {}
    find_dict["jobs"] = data
    for jobdata in find_dict["jobs"]:
        newjob = Job()
        newjob.name = jobdata['name']
        newjob.department_id = jobdata['job_id']
        newjob.url = jobdata['url']
        jobs.append(newjob)
    return jobs


def get_date_from_hire_date(hire_date):
    data = []
    spliter = '/'
    string = str(hire_date).strip()
    try:
        if string.__contains__('00:00:00'):
            if string.index('00:00:00') > 0:
                string = string.split(' ')[0].strip()
    except:
        data = []
    if string.__contains__('-'):
        spliter = '-'
    if string.index(spliter) > 0:
        data = string.split(spliter)
        if len(data[0]) == 4:
            string = '{}/{}/{}'.format(data[2],data[1],data[0])
    return string



def get_Workers(department,req):
    workers = []
    payload = {}
    jobs = get_jobs()
    departments_names, departments = get_departments()
    response = requests.request("GET", url_workers, headers=headers, data=payload)
    data = json.loads(response.text.encode('utf8'))
    find_dict = {}
    find_dict["workers"] = data
    managers = data
    for work in find_dict["workers"]:
        canload = False
        if department == 0 or str(department) == 'ALL' :
            canload = True
        worker = Worker()
        worker.department_id =  work['department_id']
        department_id = worker.department_id
        temp = '/'+ str(department_id) + '/'
        for departmt in departments:
            if departmt.url.endswith(temp):
                if departmt.name.lower() == str(department).lower():
                    canload = True
                worker.department_name = departmt.name
                break
        # go to next worker if it is not in the list of department
        if not canload:
            continue

        worker.emploee_id = work['emploee_id']
        worker.first_name = work['first_name']
        worker.last_name = work['last_name']
        worker.email = work['email']
        worker.hire_date = get_date_from_hire_date(work['hire_date'])
        worker.name =  str(work['first_name']).strip() + ' ' +str(work['last_name']).strip()
        job_id = work['job_id']
        myjobs = []
        for j in  job_id:
            temp = '/' + str(j) + '/'
            for job in jobs:
                if str(job.url).endswith(temp):
                    myjobs.append(job.name)
                    break
        worker.job_id = myjobs
        # We send the salary if only supper user has log in
        if req.user.is_active and req.user.has_perm('poll.change_poll'):
            worker.salary = work['salary']
            worker.commission_pct = work['commission_pct']
        else:
            worker.salary = 0
            worker.commission_pct = 0
        phone = str(work['phone_number'])
        if not phone.startswith('0'):
            phone = '0' + phone

        worker.phone_number = phone

        worker.picture = str(work['picture']).replace('/assets/','/static/')
        worker.manager_name = ''
        worker.manager_id = work['manager_id']
        mngr_id = int(worker.manager_id)
        if mngr_id > 0:
            for manager in  managers:
                empid = manager['emploee_id']
                if str(mngr_id) == str(empid):
                    worker.manager_name = manager['first_name'] + ' ' + manager['last_name']
                    break
        else:
            worker.manager_name = 'Company Manager'
        if canload:
            workers.append(worker)
    # print('workers',workers)
    return workers,departments_names,departments

def get_workersbyquery(lookupsworker,workers):
    department = ''
    workerslist = []
    for worker in workers:
        canload = False
        if type(lookupsworker) == int:
            if worker.emploee_id == lookupsworker:
                canload = True
                # print('Find Match emploee_id', lookupsworker)
                workerslist.append(worker)
                return workerslist, department
        if worker.first_name.lower() == str(lookupsworker).lower():
            canload = True
            # print('Find Match first_name',lookupsworker)
        if worker.last_name.lower() == str(lookupsworker).lower():
            canload = True
        try:
            if (worker.name.lower().index(str(lookupsworker).lower()) > 0):
                canload = True
        except:
            print('')
        if str(worker.department_name).lower() == str(lookupsworker).lower():
            canload = True
            department = worker.department_id
        for job in worker.job_id:
            if job.lower()  == str(lookupsworker).lower():
                canload = True
                break
        if canload:
            print('quary',worker)
            workerslist.append(worker)
    return workerslist,department


def searchworker(request):
    try:
        if request.method == 'GET':
            query= request.GET.get('q')
            try:
                id = int(query)
                query = id
            except:
                id = 0

            # print('query', query)
            submitbutton= request.GET.get('submit')
            allworkers, departments_names, departments = get_Workers(0,request)
            if query is not None:
                workers,department = get_workersbyquery(query,allworkers)
                worker = None
                if workers:
                    # print('len(workers)',len(workers))
                    if len(workers) > 1:
                        return redirect_to_workers_list(request, 1, workers, department, departments_names)
                    else:
                        worker = workers[0]
                        worker.emploee_json = buildjsonfromworker(worker, request)
                        employees = get_employees_under_me(worker.emploee_id, allworkers)
                        data = {'worker': worker, 'employees': employees}
                        data['workers_in_line'] = 6
                        return render(request, "HumanResource/worker_detail.html", data)
                else:
                    return redirect('/HumanResource/workers_list/')
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print('Did not get searchworker', message)
    return render(request, "HumanResource/404.html")


def eror(request):
    return render(request, "HumanResource/404.html")


def test_if_worker_worked_more_then_a_year(hire_date,years):
    data = []
    year = 0
    today = date.today()
    data = hire_date.split('/')
    if len(data) == 3:
        year = data[2]
    if today.year - int(year) >= years:
        return True
    return False

def SalarySummery(request):
    year = 1
    if request.method == 'GET':
        temp = request.GET.get('year')
    if temp:
        year = int(temp)
    data = {}
    allworkers, departments_names, departments = get_Workers(0, request)
    companysize = len(allworkers)
    data['TotalEmployees'] = companysize
    total = 0
    avareg = 0
    employelist = []
    for worker in allworkers:
        total += worker.salary
    avareg = total / companysize
    data['TotalBudget'] =  total
    data['avaregesalary'] = '{0:9.2f}'.format(avareg)
    data['years'] = str(year)
    years = []
    for i in range(1,21):
        years.append(str(i))
    data['yearslist'] = years
    raisetotal = 0;
    for worker in allworkers:
        if test_if_worker_worked_more_then_a_year(worker.hire_date,int(year)) and worker.salary < avareg:
            add = worker.salary * worker.commission_pct
            line = {}
            line['id'] = worker.emploee_id
            line['name'] = worker.name
            line['salary'] = worker.salary
            line['add'] = '{0:9.2f}'.format(add)
            raisetotal += add;
            employelist.append(line)
    data['employelist'] = employelist
    data['raisetotal'] = str(raisetotal)
    return render(request, "HumanResource/employeessalarysummery.html", data)

def buildjsonfromworker(worker,req):
    json_data = {}
    json_data["name"] = worker.name
    json_data["emploee_id"] = str(worker.emploee_id)
    json_data["department_name"] = worker.department_name
    json_data["manager_id"] = str(worker.manager_id)
    json_data["manager_name"] = worker.manager_name
    json_data["email"] = worker.email
    json_data["phone_number"] = worker.phone_number
    json_data["hire_date"] = worker.hire_date
    json_data["job_id"] = str(worker.job_id)
    if req.user.is_active and req.user.has_perm('poll.change_poll'):
        json_data["commission_pct"] = str(worker.commission_pct)
        json_data["salary"] = str(worker.salary)
    find_dict = {}
    find_dict["worker data"] = json_data
    new = json.dumps(find_dict)
    with open('json_data.js', "w") as f:
        json.dump(find_dict, f, indent=2)
    f = open('json_data.js')
    new = f.read()
    return new
