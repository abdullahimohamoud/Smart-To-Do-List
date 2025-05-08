# task_manager.py
# Copyright (c) 2025 made with love by @uncannystranger
import json
import os
from datetime import datetime, timedelta

TASKS_FILE = "tasks.json"

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, "r") as f:
                self.tasks = json.load(f)
        else:
            self.tasks = []

    def save_tasks(self):
        with open(TASKS_FILE, "w") as f:
            json.dump(self.tasks, f, indent=2)

    def add_task(self, name, priority="normal", deadline=None):
        task = {
            "id": len(self.tasks) + 1,
            "name": name,
            "status": "pending",
            "priority": priority,
            "deadline": deadline
        }
        self.tasks.append(task)
        self.save_tasks()
        return task

    def mark_complete(self, name):
        for task in self.tasks:
            if task["name"].lower() == name.lower():
                task["status"] = "complete"
                self.save_tasks()
                return task
        return None

    def delete_task(self, task_id):
        for i, task in enumerate(self.tasks):
            if task["id"] == task_id:
                removed = self.tasks.pop(i)
                self.save_tasks()
                return removed
        return None

    def get_due_tasks(self):
        due = []
        now = datetime.now()
        for task in self.tasks:
            if task["status"] == "pending" and task["deadline"]:
                try:
                    deadline = datetime.strptime(task["deadline"], "%Y-%m-%d")
                    if deadline <= now:
                        due.append(task)
                except Exception:
                    continue
        return due
