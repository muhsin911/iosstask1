from rest_framework import serializers
from .models import Student,Courses,Enrollment

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'name', 'age','parent_name ')

class StudentCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model= Courses
        fields = ('id', 'course_name','name', 'credit_hours')
class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ('id', 'student', 'course', 'enrollment_date', 'marks')