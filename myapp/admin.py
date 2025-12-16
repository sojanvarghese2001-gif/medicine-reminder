from django.contrib import admin
from .models import Alarm


@admin.register(Alarm)
class AlarmAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'time', 'enabled', 'triggered')
    list_filter = ('enabled', 'date')
    search_fields = ('name',)
