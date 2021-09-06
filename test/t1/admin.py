from django.contrib import admin
from .models import t1,MyModel
# Register your models here.


class tAdmin(admin.ModelAdmin):
    list_display = ['title','content']

admin.site.register(t1, tAdmin)
admin.site.register(MyModel)