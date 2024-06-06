import itertools
import os
import smtplib
import string
from email.message import EmailMessage
from random import random

import xlwt
from django.conf import settings
from django.db.models import Q, Count
from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.decorators.cache import cache_control
from matplotlib import pyplot as plt
import statsmodels.api as sm
from Admin.models import Project, Login, Employee, Team
from Login.views import login
from ProjectManager.models import ProjectTask, Empassign, Projectassigndata

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

import  numpy as np


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
# Create your views here.
def index(request):
    if "loginid" not in request.session:
        return HttpResponse(
            "<script>alert('Authentication Required Please loginfirst');window.location=' ../../Login/login';</script>")
    else:
        emp = None
        username = request.session.get('username')
        loginid = request.session.get('loginid')

        if username and loginid:
            # Check if the Login object exists
            if Login.objects.filter(username=username, loginid=loginid).exists():
                emp = Login.objects.get(username=username, loginid=loginid).empid
        pro = Project.objects.all()
        pcount = pro.count()

        protask = ProjectTask.objects.all()
        ptaskcount = protask.count()
        pending = Project.objects.filter(~Q(status="Completed"))
        pendingcount = pending.count()
        completed = Project.objects.filter(status="Completed")
        completedcount = completed.count()
        labels = []
        data = []

        queryset = Empassign.objects.values('projectid__projectname').annotate(total_students=Count('empassignid'))
        for s in queryset:
            labels.append(s['projectid__projectname'])
            data.append(s['total_students'])

        return render(request, 'Admin/index.html', {
            'labels': labels,
            'data': data, 'emp': emp, 'pcount': pcount, 'pendingcount': pendingcount, 'completedcount': completedcount,
            'ptaskcount': ptaskcount
        })



def addproject(request):
    if request.method == 'POST':
        projectname = request.POST.get('projectname')
        projectdesc = request.POST.get('projectdesc')
        projectcost = request.POST.get('projectcost')
        startingdate = request.POST.get('startingdate')
        enddate = request.POST.get('enddate')

        pro_obj = Project()
        if Project.objects.filter(projectname=projectname).exists():
            return HttpResponse("<script>alert('Duplicate..');window.location ='/Admin/addproject';</script>")
        pro_obj.projectname = projectname
        pro_obj.projectdesc = projectdesc
        pro_obj.projectcost = projectcost
        pro_obj.startingdate = startingdate
        pro_obj.enddate = enddate
        pro_obj.status="Pending"
        pro_obj.save()
        return HttpResponse("<script>alert('Inserted..');window.location ='/Admin/addproject';</script>")
    else:
        emp = None
        username = request.session.get('username')
        loginid = request.session.get('loginid')

        if username and loginid:
            # Check if the Login object exists
            if Login.objects.filter(username=username, loginid=loginid).exists():
                emp = Login.objects.get(username=username, loginid=loginid).empid
        return render(request, "Admin/addproject.html", {'emp': emp})


def viewprojects(request):
    emp = None
    username = request.session.get('username')
    loginid = request.session.get('loginid')

    if username and loginid:
        # Check if the Login object exists
        if Login.objects.filter(username=username, loginid=loginid).exists():
            emp = Login.objects.get(username=username, loginid=loginid).empid
    pro_obj = Project.objects.all()
    return render(request, "Admin/viewprojects.html", {'pro_obj': pro_obj, 'emp': emp})


