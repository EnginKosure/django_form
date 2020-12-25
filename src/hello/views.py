from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'hello/index.html')


def index1(request):
    return HttpResponse("Hello, world. b06cbb87 is the polls index.")
