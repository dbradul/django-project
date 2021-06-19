"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URL conf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from groups.views import get_groups, create_group

from students.views import generate_students, get_students, create_student

from teachers.views import get_teachers, create_teacher

urlpatterns = [
    path('admin/', admin.site.urls),
    path('generate_students/', generate_students),
    path('students/', get_students),
    path('groups/', get_groups),
    path('teachers/', get_teachers),
    path('students/create/', create_student),
    path('teachers/create/', create_teacher),
    path('groups/create/', create_group),
]
