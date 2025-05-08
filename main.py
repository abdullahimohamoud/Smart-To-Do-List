# Smart To-Do List with Voice Command (Backend-Only)
#
# Description:
# This Python project is a voice-enabled to-do list application that allows users to manage tasks using spoken commands. It recognizes voice inputs for adding, updating, and deleting tasks, and responds with audio feedback. Tasks are stored locally with attributes like name, status, priority, and deadline. The app also provides desktop notifications for due tasks. No GUI or web front-end is included—this is a backend-only productivity tool for local desktop use.
#
# Features:
# - Voice command recognition (add, complete, delete tasks)
# - Text-to-speech feedback
# - Task management with priority and deadline
# - Desktop notifications for due tasks
# - Local file storage (tasks.json)
#
# Copyright (c) 2025 made with love by @uncannystranger

from voice_interface import VoiceInterface
from task_manager import TaskManager
from notifier import Notifier
from datetime import datetime, timedelta
import re

def parse_command(command):
    if not command:
        return None, None
    # Add task
    add_match = re.match(r"add task (.+?)(?: priority (\w+))?(?: deadline (.+))?$", command)
    if add_match:
        name = add_match.group(1)
        priority = add_match.group(2) or "normal"
        deadline_str = add_match.group(3)
        deadline = None
        if deadline_str:
            if deadline_str == "tomorrow":
                deadline = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
            else:
                try:
                    deadline = datetime.strptime(deadline_str, "%Y-%m-%d").strftime("%Y-%m-%d")
                except Exception:
                    deadline = None
        return "add", {"name": name, "priority": priority, "deadline": deadline}
    # Mark complete
    mark_match = re.match(r"mark complete (.+)", command)
    if mark_match:
        return "complete", {"name": mark_match.group(1)}
    # Delete task
    delete_match = re.match(r"delete task (\d+)", command)
    if delete_match:
        return "delete", {"id": int(delete_match.group(1))}
    return None, None

def main():
    vi = VoiceInterface()
    tm = TaskManager()
    notifier = Notifier()
    vi.speak("Welcome to your smart to-do list. Say a command.")
    vi.speak("Say: add task, mark complete, or delete task.")
    while True:
        command = vi.listen()
        if command:
            cmd_clean = command.strip().lower().rstrip('.!?,')
            if cmd_clean in ["stop listening", "exit", "quit", "stop"]:
                vi.speak("Goodbye! Stopping the to-do list.")
                break
        action, params = parse_command(command)
        if action == "add":
            task = tm.add_task(params["name"], params["priority"], params["deadline"])
            vi.speak(f"Task added: {task['name']}")
            if task["deadline"]:
                notifier.notify("Task Added", f"{task['name']} due {task['deadline']}")
        elif action == "complete":
            task = tm.mark_complete(params["name"])
            if task:
                vi.speak(f"Task marked complete: {task['name']}")
            else:
                vi.speak("Task not found.")
        elif action == "delete":
            task = tm.delete_task(params["id"])
            if task:
                vi.speak(f"Task deleted: {task['name']}")
            else:
                vi.speak("Task not found.")
        else:
            vi.speak("Please say a valid command.")
        # Notify for due tasks
        due_tasks = tm.get_due_tasks()
        for task in due_tasks:
            notifier.notify("Task Due", f"{task['name']} is due!")

if __name__ == "__main__":
    main()
