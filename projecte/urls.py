from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('teachers/', views.teachers_llista, name='teachers_llista'),
    path('teachers/teacher/<str:pk>/', views.teacher_agafaun, name='teacher_un'),
    path('students/', views.students_llista, name='students_llista'),
    path('students/student/<str:pk>/', views.student_agafaun, name='student_un'),
    #path('user-form/', views.user_form, name='user_form'),
    path('teacher-create/', views.teacher_form, name='teacher_form'),
    path('update-teacher/<str:pk>/', views.update_teacher, name='update-teacher'),
    path('delete-teacher/<str:pk>/', views.delete_teacher, name='delete-teacher'),
    path('student-create/', views.student_form, name='student_form'),
    path('update-student/<str:pk>/', views.update_student, name='update-student'),
    path('delete-student/<str:pk>/', views.delete_student, name='delete-student'),
]