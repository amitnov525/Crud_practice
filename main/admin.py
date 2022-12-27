from django.contrib import admin
from main.models import Student

# Register your models here.
@admin.register(Student)
class DisplayStudent(admin.ModelAdmin):
    list_display=['id','rollno','name','email','password']

