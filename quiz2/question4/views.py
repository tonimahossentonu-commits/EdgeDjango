from django.shortcuts import render

def hello_user(request, username):
    return render(request, 'hello.html', {'username': username})
