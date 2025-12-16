from django.apps import AppConfig
import threading
import time
from datetime import datetime


class MedicineAppConfig(AppConfig):
    name = 'myapp'

    def ready(self):
        # Start background thread only once
        if not hasattr(self, 'already_started'):
            self.already_started = True
            threading.Thread(target=self.check_alarm, daemon=True).start()

    def check_alarm(self):
        # Import models ONLY here (safe)
        from .models import Alarm

        while True:
            now_date = datetime.now().date()
            now_time = datetime.now().strftime("%H:%M")

            alarms = Alarm.objects.filter(enabled=True)

            for alarm in alarms:
                alarm_time = alarm.time.strftime("%H:%M")

                if alarm.date == now_date and alarm_time == now_time and not alarm.triggered:
                    print(f"🔔 TAKE MEDICINE: {alarm.name}")
                    alarm.triggered = True
                    alarm.save()

            time.sleep(1)
