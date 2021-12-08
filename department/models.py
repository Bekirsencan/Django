from django.db import models


class Department(models.Model):
    department_name = models.CharField(max_length=100)

    objects = models.Manager()

    class Meta:
        db_table = 'Department'
