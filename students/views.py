from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from marshmallow import fields

from project.utils import format_records

from students.models import Student
from students.forms import StudentCreateForm

from webargs.djangoparser import use_args

gen_args = {
    'count': fields.Int(missing=10, required=False)
}

students_args = {
    'name': fields.Str(required=False),
    'surname': fields.Str(required=False),
    'age': fields.Int(required=False)
}


@use_args(students_args, location='query')
def get_students(request, args):
    students = Student.objects.all()
    print(students)
    for param_name, param_value, param_email in args.items():
        if param_value:
            students = students.filter(**{param_name: param_value})

    students_list = format_records(students)
    return HttpResponse(students_list)


@use_args(gen_args, location='query')
def generate_students(request, args):
    Student.generate_students(args['count'])
    return HttpResponse('OK')


@csrf_exempt
def create_student(request):
    if request.method == 'GET':

        form = StudentCreateForm()

    elif request.method == 'POST':

        form = StudentCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/students/')

    html_form = f"""
        <form method="post">

        {form.as_p()}

        <input type="submit" value="Submit">

        </form>
        """

    response = html_form

    return HttpResponse(response)
