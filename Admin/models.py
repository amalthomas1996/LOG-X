from datetime import date

from django.db import models


# Create your models here.


class Activity(models.Model):
    activityid = models.AutoField(primary_key=True)
    activityname = models.CharField(max_length=50)


class Project(models.Model):
    projectid = models.AutoField(primary_key=True)
    projectname = models.CharField(max_length=20)
    projectdesc = models.CharField(max_length=100)
    projectdate = models.DateField(default=date.today)
    projectcost = models.BigIntegerField()
    startingdate = models.DateField()
    enddate = models.DateField()
    status=models.CharField(max_length=50,null=True)


class Team(models.Model):
    teamid = models.AutoField(primary_key=True)
    teamname = models.CharField(max_length=20)
    projectid = models.ForeignKey(Project, on_delete=models.CASCADE, default="")
    description = models.CharField(max_length=50)


class Employee(models.Model):
    empid = models.AutoField(primary_key=True)
    empname = models.CharField(max_length=20)
    empcode = models.CharField(max_length=20)
    role = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20)
    projectid = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    photo = models.ImageField()
    teamid = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)
    assigndate = models.DateField(default=date.today)


class Login(models.Model):
    loginid = models.AutoField(primary_key=True)
    empid = models.ForeignKey(Employee, on_delete=models.CASCADE, default="")
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
