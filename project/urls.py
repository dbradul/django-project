import debug_toolbar

from django.contrib import admin
from django.conf import settings
from django.urls import include, path

from groups.views import get_groups, create_group

from students.views import generate_students, get_students, create_student

from teachers.views import get_teachers, create_teacher

urlpatterns = [
    path('admin/', admin.site.urls),
    path('generate_students/', generate_students),
    path('students/', get_students),
    path('groups/', get_groups),
    path('teachers/', get_teachers),
    path('', get_teachers),
    path('students/create/', create_student),
    path('teachers/create/', create_teacher),
    path('groups/create/', create_group),
    path('__debug__/', include(debug_toolbar.urls)),
]
