from django.db import models

class StateMap(models.Model):

    state = models.CharField(max_length=2, default="")
    map = models.JSONField(default=dict)


class SchoolDistrict(models.Model):

    state = models.CharField(max_length=2, default="")
    school_district = models.CharField(max_length=40, default="")
    total_pop = models.IntegerField(default=0)
    poverty_pop = models.IntegerField(default=0)