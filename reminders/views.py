from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Reminder
from .forms import ReminderForm

@login_required
def reminder_list(request):
    reminders = Reminder.objects.filter(user=request.user).order_by("-reminder_time")
    return render(request, "reminders/reminder_list.html", {"reminders": reminders})

@login_required
def reminder_create(request):
    if request.method == "POST":
        form = ReminderForm(request.POST)
        if form.is_valid():
            reminder = form.save(commit=False)
            reminder.user = request.user
            reminder.save()
            return redirect("reminders")
    else:
        form = ReminderForm()
    return render(request, "reminders/reminder_form.html", {"form": form})

@login_required
def reminder_update(request, reminder_id):
    reminder = get_object_or_404(Reminder, id=reminder_id, user=request.user)
    if request.method == "POST":
        form = ReminderForm(request.POST, instance=reminder)
        if form.is_valid():
            form.save()
            return redirect("reminders")
    else:
        form = ReminderForm(instance=reminder)
    return render(request, "reminders/reminder_form.html", {"form": form})

@login_required
def reminder_delete(request, reminder_id):
    reminder = get_object_or_404(Reminder, id=reminder_id, user=request.user)
    if request.method == "POST":
        reminder.delete()
        return redirect("reminders")
    return render(request, "reminders/reminder_confirm_delete.html", {"reminder": reminder})
