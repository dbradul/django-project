from django.forms import ModelForm

from students.models import Student


class StudentCreateForm(ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'surname', 'age', 'email']
