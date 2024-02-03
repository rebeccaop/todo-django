from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from .models import Task
from datetime import date

# Create your views here.
def task(request):
    task= request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')


def mark_as_done(request,pk):
    task= Task.objects.filter(pk= pk)
    task.update(is_completed= True)
    return redirect('home')

def mark_as_undone(request,pk):
    task= get_object_or_404(Task,pk=pk)
    task.is_completed=False
    task.save()
    return redirect('home')

def edit_task(request,pk):
    task= get_object_or_404(Task,pk=pk)
    if (request.method=='POST'):
        value= request.POST['task']
        task.task=value
        task.modified_at= date.today()
        task.save()
        return redirect('home')
    else:
        context={
            'task': task
        }
        return render(request,'edit_task.html',context= context)

def delete_task(request,pk):
    task= get_object_or_404(Task,pk=pk)
    task.delete()
    return redirect('home')