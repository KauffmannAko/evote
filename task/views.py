from django.shortcuts import render
from django import forms
# Create your views here.
class Taskform(forms.Form):
    task =forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority",min_value=1,max_value=4)
tasks = [ "nana","ako","akpah"]
def index(request):
    return render(request, "./task/index.html", {
        "tasks": tasks
    })
def addTask(request):
    if request.method == "POST":
        form = Taskform(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.append(task)
        else:
            return render(request,"task/addtask.html",{
                "form": form
            })
    return render(request,"./task/addtask.html",{
        "form":Taskfor()
    })

