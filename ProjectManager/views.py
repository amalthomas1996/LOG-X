import smtplib
from email.message import EmailMessage

import xlwt
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.db.models import Q
from django.views import View

from Admin.models import Team, Project, Activity, Employee, Login
from Login.views import login
from ProjectManager.models import ProjectTask, Empassign, Projectassigndata
from django.views.decorators.cache import cache_control
@cache_control(no_cache=True, must_revalidate=True, no_store=True)

# Create your views here.
def pmindex(request):
    if "loginid" not in request.session:
        return HttpResponse("<script>alert('Authentication Required Please loginfirst');window.location=' ../../Login/login';</script>")
    else:
        emp = None
        username = request.session.get('username')
        loginid = request.session.get('loginid')

        if username and loginid:
            # Check if the Login object exists
            if Login.objects.filter(username=username, loginid=loginid).exists():
                emp = Login.objects.get(username=username, loginid=loginid).empid.empid
                e=Employee.objects.get(empid=emp)



        return render(request,"ProjectManager/index.html",{'data':e,'emp':e})

def addteam(request):
    if "loginid" not in request.session:
        return HttpResponse("<script>alert('Authentication Required Please loginfirst');window.location=' ../../Login/login';</script>")
    if request.method == 'POST':
        teamname = request.POST.get('teamname')
        description = request.POST.get('description')
        projectid = request.POST.get('project')

        t_obj = Team()
        if Team.objects.filter(teamname=teamname).exists():
            return HttpResponse("<script>alert('Duplicate..');window.location ='/ProjectManager/addteam/';</script>")
        t_obj.teamname = teamname
        t_obj.description = description
        t_obj.projectid = Project.objects.get(projectid=projectid)


        t_obj.save()
        return HttpResponse("<script>alert('Inserted..');window.location ='/ProjectManager/addteam/';</script>")
    else:
        username = request.session.get('username')
        loginid = request.session.get('loginid')

        if username and loginid:
            # Check if the Login object exists
            if Login.objects.filter(username=username, loginid=loginid).exists():
                emp = Login.objects.get(username=username, loginid=loginid).empid
        pro = Project.objects.all()
        return render(request, "ProjectManager/addteam.html",{'pro':pro,'emp':emp})

def viewteam(request):
    if "loginid" not in request.session:
        return HttpResponse("<script>alert('Authentication Required Please loginfirst');window.location=' ../../Login/login';</script>")
    username = request.session.get('username')
    loginid = request.session.get('loginid')

    if username and loginid:
        # Check if the Login object exists
        if Login.objects.filter(username=username, loginid=loginid).exists():
            emp = Login.objects.get(username=username, loginid=loginid).empid
    t_obj=Team.objects.all()
    return render(request,"ProjectManager/viewteam.html",{'t_obj':t_obj,'emp':emp})

def editteam(request,id):
    if "loginid" not in request.session:
        return HttpResponse("<script>alert('Authentication Required Please loginfirst');window.location=' ../../Login/login';</script>")
    if request.method == 'POST':
        teamname = request.POST.get('teamname')
        description = request.POST.get('description')
        project = request.POST.get('project')
        t_obj=Team.objects.get(teamid=id)
        t_obj.teamname = teamname
        t_obj.description = description
        t_obj.projectid=Project.objects.get(projectid=project)

        t_obj.save()
        return viewteam(request)
    te = Team.objects.get(teamid=id)
    pro = Project.objects.all()
    username = request.session.get('username')
    loginid = request.session.get('loginid')

    if username and loginid:
        # Check if the Login object exists
        if Login.objects.filter(username=username, loginid=loginid).exists():
            emp = Login.objects.get(username=username, loginid=loginid).empid

    return render(request, "ProjectManager/editteam.html", {'te': te,'pro':pro,'emp':emp})

def deleteteam(request,id):
    team = Team.objects.get(teamid=id)
    team.delete()
    return viewteam(request)

