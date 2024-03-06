from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Task
from .forms import TaskForm

def index(request):
    tasks  = Task.objects.filter(title__icontains=request.GET.get('search', ''))
    context = {
        'tasks' : tasks
    }
    return render(request,'task/index.html', context)

def view(request,id):
    task = Task.objects.get(id=id)
    context = {
        'task' : task
    }

    return render(request, 'task/detail.html', context)

def edit(request,id):
    task = Task.objects.get(id=id)

    if (request.method == 'GET'):
        form = TaskForm(instance=task)
        context = {
            'form':form,
            'id' : id,
        }
        return render(request, 'task/edit.html', context)

    if (request.method == "POST"):
        form = TaskForm(request.POST, instance=task)
        if form.is_valid:
            form.save()
        context = {
            'form':form,
            'id':id,
        }
        messages.success(request, "Task Updated.")
        return render(request, 'task/edit.html', context)

def create(request):

    if (request.method == 'GET'):
        form = TaskForm()
        context = {
            'form':form,
        }
        return render(request, 'task/create.html', context)

    if (request.method == "POST"):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        context = {
            'form':form,
        }
        return redirect('task')
    
def delete(request,id):
    contact = Task.objects.get(id=id)
    contact.delete()
    return redirect('task')