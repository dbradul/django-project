import random

from django.db import models

from faker import Faker


class Student(models.Model):
    name = models.CharField(max_length=50, null=False)
    surname = models.CharField(max_length=50, null=False)
    age = models.IntegerField(default=18)
    email = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f'{self.name}, {self.surname}, {self.age}, {self.email}'

    def full_name(self):
        return f'{self.name}, {self.surname}'

    @staticmethod
    def generate_students(count):
        faker = Faker()
        for _ in range(count):
            st = Student(name=faker.first_name(), surname=faker.last_name(), age=random.randint(18, 100), email=email)
            st.save()
