from django.contrib import admin

from app.models import Student, Course, Room, Hostel

# Register your models here.
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Room)
admin.site.register(Hostel)