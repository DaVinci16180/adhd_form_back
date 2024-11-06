"""
URL configuration for adhd_form_back project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from .api.FormRestApi import *
from .api.ReportsRestApi import *

urlpatterns = [
    path('api/form/submit', post_form, name='Submit Form'),
    path('api/reports/patients', get_patients, name='Fetch Patient List'),
    path('api/reports/report', get_report, name='Fetch Report'),
    path('admin/', admin.site.urls),
]
