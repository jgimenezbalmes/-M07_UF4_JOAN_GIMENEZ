from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

# Create your views here.
def index(request):
    
    return render(request, 'index.html', {'nombre':professor["name"], "surname":professor["surname"], "age":professor["age"]})


professor =[{"name":"Roger", "surname":"Sobrino", "age":"17"}, {"name":"Pere", "surname":"Gobrino", "age":"30"}, {"name":"Soger", "surname":"Nobrino", "age":"71"}]

def teachers(request):
   
    context = {'pr':professor}
    return render(request, 'teachers.html', context)