def addprojecttask(request):
    if "loginid" not in request.session:
        return HttpResponse("<script>alert('Authentication Required Please loginfirst');window.location=' ../../Login/login';</script>")
    if request.method == 'POST':
        activityid = request.POST.get('projectactivity')
        projectid = request.POST.get('project')
        description = request.POST.get('description')

        startingdate = request.POST.get('startingdate')
        enddate = request.POST.get('enddate')
        status = request.POST.get('status')


        pt_obj = ProjectTask()
        pt_obj.activityid = Activity.objects.get(activityid=activityid)
        pt_obj.projectid = Project.objects.get(projectid=projectid)
        pt_obj.description = description
        pt_obj.startingdate = startingdate
        pt_obj.enddate = enddate
        pt_obj.status = status
        pt_obj.save()
        return HttpResponse("<script>alert('Inserted..');window.location ='/ProjectManager/addprojecttask/';</script>")
    else:
        username = request.session.get('username')
        loginid = request.session.get('loginid')

        if username and loginid:
            # Check if the Login object exists
            if Login.objects.filter(username=username, loginid=loginid).exists():
                emp = Login.objects.get(username=username, loginid=loginid).empid
        empdata = Login.objects.filter(loginid=loginid)
        pro = Project.objects.filter()
        act=Activity.objects.all()
        return render(request, "ProjectManager/addprojecttask.html",{'pro':pro,'act':act,'emp':emp,'empdata':empdata})

def viewprojecttask(request):
    if "loginid" not in request.session:
        return HttpResponse("<script>alert('Authentication Required Please loginfirst');window.location=' ../../Login/login';</script>")
    username = request.session.get('username')
    loginid = request.session.get('loginid')

    if username and loginid:
        # Check if the Login object exists
        if Login.objects.filter(username=username, loginid=loginid).exists():
            emp = Login.objects.get(username=username, loginid=loginid).empid
    protask=ProjectTask.objects.all()
    return render(request,"ProjectManager/viewprojecttask.html",{'protask':protask,'emp':emp})

def editprojecttask(request,id):
    if "loginid" not in request.session:
        return HttpResponse("<script>alert('Authentication Required Please loginfirst');window.location=' ../../Login/login';</script>")
    if request.method == 'POST':
        activityid = request.POST.get('projectactivity')
        projectid = request.POST.get('project')
        description = request.POST.get('description')
        startingdate = request.POST.get('startingdate')
        enddate = request.POST.get('enddate')
        status = request.POST.get('status')

        pt_obj = ProjectTask.objects.get(projecttaskid=id)
        pt_obj.activityid = Activity.objects.get(activityid=activityid)
        pt_obj.projectid = Project.objects.get(projectid=projectid)
        pt_obj.description = description
        pt_obj.startingdate = startingdate
        pt_obj.enddate = enddate
        pt_obj.status = status
        pt_obj.save()
        return HttpResponse("<script>alert('Inserted..');window.location ='/ProjectManager/viewprojecttask/';</script>")
    else:
        protask =ProjectTask.objects.get(projecttaskid=id)
        pro = Project.objects.all()
        act = Activity.objects.all()
        username = request.session.get('username')
        loginid = request.session.get('loginid')

        if username and loginid:
            # Check if the Login object exists
            if Login.objects.filter(username=username, loginid=loginid).exists():
                emp = Login.objects.get(username=username, loginid=loginid).empid
        return render(request, "ProjectManager/editprojecttask.html", {'protask': protask, 'act': act,'pro':pro,'emp':emp})

def deleteprojecttask(request,id):
    protask = ProjectTask.objects.get(projecttaskid=id)
    protask.delete()
    return viewprojecttask(request)