def addemployee(request):
    ecode = request.POST.get('empcode')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('phone')

        role = request.POST.get('role')
        name = request.POST.get('empname')

        if Login.objects.filter(username=email).exists():
            return HttpResponse(
                "<script>alert('email/user already exist');window.location='/Admin/addemployee';</script>")

        emp_obj = Employee()

        emp_obj.empname = request.POST.get('empname')
        emp_obj.empcode = ecode
        emp_obj.role = request.POST.get('role')
        emp_obj.email = request.POST.get('email')
        emp_obj.phone = request.POST.get('phone')
        emp_obj.photo = request.FILES.get('empphoto')
        emp_obj.status = "Available"




        emp_obj.save()

        loginobj = Login()
        loginobj.username = email
        emp_obj = Employee.objects.last()
        loginobj.empid = emp_obj
        loginobj.password = password
        loginobj.role = role
        loginobj.save()

        msg = EmailMessage()
        msg.set_content(f"Dear {name}, Employee Code : {ecode} Your Username : {email} "
                        f"and password is : {password}, Please use these credentials to login to LOG-X "
                        "and change the username and password ASAP.")
        msg['Subject'] = "Username and Password"
        msg['from'] = 'thomasamal61@gmail.com'
        msg['To'] = {email}
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login('thomasamal61@gmail.com', 'xkvx zaja bbwh nipr')
            smtp.send_message(msg)
        return HttpResponse("<script>alert('Employee Registered & Email "
                            "send');window.location='/Admin/addemployee';</script>")
    else:
        emp = None
        username = request.session.get('username')
        loginid = request.session.get('loginid')

        if username and loginid:
            # Check if the Login object exists
            if Login.objects.filter(username=username, loginid=loginid).exists():
                emp = Login.objects.get(username=username, loginid=loginid).empid
        teams = Team.objects.all()
        pro = Project.objects.all()
        return render(request, 'Admin/addemployee.html', {'teams': teams, 'emp': emp,'pro':pro})


def viewemployee(request):
    emp = None
    username = request.session.get('username')
    loginid = request.session.get('loginid')

    if username and loginid:
        # Check if the Login object exists
        if Login.objects.filter(username=username, loginid=loginid).exists():
            emp = Login.objects.get(username=username, loginid=loginid).empid
    emp_obj = Employee.objects.filter(~Q(role="Admin"))
    return render(request, "Admin/viewemployee.html", {'emp_obj': emp_obj, 'emp': emp})


def editproject(request, id):
    if request.method == 'POST':
        projectname = request.POST.get('projectname')
        projectdesc = request.POST.get('projectdesc')
        projectdate = request.POST.get('projectdate')
        projectcost = request.POST.get('projectcost')
        startingdate = request.POST.get('startingdate')
        enddate = request.POST.get('enddate')
        p_obj = Project.objects.get(projectid=id)
        p_obj.projectname = projectname
        p_obj.projectdesc = projectdesc
        p_obj.projectcost = projectcost
        p_obj.startingdate = startingdate
        p_obj.enddate = enddate
        p_obj.save()
        return viewprojects(request)
    pro = Project.objects.get(projectid=id)
    return render(request, "Admin/editproject.html", {'pro': pro})


def editemployee(request, id):
    if request.method == 'POST':
        empname = request.POST.get('empname')
        empcode = request.POST.get('empcode')
        role = request.POST.get('role')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        emp_obj = Employee.objects.get(empid=id)
        emp_obj.empname = empname
        emp_obj.empcode = empcode
        emp_obj.role = role
        emp_obj.email = email
        emp_obj.phone = phone
        emp_obj.save()
        loginobj = Login.objects.last()

        emp_obj = Employee.objects.last()
        loginobj.username = email
        loginobj.empid = emp_obj
        loginobj.password = phone
        loginobj.role = role
        loginobj.save()
        return viewemployee(request)
    emp = None
    username = request.session.get('username')
    loginid = request.session.get('loginid')

    if username and loginid:
        # Check if the Login object exists
        if Login.objects.filter(username=username, loginid=loginid).exists():
            emp = Login.objects.get(username=username, loginid=loginid).empid
    e = Employee.objects.get(empid=id)
    return render(request, "Admin/editemployee.html", {'e': e, 'emp': emp})


def deleteemployee(request, id):
    emp = Employee.objects.get(empid=id)
    emp.delete()
    return viewemployee(request)


def deleteproject(request, id):
    p = Project.objects.get(projectid=id)
    p.delete()
    return viewprojects(request)


def logout(request):
    if "loginid" in request.session:
        del request.session["loginid"]
        del request.session['username']
        return redirect('../../Login/login')

    # request.session.flush()
    # return login(request)


def viewprojectstatus(request):
    emp = None
    username = request.session.get('username')
    loginid = request.session.get('loginid')

    if username and loginid:
        # Check if the Login object exists
        if Login.objects.filter(username=username, loginid=loginid).exists():
            emp = Login.objects.get(username=username, loginid=loginid).empid
    pro = Project.objects.all()
    return render(request, "Admin/viewprojectstatus.html", {'pro': pro, 'emp': emp})


