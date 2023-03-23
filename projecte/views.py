from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

# Create your views here.
def index(request):
    professor = {"name":"Roger", "surname":"Sobrino", "age":"17"}
    return render(request, 'index.html', {'nombre':professor["name"], "surname":professor["surname"], "age":professor["age"]})

def teachers(request):
    professor = {"name":"Roger", "surname":"Sobrino", "age":"17"}
    return render(request, 'teachers.html', {'nombre':professor["name"], "surname":professor["surname"], "age":professor["age"]})