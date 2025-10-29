
from django.shortcuts import render

def home(request):
    name = "Abdur Rahim"
    age = 22
    return render(request, 'home.html', {'name': name, 'age': age})
