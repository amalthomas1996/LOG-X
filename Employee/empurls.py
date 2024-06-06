from django.urls import path
from .import views
from .views import ExportExcelt

urlpatterns = [
    path('empindex/',views.empindex,name='empindex'),
    path('viewprofile/',views.viewprofile,name='viewprofile'),
    path('changeuserpass/',views.changeuserpass,name='changeuserpass'),
    path('logout/',views.logout,name='logout'),
    path('viewtask/',views.viewtask,name='viewtask'),
    path('taskupdate/<id>',views.taskupdate,name='taskupdate'),
    path('idcard',views.idcard,name='idcard'),
    path('viewcompletedtask/',views.viewcompletedtask,name='viewcompletedtask'),
    path('viewpendingtask/',views.viewpendingtask,name='viewpendingtask'),
    path('tstatus/',views.tstatus,name='tstatus'),
    path('export_excelt/', ExportExcelt.as_view(), name='export_excelt'),

]