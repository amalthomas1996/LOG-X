import smtplib
from email.message import EmailMessage

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_control
from Admin.models import Login, Employee


@cache_control(no_cache=True, must_revalidate=True, no_store=True)



# Create your views here.
def login(request):
    if "Loginid" in request.session:
        del request.session["username"]
        del request.session['loginid']
    request.session.flush()
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        if Login.objects.filter(username=username, password=password).exists():
            loginobj = Login.objects.get(username=username, password=password)

            request.session['username'] = loginobj.username
            request.session['loginid'] = loginobj.loginid
            role = loginobj.role
            if role == "Admin":
                return redirect('index')
            if role == 'Project Manager':
                return redirect('pmindex')
            if role == 'Employee':
                return redirect('empindex')
        else:
            context = {"error": "Invalid Username and password"}
            return render(request, "Login/index.html", context)
    else:
        return render(request, "Login/index.html")

def forgotpassword(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        if Employee.objects.filter(email=email).exists():

            emp = Employee.objects.get(email=email)
            loginobj = Login.objects.get(empid=emp)
            loginobj.password = "97afhnhj"
            loginobj.save()

            msg = EmailMessage()
            msg.set_content(f"Your Username: {email}\n"
                            f"Your temporary password: 97afhnhj\n"
                            "Please use these credentials to login to LOG-X and change the password ASAP.")
            msg['Subject'] = "Temporary Password"
            msg['From'] = 'thomasamal61@gmail.com'
            msg['To'] = email
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login('thomasamal61@gmail.com', 'xkvx zaja bbwh nipr')
                smtp.send_message(msg)
            return HttpResponse("<script>alert('Temporary password sent to your email. "
                                "Please check your inbox.');window.location='/Login/login';</script>")
        else:
            context = {"error": "Email ID does not exist"}
            return render(request, "Login/index.html", context)
    else:
        return render(request, "Login/forgotpaasword.html")





