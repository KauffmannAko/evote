from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def index(request):
    return render(request, "./nav/index.html")
def ako(request):
    return  HttpResponse('hello, ako')
def calc(request):
    return HttpResponse('welcome to my first django view')
def greet(request,name):
    return HttpResponse("hello {}".format(name.capitalize()))
def introduce(request, name):
    return render(request, "./nav/greet.html",{
        "name": name.capitalize(),
    })