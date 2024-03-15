from django.shortcuts import render, redirect
from django.http import HttpResponse

from task.models import Task
from task.forms import TaskForm

def home(request):

    
    user_data = {
        "name": "Gokul",
        "email": "test@gmail.com"
    } # dict
    task_data = Task.objects.all() # List


    return render(request, "task/home.html", context={"task_data": task_data, "user_data": user_data})

def create_task(request):
    if request.method == "GET":
        form = TaskForm()
        return render(request, "task/create_task.html", context={"form": form})
    elif request.method == "POST":
        print(request.POST)
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        
        return redirect("home")