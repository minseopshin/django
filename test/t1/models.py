from django.db import models
from django_matplotlib import MatplotlibFigureField
from django.utils import timezone


class t1(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title

class MyModel(models.Model):
    figure = MatplotlibFigureField(figure='my_figure')

class ADMIN_REQ(models.Model):
    admin_req_type=models.CharField(max_length=200)
    admin_req_tel_num=models.CharField(max_length=200)
    admin_req_time=models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'admin_req'