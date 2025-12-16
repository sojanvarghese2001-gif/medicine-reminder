from django.db import models

class Alarm(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    enabled = models.BooleanField(default=True)
    triggered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} at {self.date} {self.time}"
