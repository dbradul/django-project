from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError

from project.utils import format_records

from teachers.models import Teacher
from teachers.forms import TeacherCreateForm

from webargs import fields
from webargs.djangoparser import use_args

teacher_args = {
    'name': fields.Str(required=False),
    'surname': fields.Str(required=False),
    'age': fields.Int(required=False)
}


@use_args(teacher_args, location='query')
def get_teachers(request, args):
    teachers = Teacher.objects.all()

    for param_name, param_value in args.items():
        teachers = teachers.filter(**{param_name: param_value})

    teachers_list = format_records(teachers)

    return HttpResponse(teachers_list)


@csrf_exempt
def create_teacher(request):
    if request.method == 'GET':

        form = TeacherCreateForm()

    elif request.method == 'POST':

        form = TeacherCreateForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/teachers/')

    html_form = f"""
        <form method="post">

        {form.as_p()}

        <input type="submit" value="Submit">

        </form>
        """

    response = html_form

    return HttpResponse(response)
