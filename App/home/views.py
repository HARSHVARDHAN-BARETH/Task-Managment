from django.shortcuts import render, redirect, get_object_or_404
from .models import NewTask
from .forms import TaskForm

# Create your views here.

def task_list(request):
    tasks = NewTask.objects.all()
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

# Task update
def task_update(request, pk):
    task = get_object_or_404(NewTask, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_update.html', {'form': form, 'task': task})

# Task delete
def task_delete(request, pk):
    task = get_object_or_404(NewTask, pk=pk)
    if request.method == "POST":
        task.delete()
        return redirect('task_list')
    return render(request, 'task_delete.html', {'task': task})

