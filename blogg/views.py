from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>Blog Home</h> <p>This is my first django challenge task ever..I like django</P ')


def about(request):
    return HttpResponse('<h1>About Page</h1><p>This is just a nlog website..lets see how it goes</p>')