def projectassign(request):
    emp = None
    username = request.session.get('username')
    loginid = request.session.get('loginid')

    if username and loginid:
        # Check if the Login object exists
        if Login.objects.filter(username=username, loginid=loginid).exists():
            emp = Login.objects.get(username=username, loginid=loginid).empid
    if "loginid" not in request.session:
        return HttpResponse(
            "<script>alert('Authentication Required Please loginfirst');window.location=' ../../Login/login';</script>")
    if request.method == 'POST':
        empid = request.POST.get('employee')
        projectid = request.POST.get('project')
        ea = Employee.objects.get(empid=empid)
        pob = Project.objects.get(projectid=projectid)


        pdata = Projectassigndata()
        eob=Employee.objects.get(empid=empid)
        pdata.empid=eob
        pdata.projectid=Project.objects.get(projectid=eob.projectid_id)
        pdata.status=pob.status
        pdata.save()
        ea.projectid = pob
        ea.save()

        return HttpResponse("<script>alert('Inserted..');window.location ='/Admin/projectassign/';</script>")

    proj = Employee.objects.select_related('projectid').values('projectid_id').exclude(projectid_id=None).distinct()
    proj=Project.objects.exclude(projectid__in=proj)

    emp1 = Employee.objects.filter(role='Project Manager')
    return render(request, "Admin/projectassign.html", {'proj': proj, 'emp1': emp1, 'emp': emp})


def projectassignview(request):
    emp = None
    username = request.session.get('username')
    loginid = request.session.get('loginid')

    if username and loginid:
        # Check if the Login object exists
        if Login.objects.filter(username=username, loginid=loginid).exists():
            emp = Login.objects.get(username=username, loginid=loginid).empid

    emp1 = Employee.objects.filter(role='Project Manager')

    return render(request, "Admin/projectassignview.html", {'emp': emp, 'emp1': emp1})
def yearlyreport(request):
    emp = None
    username = request.session.get('username')
    loginid = request.session.get('loginid')

    if username and loginid:
        # Check if the Login object exists
        if Login.objects.filter(username=username, loginid=loginid).exists():
            emp = Login.objects.get(username=username, loginid=loginid).empid
    return render(request,"Admin/yearlyreport.html",{'emp':emp})



class ExportExcelYear(View):
    def post(self, request):
        fdate=request.POST.get('fdate')
        tdate=request.POST.get('tdate')
        #return HttpResponse(fdate)
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="projectdetails.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Sheet1')

        # Define the column headings
        row_num = 0
        columns = ['Project Name', 'Status','Due Date','Project Task']
        for col_num, column_title in enumerate(columns):
            ws.write(row_num, col_num, column_title)

        # Query the data from your model, and write it to the worksheet
        details = Empassign.objects.filter(assigndate__range=(fdate, tdate),rstatus="Confirmed").values_list('projectid__projectname','status','duedate','projecttaskid__description')


        # Calculate total quantity for each product within the date range
        for row in details:
            row_num += 1
            for col_num,cell_value in enumerate(row):
                ws.write(row_num, col_num, cell_value)

        wb.save(response)
        return response

def empreport(request):
    emp = None
    username = request.session.get('username')
    loginid = request.session.get('loginid')

    if username and loginid:
        # Check if the Login object exists
        if Login.objects.filter(username=username, loginid=loginid).exists():
            emp = Login.objects.get(username=username, loginid=loginid).empid
    emp_obj = Employee.objects.filter(~Q(role="Admin"))

    return render(request,"Admin/empreport.html",{'emp_obj':emp_obj,'emp':emp})

class ExportExcelEmp(View):
    def post(self, request):


        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="employeedetails.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Sheet1')

        # Define the column headings
        row_num = 0
        columns = ['Employee Name', 'Emp Code','Role', 'Email', 'Phone', 'Team']
        for col_num, column_title in enumerate(columns):
            ws.write(row_num, col_num, column_title)

        # Query the data from your model, and write it to the worksheet
        details = Employee.objects.filter(~Q(role="Admin")).values_list('empname', 'empcode', 'role', 'email','phone','teamid__teamname')

        # Write data to the worksheet
        for row in details:
            row_num += 1
            for col_num, cell_value in enumerate(row):
                ws.write(row_num, col_num, cell_value)

        wb.save(response)
        return response

