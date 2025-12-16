from django.shortcuts import render, redirect
from .models import Alarm
from datetime import datetime
from django.http import JsonResponse

def index(request):
    alarms = Alarm.objects.all().order_by("date", "time")
    return render(request, "index.html", {"alarms": alarms})

def add_alarm(request):
    if request.method == "POST":
        Alarm.objects.create(
            date=request.POST["alarm_date"],
            time=request.POST["alarm_time"],
            name=request.POST["medicine_name"],
        )
    return redirect("/")
def check_alarm(request):
    now = datetime.now()
    alarms = Alarm.objects.filter(enabled=True, date=now.date(), time=now.time().replace(second=0, microsecond=0))

    if alarms.exists():
        return JsonResponse({"ring": True})
    return JsonResponse({"ring": False})

def toggle_alarm(request, alarm_id):
    alarm = Alarm.objects.get(id=alarm_id)
    alarm.enabled = not alarm.enabled
    alarm.save()
    return redirect("/")

def delete_alarm(request, alarm_id):
    Alarm.objects.get(id=alarm_id).delete()
    return redirect("/")
def check_alarm(request):
    now = datetime.now()
    now_time = now.time().replace(second=0, microsecond=0)

    alarm = Alarm.objects.filter(
        enabled=True,
        date=now.date(),
        time=now_time
    ).first()

    if alarm:
        return JsonResponse({
            "ring": True,
            "name": alarm.name   # send medicine name
        })

    return JsonResponse({"ring": False})

