from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

# Create your views here.
def index(request):
    
    return render(request, 'index.html', {'nombre':professor["name"], "surname":professor["surname"], "age":professor["age"]})


professor =[{"name":"Roger", "surname":"Sobrino", "age":"17"}, {"name":"Pere", "surname":"Gobrino", "age":"30"}, {"name":"Soger", "surname":"Nobrino", "age":"71"}]

student = [{"name":"Kevin", "surname":"Sama", "age":"17"}, {"name":"Pol", "surname":"Iniesta", "age":"18"}, {"name":"Soger", "surname":"Nobrino", "age":"11"}, {"name":"Mich", "surname":"Rosado", "age":"20"}, {"name":"Luis", "surname":"Castillo", "age":"20"}, {"name":"Andrei", "surname":"Crasnaru", "age":"19"}]

def teachers(request):
    context = {'pr':professor}
    return render(request, 'teachers.html', context)

def students(request):
    context = {'st':student}
    return render(request, 'students.html', context)