from django.urls import path
from .import views



urlpatterns = [
    path('login/',views.login,name='login'),
    path('forgotpassword/',views.forgotpassword,name='forgotpassword'),


]