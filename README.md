<<<<<<< HEAD
...your local content...
=======
...content from GitHub...
>>>>>>> main
# README.md
# Smart To-Do List with Voice Command (Backend-Only)

Copyright (c) 2025 made with love by @uncannystranger

## Features
- Voice command recognition (add, complete, delete tasks)
- Text-to-speech feedback
- Task management with priority and deadline
- Desktop notifications for due tasks
- Local file storage (tasks.json)

## Quick Start
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the app:
   ```bash
   python main.py
   ```
3. Speak commands like:
   - "Add task buy groceries priority high deadline tomorrow"
   - "Mark complete buy groceries"
   - "Delete task 2"

## File Structure
- main.py — Entry point, runs the voice command loop
- voice_interface.py — Speech recognition and TTS
- task_manager.py — Task CRUD and file storage
- notifier.py — Desktop notifications
- requirements.txt — Dependencies
- tasks.json — Task data (auto-created)

## Notes
- All data is stored locally in tasks.json.
- Notifications work on macOS via plyer.
- No GUI or web front-end included.

---
Made with love by @uncannystranger
=======
# Smart-To-Do-List
A Python voice-enabled to-do list app that lets users add, update, and delete tasks using speech. It recognizes commands, gives spoken feedback, and stores tasks locally with name, status, priority, and deadline. Includes desktop reminders. Fully backend—no GUI or web front-end required.
>>>>>>> 805dff673712e1476f1bc6ac4812f8e30233863b
