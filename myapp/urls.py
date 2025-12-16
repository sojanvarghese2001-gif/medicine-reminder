from django.urls import path
from . import views
from .views import check_alarm

urlpatterns = [
    path("", views.index),
    path("add_alarm", views.add_alarm),
    path("toggle/<int:alarm_id>", views.toggle_alarm),
    path("delete/<int:alarm_id>", views.delete_alarm),
    path("check_alarm/", check_alarm)
]
