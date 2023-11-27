from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    parent_name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Courses(models.Model):
    course_name = models.CharField(max_length=100)
    dept = models.CharField(max_length=100)
    credit_hours=models.IntegerField()

    def __str__(self):
        return self.course_name



class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    enrollment_date = models.DateField()
    marks = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)