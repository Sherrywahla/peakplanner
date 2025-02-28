from django.shortcuts import render
from notes.models import Note
from reminders.models import Reminder
from tasks.models import Task
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    tasks = Task.objects.filter(user=request.user)[:5]
    notes = Note.objects.filter(user=request.user)[:5]
    reminders = Reminder.objects.filter(user=request.user)[:5]
    
    return render(request, "dashboard/dashboard.html", {
        "tasks": tasks,
        "notes": notes,
        "reminders": reminders
    })

