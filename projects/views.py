from django.http import Http404
from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from projects import models,forms

def home(request):

    projects = models.Project.objects.all().order_by("name")
    projectNumber = len(projects)

    return render(request,'projects/home.html',locals())

def showProject(request,slug):

    try:
        project = models.Project.objects.get(slug=slug)
    except ObjectDoesNotExist:
        raise Http404

    if request.user.is_authenticated():
        if request.method == "POST":
            form = forms.createTaskForm(request.POST)
            if form.is_valid():
                task = form.save(commit=False)
                task.progression = 0
                task.project = project
                task.save()
        else:
            form = forms.createTaskForm()

    return render(request,"projects/showProject.html",locals())

def setTaskProgression(request,id):

    if request.user.is_authenticated():
        try:
            task = models.Task.objects.get(id=id)
            newProgression = int(request.GET.get("progress","-1"))
            if newProgression > -1 and newProgression <= 100:
                task.progression = newProgression
                task.save()
            else :
                error = "not valid"
                errDescription = "You don't enter a valid progression in the parameter 'progress'"

        except ObjectDoesNotExist:
            error = "not found"
            errDescription = "The task "+id+" doesn't exist"
    else:
        error = "forbidden"
        errDescription = "You are not allowed to edit the tasks progressions. Please log in"

    return render(request,"projects/setTaskProgression.json",locals())