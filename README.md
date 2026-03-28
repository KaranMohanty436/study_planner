# study_planner
Smart AI Trip Planner for personalized travel experiences
# 📚 Study Planner with Pomodoro Timer

A modern Tkinter-based application that combines task management with the proven Pomodoro Technique for effective studying.

---

## 🎯 Features

### 🔐 User Authentication (NEW!)
- **Registration**: Create account with phone number, email, and password
- **Login**: Secure login with phone and password
- **Data Security**: User credentials stored in users.json
- **Unique Accounts**: Prevents duplicate phone number registration

### ⚙️ Custom Timer Settings (NEW!)
- **Flexible Study Time**: Set study duration from 1 to 120 minutes (default 25)
- **Flexible Break Time**: Set break duration from 1 to 60 minutes (default 5)
- **Apply Button**: Instantly update timer with custom settings
- **Auto-Switch**: Automatically switches between custom study and break modes
- **Real-time Updates**: Changes apply immediately

### ✅ Task Management
- **Add Tasks**: Easily add study tasks with a simple input field
- **Task List**: View all your tasks in an organized list
- **Mark Complete**: Check off completed tasks with a visual checkmark (✓)
- **Delete Tasks**: Remove tasks you no longer need
- **Task Persistence**: Tasks are automatically saved to a JSON file and loaded on startup
- **Progress Tracking**: See how many tasks you've completed today

### ⏱️ Pomodoro Timer
- **Customizable Study Sessions**: Study time from 1-120 minutes (default 25)
- **Customizable Breaks**: Break time from 1-60 minutes (default 5)
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

### 🔐 Login & Registration

**First Time Users:**
1. Application opens with Login screen
2. Click **"✍️ Create Account"**
3. Fill in details:
   - 📱 **Phone Number**: 10+ digits (e.g., 9876543210)
   - 📧 **Email**: Valid email (e.g., user@example.com)
   - 🔒 **Password**: Minimum 6 characters
   - 🔒 **Confirm Password**: Must match
4. Click **"✓ Register"**
5. Now login with phone and password

**Returning Users:**
1. Enter your phone number
2. Enter your password
3. Click **"▶ Login"**
4. Main app opens! 🎉

### ⚙️ Custom Timer Settings

**Change Study Time:**
1. Look for **"⚙️ Timer Settings"** section
2. Find **"📚 Study Time (min)"** spinbox
3. Change value (1-120 minutes)
   - Example: 45, 60, 90 minutes
4. Click **"✓ Apply"** button
5. New time takes effect immediately!

**Change Break Time:**
1. Find **"☕ Break Time (min)"** spinbox
2. Change value (1-60 minutes)
   - Example: 10, 15, 20 minutes
3. Click **"✓ Apply"** button
4. New break duration set!

**Examples:**
- Short focus: 20 min study + 5 min break
- Normal: 25 min study + 5 min break (default)
- Extended: 45 min study + 15 min break
- Deep work: 90 min study + 20 min break

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
1. (Optional) Set custom timer in **"⚙️ Timer Settings"**
2. Click **"▶ Start"** to begin study session
3. The timer will count down with minutes:seconds display
4. Work on your tasks without distractions

#### During a Session
- **Pause**: Click **"⏸ Pause"** to temporarily stop the timer
- **Resume**: Click **"▶ Start"** again to continue
- **Reset**: Click **"⟲ Reset"** to start over
- **Change Timer**: Update spinbox values and click **"✓ Apply"**

#### When Timer Completes
1. A popup notification appears
2. Timer automatically switches to break time
3. Take a break (your custom break duration)
4. After break, timer returns to study mode
5. Ready for next session!

### Tracking Progress
- The **"Completed: X/Y"** counter shows your daily progress
- Completed tasks display with a green checkmark (✓)

---

## 📁 File Structure

```
studentManageTime/
├── study_planner.py       # Main application file
├── tasks.json             # Auto-created: stores your tasks
├── users.json             # Auto-created: stores user accounts
└── README.md              # This file
```

### tasks.json Format
Tasks are stored in JSON format:

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

### users.json Format
User accounts are stored securely:

```json
{
  "9876543210": {
    "email": "user@example.com",
    "password": "123456",
    "created": "2026-03-28T20:18:00"
  }
}
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

### Customizing Timer:
1. **Short Focus**: Set 20 min study + 5 min break for quick review
2. **Normal Pomodoro**: Use default 25 min + 5 min (proven technique)
3. **Extended Study**: 45 min study + 15 min break for deep work
4. **Deep Work**: 90 min study + 20 min break for complex topics
5. **Adjust Anytime**: Change timer before or after each session

### Pomodoro Technique Best Practices:
1. **Choose One Task**: Focus on a single task during each study session
2. **Eliminate Distractions**: Put your phone away, close unnecessary tabs
3. **Use Breaks Wisely**: During breaks, take a walk or drink water
4. **Take Longer Breaks**: After 4 complete cycles, take a 15-30 minute break
5. **Track Your Progress**: Keep using the app to see your completed tasks grow

### Tips for Success:
- Start with realistic task estimates
- Break large tasks into smaller subtasks
- Review completed tasks weekly to build motivation
- Experiment with different timer durations to find what works best for you
- Use the custom timer feature to match your focus capacity

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

### First Time:
1. **Open app**: `python study_planner.py`
2. **Create account**: Phone, email, password
3. **Login**: Use your phone & password
4. **Main app opens**: Ready to study!

### Daily Usage:
1. **Login**: Enter phone and password
2. **Add tasks**: "Chapter 5 math", "Physics revision", etc.
3. **Set timer** (optional): Change to 45 min study + 15 min break
4. **Start first task**: Click "▶ Start"
5. **Focus**: Study without distractions
6. **Break**: Auto-switches to break time
7. **Next session**: Click "▶ Start" again
8. **Mark complete**: Check off finished tasks
9. **Review progress**: Watch your completed count grow

### Example Timer Configurations:
| Session Type | Study Time | Break Time | Best For |
|---|---|---|---|
| Quick Review | 20 min | 5 min | Fast topics |
| Standard | 25 min | 5 min | Most studying |
| Extended | 45 min | 15 min | Complex topics |
| Deep Work | 90 min | 20 min | Programming |
| Marathon | 120 min | 30 min | Research/Writing |

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

**Q: How do I change the timer duration?**
A: Use the **⚙️ Timer Settings** section! Change "Study (min)" or "Break (min)" and click "✓ Apply". No need to edit code!

**Q: Can I use different timer durations for different tasks?**
A: Yes! Update the settings before each study session.

**Q: What's the maximum timer duration?**
A: Study time: 1-120 minutes, Break time: 1-60 minutes.

**Q: Do I need to apply timer settings every session?**
A: No! Settings stay saved until you change them again.

**Q: What if I forgot my password?**
A: Currently, delete `users.json` file and register a new account. (Future improvement: password reset feature)

**Q: Can I change the timer while studying?**
A: Yes! Change the values and click "✓ Apply" - it updates immediately.

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



**Happy Studying! 🎓**

Remember: Consistency is key. Use the Pomodoro Technique daily to build better study habits!

