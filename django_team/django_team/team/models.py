from django.db import models
from django_team.responsability.models import Responsability


class Team(models.Model):
    name = models.CharField(max_length = 50, null = False, blank = False)
    description = models.CharField(max_length = 255, null = False, blank = False)
    created_date = models.DateField(auto_now_add = True)
    responsability = models.ManyToManyField(Responsability)

    def __str__(self):
        return f'Name: {self.name}  -  Descrição: {self.description}'
