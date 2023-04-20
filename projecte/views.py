from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Context, loader
from .models import Teacher, Student
from .forms import TeacherForm, StudentForm


# Create your views here.
def index(request):
    
    return render(request, 'index.html', {'nombre':professor["name"], "surname":professor["surname"], "age":professor["age"]})


professor =[{"id":"0","name":"Roger", "surname":"Sobrino", "age":"17"}, {"id":"1","name":"Pere", "surname":"Gobrino", "age":"30"}, {"id":"2","name":"Soger", "surname":"Nobrino", "age":"71"}]

student = [{"id":"0","name":"Kevin", "surname":"Sama", "age":"17"}, {"id":"1","name":"Pol", "surname":"Iniesta", "age":"18"}, {"id":"2","name":"Soger", "surname":"Nobrino", "age":"11"}, {"id":"3","name":"Mich", "surname":"Rosado", "age":"20"}, {"id":"4","name":"Luis", "surname":"Castillo", "age":"20"}, {"id":"5","name":"Andrei", "surname":"Crasnaru", "age":"19"}]

def teachers_llista(request):
    teachers = Teacher.objects.all()
    context = {'teachers':teachers}
    return render(request, 'teachers.html', context)

def teacher_agafaun(request, pk):
    teacher = Teacher.objects.get(id=pk)
    context = {'teacher':teacher}
    return render(request, 'teacher.html', context)

def students_llista(request):
    students = Student.objects.all()
    context = {'students':students}
    return render(request, 'students.html', context)

def student_agafaun(request, pk):
    student = Student.objects.get(id=pk)
    context = {'student':student}
    return render(request, 'student.html', context)

# def students(request):
#     context = {'st':student}
#     return render(request, 'students.html', context)

# def teacher(request, pk):
#     teacher_Obj = None
#     for i in professor:
#         if i['id'] == pk:
#             teacher_Obj = i
#     return render(request, 'teacher.html', {'teachers': teacher_Obj})

# def student(request, pk):
#     student_Obj = None
#     for i in student:
#         if i['id'] == pk:
#             student_Obj = i
#     return render(request, 'student.html', {'students': student_Obj})

# def user_form(request):
#     form = TeacherForm()
#     context = {'form':form}
#     return render(request, 'form.html', context)

def teacher_form(request):
    form = TeacherForm()

    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():

            form.save()
            return redirect('teachers_llista')
    context = {'form':form}
    return render(request, 'form.html', context)

def update_teacher(request, pk):
    teacher = Teacher.objects.get(id=pk)
    form = TeacherForm(instance=teacher)

    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teachers_llista')
    
    context = {'form':form}
    return render(request, 'form.html', context)

def delete_teacher(request, pk):
    teacher = Teacher.objects.get(id = pk)

    if request.method == 'POST':
        teacher.delete()
        return redirect('teachers_llista')

    context = {'object':teacher}
    return render(request, 'delete_object.html', context)

def student_form(request):
    form = StudentForm()

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():

            form.save()
            return redirect('students_llista')
    context = {'form':form}
    return render(request, 'form_student.html', context)

def update_student(request, pk):
    student = Student.objects.get(id=pk)
    form = StudentForm(instance=student)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('students_llista')
    
    context = {'form':form}
    return render(request, 'form.html', context)

def delete_student(request, pk):
    student = Student.objects.get(id = pk)

    if request.method == 'POST':
        student.delete()
        return redirect('students_llista')

    context = {'object':student}
    return render(request, 'delete_object.html', context)