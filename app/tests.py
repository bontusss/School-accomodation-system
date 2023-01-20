from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from .models import Student

# Create your tests here.
class AppTest(TestCase):
    def create_student(
        self,
        first_name="John",
        last_name="Doe",
        enrollment_no="1234",
        room_alloted=False,
    ):
        return Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            enrollment_no=enrollment_no,
            room_allotted=room_alloted,
        )

    def test_student_creation(self):
        s = self.create_student()
        self.assertTrue(isinstance(s, Student))
        self.assertTrue(s.__unicode__(), s.student_name)