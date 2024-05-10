from django.db import models


class Data(models.Model):
    title = models.CharField(max_length=200)

