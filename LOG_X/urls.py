"""LOG_X URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from django.conf.urls.static import static

from LOG_X import settings

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', lambda request: redirect('Login/login', permanent=False)),  # Redirects to Login page
    path('Admin/',include('Admin.adminurls')),
    path('Login/', include('Login.loginurls')),
    path('ProjectManager/',include('ProjectManager.pmurls')),
    path('Employee/',include('Employee.empurls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
