from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.

class Room(models.Model):
    room_choice = [('S', 'Single Occupancy'), ('D', 'Double Occupancy'), ('P', 'Reserved for Research Scholars'),('B', 'Both Single and Double Occupancy')]
    no = models.CharField(max_length=5)
    name = models.CharField(max_length=10)
    room_type = models.CharField(choices=room_choice, max_length=1, default=None)
    vacant = models.BooleanField(default=False)
    hostel = models.ForeignKey('Hostel', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Hostel(models.Model):
    name = models.CharField(max_length=5)
    gender_choices = [('M', 'Male'), ('F', 'Female')]
    gender = models.CharField(
        choices=gender_choices,
        max_length=1,
        default=None,
        null=True)
    course = models.ManyToManyField('Course', default=None, blank=True)
    caretaker = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Landlord(models.Model):
    name = models.CharField(max_length=100, null=True)
    hostel = models.ForeignKey('Hostel', default=None, null=True, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, null=True)


class Course(models.Model):
    # if a student has enrollment number iit2017001 then the course code is iit2017
    code = models.CharField(max_length=100, default=None)
    room_choice = [('SINGLE', 'Single Occupancy'), ('DOUBLE', 'Double Occupancy'), ('RESERVED', 'Reserved for Research Scholars'), ('SUITE', 'Both Single and Double Occupancy')]
    room_type = models.CharField(choices=room_choice, max_length=10, default='D')

    def __str__(self):
        return self.code


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender_choices = [('M', 'Male'), ('F', 'Female')]
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    enrollment_no = models.CharField(max_length=10, unique=True, null=True)
    course = models.ForeignKey(
        'Course',
        null=True,
        default=None,
        on_delete=models.CASCADE)
    dob = models.DateField(
        max_length=10,
        help_text="format : YYYY-MM-DD",
        null=True)
    gender = models.CharField(
        choices=gender_choices,
        max_length=1,
        default=None,
        null=True)
    room = models.OneToOneField(
        'Room',
        blank=True,
        on_delete=models.CASCADE,
        null=True)
    room_allotted = models.BooleanField(default=False)
    no_dues = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_student_signal(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)
    instance.student.save()