def empassign(request):
    if "loginid" not in request.session:
        return HttpResponse("<script>alert('Authentication Required Please loginfirst');window.location=' ../../Login/login';</script>")
    if request.method == 'POST':

        projecttaskid = request.POST.get('projecttask')
        empid = request.POST.get('employee')
        projectid=request.POST.get('project')
        duedate = request.POST.get('duedate')
        team=request.POST.get('teamid')
        status = "none"

        ea = Empassign()
        ea.projecttaskid = ProjectTask.objects.get(projecttaskid=projecttaskid)
        ea.empid = Employee.objects.get(empid=empid)

        ea.duedate = duedate
        ea.status = status
        ea.projectid=Project.objects.get(projectid=projectid)
        ea.rstatus='none'
        ea.save()
        emp = Employee.objects.get(empid=empid)
        emp.projectid = Project.objects.get(projectid=projectid)
        emp.teamid = Team.objects.get(teamid=team)
        emp.save()
        return HttpResponse("<script>alert('Inserted..');window.location ='/ProjectManager/empassign/';</script>")
    else:
        username = request.session.get('username')
        loginid = request.session.get('loginid')

        if username and loginid:
            # Check if the Login object exists
            if Login.objects.filter(username=username, loginid=loginid).exists():
                emp = Login.objects.get(username=username, loginid=loginid).empid

       # pro = ProjectTask.objects.all()
        e = Employee.objects.filter(role='employee').exclude(empid__in=Empassign.objects.filter(~Q(status="Completed")).values('empid') )

        emp1 = Employee.objects.filter(role='Employee')
        proj = Login.objects.filter(loginid=request.session['loginid']).values('empid__projectid__projectname',
                                                                               'empid__projectid__projectid')
        team = Team.objects.all()
        for p in proj:
            pro = ProjectTask.objects.filter(projectid=p['empid__projectid__projectid'])
        return render(request, "ProjectManager/empassign.html",
                      {'pro': pro, 'emp1': emp1, 'proj': proj, 'emp': emp, 'team': team})


def viewempassign(request):
    if "loginid" not in request.session:
        return HttpResponse("<script>alert('Authentication Required Please loginfirst');window.location=' ../../Login/login';</script>")
    username = request.session.get('username')
    loginid = request.session.get('loginid')

    if username and loginid:
        # Check if the Login object exists
        if Login.objects.filter(username=username, loginid=loginid).exists():
            emp = Login.objects.get(username=username, loginid=loginid).empid
    pro = Login.objects.filter(loginid=request.session['loginid']).values('empid__projectid__projectname','empid__projectid__projectid','empid__empid')
    for p in pro:
        #return HttpResponse(p['empid__empid'])
        pdata=Projectassigndata.objects.filter(empid=p['empid__empid'])

    #return HttpResponse(pro)
    empassign=Empassign.objects.all()
    return render(request,"ProjectManager/viewempassign.html",{'empassign':empassign,'pro':pro,'emp':emp,'pdata':pdata})


def filldata(request):
    did = request.POST.get("did")

    # Retrieve data
    project_data = Project.objects.filter(projectid=did).values()
    emp_assign_data = Empassign.objects.filter(projectid=did).values()
    employee_data = Employee.objects.filter(empassign__projectid=did).values()

    response_data = {
        'project_data': list(project_data),
        'emp_assign_data': list(emp_assign_data),
        'employee_data': list(employee_data),
    }

    # Get all project task IDs for the given project ID
    project_task_ids = [assignment['projecttaskid_id'] for assignment in response_data['emp_assign_data']]

    # Retrieve activity names for all project tasks
    project_task_activity_mapping = {
        task_id: Activity.objects.filter(projecttask__projecttaskid=task_id).values_list('activityname', flat=True).first()
        for task_id in project_task_ids
    }

    # Update emp_assign_data with activity names
    for assignment in response_data['emp_assign_data']:
        project_task_id = assignment.get('projecttaskid_id')
        if project_task_id in project_task_activity_mapping:
            assignment['activityname'] = project_task_activity_mapping[project_task_id]
        else:
            assignment['activityname'] = '-'

    return JsonResponse(response_data)

def deleteempassign(request,id):
    empass = Empassign.objects.get(empassignid=id)
    empass.delete()
    return viewempassign(request)