def sortempreport(request):
    emp = None
    username = request.session.get('username')
    loginid = request.session.get('loginid')

    if username and loginid:
        # Check if the Login object exists
        if Login.objects.filter(username=username, loginid=loginid).exists():
            emp = Login.objects.get(username=username, loginid=loginid).empid
    return render(request,"Admin/sortempreport.html",{'emp':emp})



class ExportExcelSortEmp(View):
    def post(self, request):
        role=request.POST.get('role')

        #return HttpResponse(fdate)
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="Empdetails.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Sheet1')

        # Define the column headings
        row_num = 0
        columns = ['Employee Name', 'Emp Code','Email','Phone']
        for col_num, column_title in enumerate(columns):
            ws.write(row_num, col_num, column_title)

        # Query the data from your model, and write it to the worksheet
        details = Employee.objects.filter(role=role).values_list('empname','empcode','email','phone')


        # Calculate total quantity for each product within the date range
        for row in details:
            row_num += 1
            for col_num,cell_value in enumerate(row):
                ws.write(row_num, col_num, cell_value)

        wb.save(response)
        return response

def fillemp(request):
    did = request.POST.get("did")

    # Retrieve employee data based on role
    employee_data = Employee.objects.filter(role=did).values()

    response_data = {
        'employee_data': list(employee_data),
    }

    return JsonResponse(response_data)
def fillprodata(request):
    fdate = request.POST.get('fdate')
    tdate = request.POST.get('tdate')

    # Retrieve project data based on date range and status
    details = Empassign.objects.filter(assigndate__range=(fdate, tdate), rstatus="Confirmed").values_list(
        'projectid__projectname', 'status', 'duedate', 'projecttaskid__description')

    response_data = {
        'project_data': list(details),
    }

    return JsonResponse(response_data)

def predictionspage(request):
    return render(request, "Admin/predictions.html")



def prediction(request):
    csv_file_path = os.path.join(settings.BASE_DIR, 'static', 'project_dataset.xlsx')
    furniture = pd.read_excel(csv_file_path)
    # furniture = df.loc[df['Category'] == 'Furniture']
    furniture = furniture[pd.to_datetime(furniture['Date'], errors='coerce').notna()]

    # Preprocess the dataset
    furniture['Date'] = pd.to_datetime(furniture['Date'])
    furniture = furniture.sort_values('Date')
    furniture = furniture.groupby('Date')['revenue'].sum().reset_index()
    furniture = furniture.set_index('Date')
    # furniture.index
    y = furniture['revenue'].resample('MS').mean()
    # print(y['2017':])
    #y.plot(figsize=(15, 6))
    #plt.show()

    p = d = q = range(0, 2)
    pdq = list(itertools.product(p, d, q))
    seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]

    for param in pdq:
        for param_seasonal in seasonal_pdq:
            try:
                mod = sm.tsa.statespace.SARIMAX(y,
                                                order=param,
                                                seasonal_order=param_seasonal,
                                                enforce_stationarity=False,
                                                enforce_invertibility=False)
                results = mod.fit()
                # print('ARIMA{}x{}12 - AIC:{}'.format(param, param_seasonal, results.aic))
            except:
                continue

    pred_uc = results.get_forecast(steps=36)
    pred_ci = pred_uc.conf_int()
    ax = y.plot(label='observed', figsize=(14, 4))
    pred_uc.predicted_mean.plot(ax=ax, label='Forecast')
    ax.fill_between(pred_ci.index,
                    pred_ci.iloc[:, 0],
                    pred_ci.iloc[:, 1], color='k', alpha=.25)
    ax.set_xlabel('Date')
    ax.set_ylabel('revenue')
    plt.legend()
    # plt.yticks(ticks=range(0, int(y.max()) + 10000, 10000))

    plt.show()
    return render(request, "Admin/predictions.html")
