# views.py
from rest_framework import generics
from rest_framework.response import Response
from .models import Student, Courses, Enrollment
from .serializers import StudentSerializer, StudentCourseSerializer, EnrollmentSerializer

class EnrollStudentInCourse(generics.CreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

class UpdateMarks(generics.UpdateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

class ListAvailableCourses(generics.ListAPIView):
    queryset = Courses.objects.all()
    serializer_class = StudentCourseSerializer

class ListMarksOfStudent(generics.ListAPIView):
    serializer_class = EnrollmentSerializer

    def get_queryset(self):
        student_id = self.kwargs['student_id']
        return Enrollment.objects.filter(student_id=student_id)

class CalculateAverageGrade(generics.GenericAPIView):
    def get(self, request, student_id):
        student_enrollments = Enrollment.objects.filter(student_id=student_id)
        total_marks = sum(enrollment.marks for enrollment in student_enrollments if enrollment.marks is not None)
        if student_enrollments.exists():
            average_grade = total_marks / student_enrollments.count()
            return Response({'average_grade': average_grade})
        else:
            return Response({'message': 'No enrollments found for this student'}, status=404)
