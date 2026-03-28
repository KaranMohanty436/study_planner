# study_planner
Smart AI Trip Planner for personalized travel experiences
# 📚 Study Planner with Pomodoro Timer
A modern Tkinter-based application that combines task management with the proven Pomodoro Technique for effective studying.

---

## 🎯 Features

### ✅ Task Management
- **Add Tasks**: Easily add study tasks with a simple input field
- **Task List**: View all your tasks in an organized list
- **Mark Complete**: Check off completed tasks with a visual checkmark (✓)
- **Delete Tasks**: Remove tasks you no longer need
- **Task Persistence**: Tasks are automatically saved to a JSON file and loaded on startup
- **Progress Tracking**: See how many tasks you've completed today

### ⏱️ Pomodoro Timer
- **25-Minute Study Sessions**: Focus on work with timed intervals
- **5-Minute Breaks**: Rest and recharge between sessions
- **Auto-Switch**: Automatically switches between study and break modes
- **Full Controls**: Start, Pause, and Reset buttons for complete control
- **Session Notifications**: Popup alerts when timer completes

### 🎨 Modern UI
- Clean, professional interface with intuitive layout
- Color-coded elements for easy navigation
- Large timer display for visibility
- Responsive button controls
- Completed tasks shown in green for visual feedback

---

## 📋 Requirements

### System Requirements
- Python 3.6 or higher
- Tkinter (usually comes pre-installed with Python)

### No External Dependencies!
This application uses only Python's standard library:
- `tkinter` - GUI framework
- `json` - Task storage
- `os` - File management
- `datetime` - Date tracking

---

## 🚀 Installation & Running

### Step 1: Download the File
The file `study_planner.py` should be in your project directory.

