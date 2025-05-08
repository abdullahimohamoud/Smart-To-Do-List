# notifier.py
# Copyright (c) 2025 made with love by @uncannystranger
from plyer import notification

class Notifier:
    @staticmethod
    def notify(title, message):
        notification.notify(
            title=title,
            message=message,
            app_name="Smart To-Do List",
            timeout=5
        )
