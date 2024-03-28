from django.db import models


class Compromissos(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    event_date = models.DateTimeField()
    creation_date = models.DateTimeField(auto_now=True)
