from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

# Create your views here.

def task_list(request):
    tasks = Task.objects.all()
    return render(request,"task_list.html", {"tasks":tasks})

def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request,'task_create.html', {'form':form})

def home(request):
    people = [
        {'name':'harsh','age':19},
        {'name':'h','age':20}
    ]
    return render(request,"index.html", context={'people':people})