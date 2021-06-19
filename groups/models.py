import random

from django.db import models

from faker import Faker


class Group(models.Model):
    name = models.CharField(max_length=50, null=False)
    status = models.CharField(max_length=50, null=False)
    members_quantity = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name}, {self.status}, {self.members_quantity}'

    @staticmethod
    def generate_groups(count):
        faker = Faker()
        for _ in range(count):
            groups = Group(name=faker.first_name().lower(), status='123123', member_quantity=random.randint(1, 100))
            groups.save()
