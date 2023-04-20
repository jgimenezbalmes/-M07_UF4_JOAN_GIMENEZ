from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('teachers/', views.teachers, name='teachers'),
    path('teachers/teacher/<str:pk>/', views.teacher, name='teacher'),
    path('students/', views.students, name='students'),
    path('students/student/<str:pk>/', views.student, name='student'),
    path('user-form/', views.user_form, name='user_form'),
    path('teacher-create/', views.teacher_form, name='teacher_form'),
    path('update-teacher/<str:pk>/', views.update_teacher, name='update-teacher'),
]