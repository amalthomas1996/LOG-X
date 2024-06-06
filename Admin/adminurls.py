from django.urls import path
from . import views
from .views import ExportExcelYear, ExportExcelEmp, ExportExcelSortEmp

urlpatterns = [
    path('index/', views.index, name='index'),
    path('addproject/', views.addproject, name='addproject'),
    path('viewprojects/', views.viewprojects, name='viewprojects'),
    path('addemployee/', views.addemployee, name='addemployee'),
    path('viewemployee/', views.viewemployee, name='viewemployee'),
    path('editproject/<id>', views.editproject, name='editproject'),
    path('editemployee/<id>', views.editemployee, name='editemployee'),
    path('deleteemployee/<id>', views.deleteemployee, name='deleteemployee'),
    path('deleteproject/<id>', views.deleteproject, name='deleteproject'),
    path('viewprojectstatus/', views.viewprojectstatus, name='viewprojectstatus'),
    path('projectassignview/', views.projectassignview, name='projectassignview'),
    path('projectassign/', views.projectassign, name='projectassign'),
    path('fillemp/',views.fillemp,name='fillemp'),
    path('yearlyreport/',views.yearlyreport,name='yearlyreport'),
    path('export_excel/', ExportExcelYear.as_view(), name='export_excel'),
    path('fillprodata/',views.fillprodata,name='fillprodata'),
    path('sortempreport/',views.sortempreport,name='sortempreport'),
    path('export_excel_sortemp/', ExportExcelSortEmp.as_view(), name='export_excel_sortemp'),

    path('empreport/',views.empreport,name='empreport'),
    path('export_excelemp/',ExportExcelEmp.as_view(),name='export_excelemp'),
    path('predictionspage/',views.predictionspage,name='predictionspage'),
    path('prediction/',views.prediction,name='prediction'),

    path('logout/', views.logout, name='logout'),
]