def confirm(request,id):

    empass = Empassign.objects.get(empassignid=id)
    empass.rstatus = 'Confirmed'

    empass.save()
    projecttaskcount=Empassign.objects.filter(projectid_id=empass.projectid_id).count()
    projectstatuscount=Empassign.objects.filter(status="Completed",projectid_id=empass.projectid_id).count()
    #return HttpResponse(str(projecttaskcount)+" "+str(projectstatuscount))
    if projecttaskcount == projectstatuscount:
        pob=Project.objects.get(projectid=empass.projectid_id)
        pdata=Projectassigndata.objects.get(projectid=empass.projectid_id)
        pob.status="Completed"
        pdata.status="Completed"
        pob.save()
        pdata.save()
    return viewempassign(request)
def reject(request,id):
    empass = Empassign.objects.get(empassignid=id)
    empass.rstatus = 'Rejected'
    empass.save()
    return viewempassign(request)

def viewprofilepm(request):

    if "loginid" not in request.session:
        return HttpResponse("<script>alert('Authentication Required Please login first');window.location=' ../../Login/login';</script>")
    username = request.session.get('username')
    loginid = request.session.get('loginid')

    if username and loginid:
        # Check if the Login object exists
        if Login.objects.filter(username=username, loginid=loginid).exists():
            emp = Login.objects.get(username=username, loginid=loginid).empid
    return render(request, "ProjectManager/viewprofilepm.html",{'emp':emp})

def logout(request):
    request.session.flush()
    return login(request)

def cup(request):
    if request.method == 'POST':

        username = request.session.get('username')
        loginid = request.session.get('loginid')

        cusername = request.POST.get('cusername')
        nusername = request.POST.get('nusername')
        cpassword = request.POST.get('cpassword')
        npassword = request.POST.get('newpassword')
        repassword = request.POST.get('repassword')

        if username and cpassword:
            if cusername == username:
                if npassword == repassword:
                    login_obj = Login.objects.filter(username=username, password=cpassword).first()
                    if login_obj:
                        login_obj.username = nusername
                        login_obj.password = npassword
                        login_obj.save()

                        return render(request, "Login/index.html")
                    else:
                        return render(request, "ProjectManager/cup.html", {'error': 'Invalid credentials'})
                else:
                    return render(request, "ProjectManager/cup.html", {'error': 'New passwords do not match'})
            else:
                return render(request, "ProjectManager/cup.html",
                              {'error': 'Current username does not match session'})
        else:
            return render(request, "ProjectManager/cup.html", {'error': 'Session data missing'})

    return render(request, "ProjectManager/cup.html")


def sendmail(request,id):
    if request.method == 'POST':
        projectname= request.POST.get("projectname")
        projecttask= request.POST.get("projecttask")
        duedate= request.POST.get("duedate")
        message= request.POST.get("message")
        empid = request.POST.get("empid")
        emp = Employee.objects.get(empid=empid)
        email=emp.email
        if Employee.objects.filter(email=email).exists():

            msg = EmailMessage()
            msg.set_content(f"PROJECT NAME: {projectname}\n"
                            f"PROJECT TASK: {projecttask}\n"
                            f"DUE DATE: {duedate}\n"
                            f"MESSAGE: {message}\n")
            msg['Subject'] = "Due Date is Over"
            msg['From'] = 'thomasamal61@gmail.com'
            msg['To'] = email
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login('thomasamal61@gmail.com', 'xkvx zaja bbwh nipr')
                smtp.send_message(msg)
            return HttpResponse("<script>alert('Mail Send Successfully');window.location='/ProjectManager/viewempassign/';</script>")
        else:
            context = {"error": "ERROR"}
            return render(request, "ProjectManager/viewempassign.html", context)
    else:

        ea = Empassign.objects.get(empassignid=id)
        return render(request, "ProjectManager/sendmail.html",{'ea':ea})

def prststus(request):
    return render(request,"ProjectManager/prststus.html")



class ExportExcelpr(View):
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