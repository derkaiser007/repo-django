from django.shortcuts import render

tasks = ["eat", "exercise", "program"]
# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })
