from django.db import models

class StateMap(models.Model):

    state = models.CharField(max_length=2, default="")
    coords = models.TextField(default="")
    map = models.JSONField(default={})