from django.db import models


class Testmodel1(models.Model):
    name = models.CharField(max_length=20)


class Testmodel2(Testmodel1):
    age = models.CharField(max_length=10)