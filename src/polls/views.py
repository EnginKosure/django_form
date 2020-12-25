from django.shortcuts import render

# Create your views here.

# Get questions and display them


def index(request):
    return render(request, 'polls/index.html')
