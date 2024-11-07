from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sayHelloWorld(req):
    x = 1
    y = 2
    return render(req, 'Hello.html', {'name': "Surya "})