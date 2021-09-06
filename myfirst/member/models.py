from django.db import models

class Member(models.Model):
    username = models.CharField(max_length=100)
    pwd = models.CharField(max_length=100)
    regdate = models.DateField(auto_now_add=True)
    email = models.CharField(max_length=50)