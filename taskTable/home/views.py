from django.shortcuts import render
from . import models
from .forms import TaskForm
from django.contrib import messages



def homepage(request,col='',asec=0):

    contents = models.Task.objects.all()
    '''
    if soring by column than tried giving not completed task
    higher value if priority of task is same
    '''

    if col=='priority':
        order = {'low': 0, 'medium': 10, 'high': 20, 'urgent': 30}
        status = {'Not Completed':1,'Completed':0}
        contents = sorted(contents,key= lambda x: order[x.priority]+status[x.status],reverse= True if asec==0 else False)
    
    elif col!='':
        #order by high to low
        if asec:
            contents = contents.order_by('-'+col)
        else:
            contents = contents.order_by(col)

    context = {'contents':contents}
    return render(request,'homepage.html',context)

def create_task(request):
    context = {}

    if request.method=="POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'New Task Added')
            return homepage(request)

    else:
        form = TaskForm()

    context['form'] = form
    context['contents'] = models.Task.objects.all()
    return render(request, "create_task.html", context)

def delete_task(request,id):
    task = models.Task.objects.filter(id=id).delete()
    return homepage(request)

def update_status(request,id):

    task = models.Task.objects.get(id=id)
    #update task status with id=id
    
    if task.status=='Not Completed':
        task.status='Completed'
    else:
        task.status = 'Not Completed'

    task.save()

    return homepage(request)
