from django.urls import path
from .import views
from .views import ExportExcelpr

urlpatterns = [
    path('pmindex/',views.pmindex,name='pmindex'),
    path('addteam/',views.addteam,name='addteam'),
    path('viewteam/',views.viewteam,name='viewteam'),
    path('editteam/<id>',views.editteam,name='editteam'),
    path('deleteteam/<id>',views.deleteteam,name='deleteteam'),
    path('addprojecttask/',views.addprojecttask,name='addprojecttask'),
    path('viewprojecttask/',views.viewprojecttask,name='viewprojecttask'),
    path('editprojecttask/<id>',views.editprojecttask,name='editprojecttask'),
    path('deleteprojecttask/<id>',views.deleteprojecttask,name='deleteprojecttask'),
    path('empassign/',views.empassign,name='empassign'),
    path('viewempassign/',views.viewempassign,name='viewempassign'),
    path('filldata/',views.filldata,name='filldata'),
    path('deleteempassign/<id>',views.deleteempassign,name='deleteempassign'),
    path('confirm/<id>',views.confirm,name='confirm'),
    path('viewprofilepm/',views.viewprofilepm,name='viewprofilepm'),
    path('cup/',views.cup,name='cup'),
    path('sendmail/<id>',views.sendmail,name='sendmail'),
    path('prststus/',views.prststus,name='prststus'),
    path('export_excel/', ExportExcelpr.as_view(), name='export_excelpr'),
    path('logout/',views.logout,name='logout'),
]