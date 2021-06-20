from django.forms import ModelForm
from django.core.exceptions import ValidationError

from project.utils import email_validator

from students.models import Student


class StudentCreateForm(ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'surname', 'age', 'email']

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email_validator(email):
            raise ValidationError('Invalid email', code='invalid')

        return email

