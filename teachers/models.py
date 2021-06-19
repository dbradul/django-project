from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=50, null=False)
    surname = models.CharField(max_length=50, null=False)
    age = models.IntegerField(default=18)
    email = models.CharField(max_length=50, null=False)

    def __str__(self):
        return f'{self.name}, {self.surname}, {self.age}, {self.email}'