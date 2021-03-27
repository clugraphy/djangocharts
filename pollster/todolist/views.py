from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import TaskList
from .forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.urls import reverse



#@login_required
def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.manager = request.user
            instance.save()
        messages.success(request,("New Task Added!"))
        return redirect('todolist:todolist')
    else:
        all_tasks = TaskList.objects.filter(manager=request.user)
        paginator = Paginator(all_tasks, 5, allow_empty_first_page=True)
        page = request.GET.get('page')
        all_tasks = paginator.get_page(page)

        return render(request, 'todolist/todolist.html', {'all_tasks': all_tasks})

#@login_required
def delete_task(request, task_id):
    task = TaskList.objects.get(pk = task_id)
    if task.manager == request.user:
        task.delete()
    else:
        messages.error(request,("Access Restricted , You are not Allowed."))
    return redirect('todolist:todolist')

#@login_required
def edit_task(request, task_id):
    if request.method == "POST":
        task = TaskList.objects.get(pk = task_id)
        form = TaskForm(request.POST or None, instance = task)
        if form.is_valid():
            form.save()
            messages.success(request,("Task Edited !"))
        return redirect('todolist:todolist')
    else:
        task_object = TaskList.objects.get(pk = task_id)
        return render(request, 'todolist/edit.html', {'task_object': task_object})

#@login_required
def complete_task(request, task_id):
    task = TaskList.objects.get(pk = task_id)
    if task.manager == request.user:
        task.done = True
        task.save()
    else:
         messages.error(request,("Access Restricted , You are not Allowed."))

    return redirect('todolist:todolist')

#@login_required
def pending_task(request, task_id):
    task = TaskList.objects.get(pk = task_id)
    task.done = False
    task.save()

    return redirect('todolist:todolist')

def index(request):
    context = {'index_text': "Wellcome To Homepage from Jinja2 this your index page"}
    return render(request, 'todolist/index.html', context)


        