### Step 2: Verify Python Installation
Open Command Prompt or PowerShell and check Python version:
```bash
python --version
```
You should see Python 3.6 or higher. If not, [install Python](https://www.python.org/downloads/)

### Step 3: Verify Tkinter Installation
```bash
python -m tkinter
```
A small window should appear. If it does, Tkinter is installed correctly. Close the window and proceed.

### Step 4: Run the Application
Navigate to the project directory and run:
```bash
python study_planner.py
```

**Alternative (if above doesn't work):**
```bash
python3 study_planner.py
```

---

## 📖 How to Use

### Adding Tasks
1. Type your task in the text field (e.g., "Complete Math homework")
2. Click the **"+ Add"** button or press Enter
3. Your task will appear in the list below

### Managing Tasks
- **Mark Completed**: Select a task and click **"✓ Mark Completed"** to check it off
- **Toggle Status**: Click again to unmark a completed task
- **Delete Task**: Select a task and click **"🗑 Delete Task"**

### Using the Pomodoro Timer

#### Starting a Session
1. Click **"▶ Start"** to begin a 25-minute study session
2. The timer will count down with minutes:seconds display
3. Work on your tasks without distractions

#### During a Session
- **Pause**: Click **"⏸ Pause"** to temporarily stop the timer
- **Resume**: Click **"▶ Start"** again to continue
- **Reset**: Click **"⟲ Reset"** to start over

#### When Timer Completes
1. A popup notification appears
2. Timer automatically switches to a 5-minute break
3. Take a break, then start the next session
4. After your break, the timer returns to study mode

### Tracking Progress
- The **"Completed: X/Y"** counter shows your daily progress
- Completed tasks display with a green checkmark (✓)

---

## 📁 File Structure

```
studentManageTime/
├── study_planner.py       # Main application file
├── tasks.json             # Auto-created: stores your tasks
└── README.md              # This file
```

### tasks.json Format
Tasks are stored in JSON format. You can view the file in any text editor:

```json
[
  {
    "text": "Complete Math homework",
    "completed": false,
    "created_date": "2026-03-27"
  },
  {
    "text": "Study for Biology exam",
    "completed": true,
    "created_date": "2026-03-27"
  }
]
```

---

## 🎮 Keyboard Shortcuts

| Action | How To Do It |
|--------|-------------|
| Add Task | Type in field + Click "Add" or Press Enter |
| Pause Timer | Click "⏸ Pause" button |
| Reset Timer | Click "⟲ Reset" button |
| Close App | Click X or use Quit option |

---

## 💡 Tips for Effective Study

### Pomodoro Technique Best Practices:
1. **Choose One Task**: Focus on a single task during each 25-minute session
2. **Eliminate Distractions**: Put your phone away, close unnecessary tabs
3. **Use Breaks Wisely**: During 5-minute breaks, take a walk or drink water
4. **Take Longer Breaks**: After 4 complete cycles, take a 15-30 minute break
5. **Track Your Progress**: Keep using the app to see your completed tasks grow

### Tips for Success:
- Start with realistic task estimates
- Break large tasks into smaller subtasks
- Review completed tasks weekly to build motivation
- Adjust your workflow based on what works best for you

---

## 🔧 Troubleshooting

### "python: command not found"
**Solution**: 
- Use `python3` instead of `python`
- Or [reinstall Python](https://www.python.org/downloads/) with "Add Python to PATH" checked

### Tkinter not found
**Solution** (depending on OS):
- **Windows**: Reinstall Python and make sure "tcl/tk and IDLE" is checked
- **Mac**: `brew install python-tk`
- **Linux**: `sudo apt-get install python3-tk`

### Tasks not saving
**Solution**:
- Check if you have write permissions in the directory
- Move the file to Documents or Desktop folder
- Restart the application

### Timer not working
**Solution**:
- Close and restart the application
- Make sure no background process is using excessive CPU

---

## 🛠️ Code Structure

The application is organized into logical sections:

```
1. Configuration & Constants
   - Timer durations (25 min study, 5 min break)
   - Color scheme
   - File paths

2. Task Management Functions
   - load_tasks()
   - save_tasks()
   - add_task()
   - delete_task()
   - mark_completed()
   - update_task_display()

3. Pomodoro Timer Functions
   - start_timer()
   - pause_timer()
   - reset_timer()
   - countdown()
   - timer_finished()
   - update_timer_display()

4. GUI Setup
   - Window configuration
   - Frame creation
   - Widget placement
   - Event handlers
```

---

## 🎨 Customization Guide

### Change Timer Duration
Edit these lines in `study_planner.py`:
```python
POMODORO_STUDY_TIME = 25 * 60  # Change 25 to your preferred minutes
POMODORO_BREAK_TIME = 5 * 60   # Change 5 to your preferred minutes
```

### Change Colors
Edit the color constants:
```python
COLOR_PRIMARY = "#4CAF50"       # Green (main buttons)
COLOR_ACCENT = "#2196F3"        # Blue (secondary buttons)
COLOR_WARNING = "#FF9800"       # Orange (delete, reset)
COLOR_SUCCESS = "#8BC34A"       # Light green (completed tasks)
```

### Adjust Window Size
Edit this line:
```python
root.geometry("700x900")  # Change to your preferred width x height
```

---

## 📊 Example Workflow

1. **Start your day**: Open Study Planner
2. **Add tasks**: Type in 3-5 tasks for today
3. **Pick first task**: Choose what you'll study for 25 minutes
4. **Start timer**: Click "▶ Start"
5. **Focus**: Study without distractions
6. **Timer ends**: Take a 5-minute break
7. **Repeat**: Continue with next task
8. **Mark complete**: Check off finished tasks
9. **Review progress**: Watch your completed count grow

---

## 🐛 Known Limitations

- Timer is not perfectly accurate (±1 second variation possible)
- Sound notifications require system audio configuration
- Maximum recommended window size: 1200x1000 pixels

---

## 📚 Learning Resources

### Pomodoro Technique
- [Official Pomodoro Technique](https://pomodorotechnique.com/)
- Helps improve focus and reduce burnout

### Tkinter Documentation
- [Python Tkinter Docs](https://docs.python.org/3/library/tkinter.html)
- [Tkinter Tutorial](https://docs.python.org/3/library/tkinter.html)

---

## 📝 License

This project is free to use and modify for educational and personal purposes.

---

## 🤝 Contributing

Feel free to enhance this application! Some ideas:
- Add sound notifications when timer ends
- Export task reports to PDF
- Add task categories and filters
- Sync tasks with cloud storage
- Create a statistics dashboard
- Add dark mode theme

---

## ❓ FAQ

**Q: Can I use this on Mac or Linux?**
A: Yes! The code works on all operating systems (Windows, Mac, Linux). Just run `python3 study_planner.py`

**Q: Will my tasks be saved if I close the app?**
A: Yes! Tasks are automatically saved to `tasks.json`. They'll load when you restart the app.

**Q: Can I use a different timer duration?**
A: Yes! Edit the `POMODORO_STUDY_TIME` and `POMODORO_BREAK_TIME` constants in the code.

**Q: What if Tkinter is not installed?**
A: See the Troubleshooting section above for installation instructions.

**Q: Can I run multiple instances of this app?**
A: Yes, but they'll share the same `tasks.json` file, so changes in one will affect the other.

---

## 📞 Support

If you encounter issues:
1. Check the Troubleshooting section
2. Verify all requirements are installed
3. Try closing and reopening the application
4. Check that you have write permissions in the directory

---

**Happy Studying! 🎓**

Remember: Consistency is key. Use the Pomodoro Technique daily to build better study habits!

