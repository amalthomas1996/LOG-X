from datetime import date

from django.db import models

from Admin.models import Activity, Project, Employee

# Create your models here.
class ProjectTask(models.Model):
    projecttaskid = models.AutoField(primary_key=True)
    activityid = models.ForeignKey(Activity, on_delete=models.CASCADE, default="")
    projectid = models.ForeignKey(Project, on_delete=models.CASCADE, default="")
    description = models.CharField(max_length=50)
    startingdate = models.DateField()
    enddate = models.DateField()



class Empassign(models.Model):
    empassignid = models.AutoField(primary_key=True)
    projecttaskid = models.ForeignKey(ProjectTask, on_delete=models.CASCADE, default="")
    empid = models.ForeignKey(Employee, on_delete=models.CASCADE, default="")
    assigndate = models.DateField(default=date.today)
    duedate = models.DateField()
    status = models.CharField(max_length=50)
    projectid = models.ForeignKey(Project, on_delete=models.CASCADE, default="")
    rstatus = models.CharField(max_length=50)

class Projectassigndata(models.Model):
    assignid = models.AutoField(primary_key=True)
    projectid = models.ForeignKey(Project, on_delete=models.CASCADE, default="")
    empid = models.ForeignKey(Employee, on_delete=models.CASCADE, default="")
    status = models.CharField(max_length=50,null=True)