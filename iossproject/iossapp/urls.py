from django.urls import path
from .views import *

urlpatterns = [
    path('enroll/', EnrollStudentInCourse.as_view(), name='enroll-student'),
    path('update-marks/<int:pk>/', UpdateMarks.as_view(), name='update-marks'),
    path('available-courses/', ListAvailableCourses.as_view(), name='available-courses'),
    path('std-marks/<int:student_id>/', ListMarksOfStudent.as_view(), name='student-marks'),
    path('avg-grade/<int:student_id>/', CalculateAverageGrade.as_view(), name='average-grade'),
]
