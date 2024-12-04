from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def students(request):
    students = [
        {'id': 1, 'name': 'John Doe', 'age': 26}
    ]
    return HttpResponse(students)
