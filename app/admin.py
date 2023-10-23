from django.contrib import admin

from app.models import Stu, people

# Register your models here.
@admin.register(people)
class peopleAdmin(admin.ModelAdmin):
    list_display=['id','age','height','student']


@admin.register(Stu)
class StuAdmin(admin.ModelAdmin):
    list_display=['id','name','dob']
