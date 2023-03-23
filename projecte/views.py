from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

# Create your views here.
def index(request):
    professor = {"name":"Roger", "surname":"Sobrino", "age":"17"}
    template = loader.get_template('index.html')
    return HttpResponse(template.render())