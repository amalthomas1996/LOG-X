import xlwt
from django.http import request
from django.shortcuts import render, redirect ,HttpResponse
from django.db.models import Q
from django.views import View

from Admin.models import Employee, Login
from Login.views import login
from ProjectManager.models import Empassign
from django.views.decorators.cache import cache_control
@cache_control(no_cache=True, must_revalidate=True, no_store=True)



# Create your views here.
def empindex(request):
    if "loginid" not in request.session:
        return HttpResponse("<script>alert('Authentication Required Please loginfirst');window.location=' ../../Login/login';</script>")

    else:
        emp = None
        username = request.session.get('username')
        loginid = request.session.get('loginid')

        if username and loginid:
            # Check if the Login object exists
            if Login.objects.filter(username=username, loginid=loginid).exists():
                emp = Login.objects.get(username=username, loginid=loginid).empid
                emp1 = Empassign.objects.filter(empid=emp)
                emp12 = Empassign.objects.filter(~Q(status="Completed"),empid=emp)
                tcount=emp1.count()
                stauscount=Empassign.objects.filter(~Q(status="Completed"),empid=emp)
                scount=stauscount.count()
                ccount = Empassign.objects.filter(status="Completed", empid=emp)
                comcount = ccount.count()
                notification = Empassign.objects.filter(empid=emp,status="0-10 %" and "none")
                notcount =notification.count()
            else:
                # Clear the session if username or loginid is not present
                request.session.flush()
                return redirect('login')

    return render(request,"Employee/empindex.html",{'emp':emp,'tcount':tcount,'scount':scount,'comcount':comcount,'notification':notification,'notcount':notcount,'emp1':emp12,'ccount':ccount})


def viewprofile(request):
    emp = None
    username = request.session.get('username')
    loginid = request.session.get('loginid')

    if username and loginid:
        # Check if the Login object exists
        if Login.objects.filter(username=username, loginid=loginid).exists():
            emp = Login.objects.get(username=username, loginid=loginid).empid

    return render(request, "Employee/viewprofile.html", {'emp': emp})


def changeuserpass(request):

    emp = None
    username = request.session.get('username')
    loginid = request.session.get('loginid')

    if username and loginid:
        # Check if the Login object exists
        if Login.objects.filter(username=username, loginid=loginid).exists():
            emp = Login.objects.get(username=username, loginid=loginid).empid
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
                        request.session.flush()
                        return render(request, "Login/index.html")
                    else:
                        return render(request, "Employee/changeuserpass.html", {'error': 'Invalid credentials'})
                else:
                    return render(request, "Employee/changeuserpass.html", {'error': 'New passwords do not match'})
            else:
                return render(request, "Employee/changeuserpass.html",
                              {'error': 'Current username does not match session'})
        else:
            return render(request, "Employee/changeuserpass.html", {'error': 'Session data missing'})

    return render(request, "Employee/changeuserpass.html",{'emp':emp})

def logout(request):
    request.session.flush()
    return redirect('/Login/login')


def viewtask(request):

    username = request.session.get('username')
    loginid = request.session.get('loginid')

    if username and loginid:

        if Login.objects.filter(username=username, loginid=loginid).exists():
            id = Login.objects.get(username=username, loginid=loginid).empid
            emp = Login.objects.get(username=username, loginid=loginid).empid

    emp1 = Empassign.objects.filter(empid=id)


    return render(request,"Employee/viewtask.html",{'emp1':emp1,'emp':emp})

def taskupdate(request, id):
    emp = None
    assigndata = None  # Initialize assigndata outside the if block to ensure it's always defined

    username = request.session.get('username')
    loginid = request.session.get('loginid')

    if username and loginid:
        # Check if the Login object exists
        if Login.objects.filter(username=username, loginid=loginid).exists():
            emp = Login.objects.get(username=username, loginid=loginid).empid
            try:
                assigndata = Empassign.objects.get(empassignid=id)
            except Empassign.DoesNotExist:
                pass  # Handle case where the assignment doesn't exist

    if request.method == 'POST':
        try:
            assignobj = Empassign.objects.get(empassignid=id)
            assignobj.status = request.POST.get('status')
            assignobj.rstatus='Requested'
            assignobj.save()
        except Empassign.DoesNotExist:
            pass  # Handle case where the assignment doesn't exist

        # Redirect to a different page after the update
        return redirect("viewtask")

    return render(request, "Employee/taskupdate.html", {'assigndata': assigndata, 'emp': emp})

def idcard(request):
    emp = None
    username = request.session.get('username')
    loginid = request.session.get('loginid')

    if username and loginid:
        # Check if the Login object exists
        if Login.objects.filter(username=username, loginid=loginid).exists():
            emp = Login.objects.get(username=username, loginid=loginid).empid

    return render(request, "Employee/idcard.html", {'emp': emp})


def viewcompletedtask(request):
    #return HttpResponse(id)
    username = request.session.get('username')
    loginid = request.session.get('loginid')

    if username and loginid:
        # Check if the Login object exists
        if Login.objects.filter(username=username, loginid=loginid).exists():
            id = Login.objects.get(username=username, loginid=loginid).empid
            emp = Login.objects.get(username=username, loginid=loginid).empid

    emp1 = Empassign.objects.filter(empid=id,status="Completed")
    return render(request,"Employee/viewcompletedtask.html",{'emp1':emp1,'emp':emp})

def viewpendingtask(request):
    #return HttpResponse(id)
    username = request.session.get('username')
    loginid = request.session.get('loginid')

    if username and loginid:
        # Check if the Login object exists
        if Login.objects.filter(username=username, loginid=loginid).exists():
            id = Login.objects.get(username=username, loginid=loginid).empid
            emp = Login.objects.get(username=username, loginid=loginid).empid

    emp1=Empassign.objects.filter(~Q(status="Completed"),empid=id)
    return render(request,"Employee/viewpendingtask.html",{'emp1':emp1,'emp':emp})

def tstatus(request):
    emp = None
    username = request.session.get('username')
    loginid = request.session.get('loginid')

    if username and loginid:
        # Check if the Login object exists
        if Login.objects.filter(username=username, loginid=loginid).exists():
            id = Login.objects.get(username=username, loginid=loginid).empid
            emp = Login.objects.get(username=username, loginid=loginid).empid
        emp1 = Empassign.objects.filter(empid=id)
    return render(request,"Employee/tstatus.html",{'emp':emp,'emp1':emp1})



class ExportExcelt(View):
    def post(self, request):
        fdate=request.POST.get('fdate')
        tdate=request.POST.get('tdate')
        emp_id=request.POST.get('id')
        #return HttpResponse(emp_id)

        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="projectdetails.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Sheet1')

        # Define the column headings
        row_num = 0
        columns = ['Activity Name', 'Project','Assigned Date','Due Date','Status']
        for col_num, column_title in enumerate(columns):
            ws.write(row_num, col_num, column_title)

        # Query the data from your model, and write it to the worksheet
        details = Empassign.objects.filter(assigndate__range=(fdate, tdate),empid=emp_id).values_list('projecttaskid__activityid__activityname','projectid__projectname','assigndate','duedate','status')


        # Calculate total quantity for each product within the date range
        for row in details:
            row_num += 1
            for col_num,cell_value in enumerate(row):
                ws.write(row_num, col_num, cell_value)

        wb.save(response)
        return response