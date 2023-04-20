from django.forms import ModelForm
from .models import Teacher, Student

class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'