"""
Study Planner with Pomodoro Timer
A Tkinter-based application to manage study tasks and track time using the Pomodoro technique.
"""

import tkinter as tk
from tkinter import messagebox, font
import json
import os
from datetime import datetime

# Try import winsound for Windows alarm sound
try:
    import winsound
except ImportError:
    winsound = None

# =============================================
# Configuration and Constants
# =============================================
TASKS_FILE = "tasks.json"
USERS_FILE = "users.json"
DEFAULT_STUDY_TIME = 25  # Default study time in minutes
DEFAULT_BREAK_TIME = 5   # Default break time in minutes

# Color scheme for modern UI
COLOR_BG = "#f0f0f0"           # Light gray background
COLOR_PRIMARY = "#4CAF50"       # Green for primary actions
COLOR_ACCENT = "#2196F3"        # Blue for secondary actions
COLOR_WARNING = "#FF9800"       # Orange for warnings
COLOR_SUCCESS = "#8BC34A"       # Light green for completed tasks
COLOR_TEXT = "#333333"          # Dark text

# =============================================
# User Authentication Functions
# =============================================

def load_users():
    """Load users from JSON file."""
    if os.path.exists(USERS_FILE):
        try:
            with open(USERS_FILE, 'r') as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError):
            return {}
    return {}

def save_users(users):
    """Save users to JSON file."""
    try:
        with open(USERS_FILE, 'w') as file:
            json.dump(users, file, indent=2)
    except IOError as e:
        messagebox.showerror("Error", f"Failed to save: {e}")

def is_valid_email(email):
    """Validate email format."""
    return "@" in email and "." in email.split("@")[1] if "@" in email else False

def is_valid_phone(phone):
    """Validate phone number (10 digits)."""
    return phone.isdigit() and len(phone) >= 10

def register_user():
    """Register a new user."""
    phone = entry_reg_phone.get().strip()
    username = entry_reg_username.get().strip()
    email = entry_reg_email.get().strip()
    password = entry_reg_password.get().strip()
    confirm_password = entry_reg_confirm.get().strip()

    # Validation
    if not phone or not username or not email or not password or not confirm_password:
        messagebox.showwarning("Empty Fields", "Please fill all fields!")
        return
    
    if not is_valid_phone(phone):
        messagebox.showwarning("Invalid Phone", "Phone number must be at least 10 digits!")
        return
    
    if not is_valid_email(email):
        messagebox.showwarning("Invalid Email", "Please enter a valid email address!")
        return

    if len(username) < 3:
        messagebox.showwarning("Invalid Username", "Username must be at least 3 characters!")
        return

    if password != confirm_password:
        messagebox.showwarning("Password Mismatch", "Passwords don't match!")
        return

    if len(password) < 6:
        messagebox.showwarning("Weak Password", "Password must be at least 6 characters!")
        return

    users = load_users()
    
    # Check if user already exists
    if phone in users:
        messagebox.showwarning("User Exists", "Phone number already registered!")
        return
    
    # Save new user
    users[phone] = {
        "username": username,
        "email": email,
        "password": password,
        "created": datetime.now().isoformat()
    }
    save_users(users)
    
    messagebox.showinfo("Success", "Account created! Please login.")
    show_login_screen()

def login_user():
    """Login user."""
    phone = entry_login_phone.get().strip()
    password = entry_login_password.get().strip()

    if not phone or not password:
        messagebox.showwarning("Empty Fields", "Enter phone and password!")
        return

    users = load_users()

    if phone not in users:
        messagebox.showerror("Error", "User not found! Please register.")
        return

    if users[phone]["password"] != password:
        messagebox.showerror("Error", "Wrong password!")
        return

    global current_user, tasks, tasks_data
    current_user = phone
    tasks_data = load_tasks()
    tasks = tasks_data.get(current_user, [])

    messagebox.showinfo("Success", f"Welcome back, {users[phone].get('username', users[phone]['email'])}! 👋")
    destroy_login_screen()
    root.deiconify()

    populate_profile_section()
    update_task_display()
    update_timer_display()


def logout_user():
    """Logout current user and show login window."""
    global current_user, tasks
    if messagebox.askyesno("Logout", "Do you want to logout?"):
        current_user = None
        tasks = []
        root.withdraw()
        show_login_window()


def change_password():
    """Open change password window."""
    if not current_user:
        messagebox.showerror("Error", "No user logged in.")
        return

    def do_change():
        current_pass = entry_current.get().strip()
        new_pass = entry_new.get().strip()
        confirm_new = entry_confirm.get().strip()

        users = load_users()
        user = users.get(current_user)

        if not user or user['password'] != current_pass:
            messagebox.showerror("Error", "Current password is wrong.")
            return

        if len(new_pass) < 6:
            messagebox.showwarning("Weak Password", "Password must be at least 6 characters!")
            return

        if new_pass != confirm_new:
            messagebox.showwarning("Mismatch", "New passwords do not match.")
            return

        user['password'] = new_pass
        save_users(users)
        messagebox.showinfo("Success", "Password changed successfully.")
        win.destroy()

    win = tk.Toplevel(root)
    win.title("Change Password")
    win.geometry("350x260")
    win.resizable(False, False)

    tk.Label(win, text="🔒 Change Password", font=("Arial", 14, "bold")).pack(pady=10)

    tk.Label(win, text="Current Password:").pack(anchor="w", padx=20, pady=(5, 0))
    entry_current = tk.Entry(win, show="●", width=30)
    entry_current.pack(padx=20, pady=5)

    tk.Label(win, text="New Password:").pack(anchor="w", padx=20, pady=(5, 0))
    entry_new = tk.Entry(win, show="●", width=30)
    entry_new.pack(padx=20, pady=5)

    tk.Label(win, text="Confirm New Password:").pack(anchor="w", padx=20, pady=(5, 0))
    entry_confirm = tk.Entry(win, show="●", width=30)
    entry_confirm.pack(padx=20, pady=5)

    tk.Button(win, text="Update", command=do_change, bg=COLOR_PRIMARY, fg="white", width=20).pack(pady=10)


def show_profile_window():
    """Show user profile details."""
    if not current_user:
        messagebox.showerror("Error", "No user logged in")
        return

    users = load_users()
    user = users.get(current_user, {})

    win = tk.Toplevel(root)
    win.title("User Profile")
    win.geometry("380x220")
    win.resizable(False, False)

    tk.Label(win, text="👤 User Profile", font=("Arial", 16, "bold")).pack(pady=10)
    tk.Label(win, text=f"Phone: {current_user}", font=("Arial", 11)).pack(anchor="w", padx=20, pady=2)
    tk.Label(win, text=f"Username: {user.get('username', 'N/A')}", font=("Arial", 11)).pack(anchor="w", padx=20, pady=2)
    tk.Label(win, text=f"Email: {user.get('email', 'N/A')}", font=("Arial", 11)).pack(anchor="w", padx=20, pady=2)
    tk.Label(win, text=f"Created: {user.get('created', 'N/A')}", font=("Arial", 11)).pack(anchor="w", padx=20, pady=2)

    tk.Button(win, text="Change Password", command=change_password, bg=COLOR_ACCENT, fg="white", width=18).pack(pady=(10, 2))
    tk.Button(win, text="Close", command=win.destroy, width=12).pack(pady=5)


def populate_profile_section():
    """Populate the profile details area in main window."""
    if current_user:
        users = load_users()
        user = users.get(current_user, {})
        label_profile_info.config(text=f"Logged in as {user.get('username', 'Unknown')} ({current_user})")
        button_profile.config(state=tk.NORMAL)
        button_logout.config(state=tk.NORMAL)
    else:
        label_profile_info.config(text="Not logged in")
        button_profile.config(state=tk.DISABLED)
        button_logout.config(state=tk.DISABLED)


def show_registration_screen():
    """Show registration screen."""
    global frame_login_main
    
    # Clear login frame
    for widget in frame_login_main.winfo_children():
        widget.destroy()
    
    # Registration title
    label_reg_title = tk.Label(frame_login_main, text="📝 Create Account", 
                              font=("Arial", 20, "bold"), fg=COLOR_PRIMARY, bg="white")
    label_reg_title.pack(pady=20)
    
    # Phone
    tk.Label(frame_login_main, text="📱 Phone Number:", font=("Arial", 11), 
            fg=COLOR_TEXT, bg="white").pack(anchor="w", padx=30, pady=(10, 0))
    global entry_reg_phone
    entry_reg_phone = tk.Entry(frame_login_main, font=("Arial", 11), width=30, 
                              relief=tk.SOLID, bd=2, bg="white", fg=COLOR_TEXT)
    entry_reg_phone.pack(padx=30, pady=(0, 15), ipady=8)
    entry_reg_phone.focus()

    # Username
    tk.Label(frame_login_main, text="👤 Username:", font=("Arial", 11), 
            fg=COLOR_TEXT, bg="white").pack(anchor="w", padx=30, pady=(10, 0))
    global entry_reg_username
    entry_reg_username = tk.Entry(frame_login_main, font=("Arial", 11), width=30, 
                                 relief=tk.SOLID, bd=2, bg="white", fg=COLOR_TEXT)
    entry_reg_username.pack(padx=30, pady=(0, 15), ipady=8)

    # Email
    tk.Label(frame_login_main, text="📧 Email:", font=("Arial", 11), 
            fg=COLOR_TEXT, bg="white").pack(anchor="w", padx=30, pady=(10, 0))
    global entry_reg_email
    entry_reg_email = tk.Entry(frame_login_main, font=("Arial", 11), width=30, 
                              relief=tk.SOLID, bd=2, bg="white", fg=COLOR_TEXT)
    entry_reg_email.pack(padx=30, pady=(0, 15), ipady=8)
    
    # Password
    tk.Label(frame_login_main, text="🔒 Password:", font=("Arial", 11), 
            fg=COLOR_TEXT, bg="white").pack(anchor="w", padx=30, pady=(10, 0))
    global entry_reg_password
    entry_reg_password = tk.Entry(frame_login_main, font=("Arial", 11), width=30, 
                                 relief=tk.SOLID, bd=2, bg="white", fg=COLOR_TEXT, show="●")
    entry_reg_password.pack(padx=30, pady=(0, 15), ipady=8)
    
    # Confirm Password
    tk.Label(frame_login_main, text="🔒 Confirm Password:", font=("Arial", 11),
            fg=COLOR_TEXT, bg="white").pack(anchor="w", padx=30, pady=(10, 0))
    global entry_reg_confirm
    entry_reg_confirm = tk.Entry(frame_login_main, font=("Arial", 11), width=30,
                                relief=tk.SOLID, bd=2, bg="white", fg=COLOR_TEXT, show="●")
    entry_reg_confirm.pack(padx=30, pady=(0, 20), ipady=8)
    
    # Register button
    tk.Button(frame_login_main, text="✓ Register", command=register_user,
             bg=COLOR_PRIMARY, fg="white", font=("Arial", 12, "bold"),
             width=30, relief=tk.FLAT).pack(padx=30, pady=10, ipady=8)
    
    # Back to login
    tk.Button(frame_login_main, text="← Back to Login", command=show_login_screen,
             bg=COLOR_ACCENT, fg="white", font=("Arial", 10),
             width=30, relief=tk.FLAT).pack(padx=30, pady=5, ipady=6)

def show_login_screen():
    """Show login screen."""
    global frame_login_main
    
    # Clear frame
    for widget in frame_login_main.winfo_children():
        widget.destroy()
    
    # Login title
    label_login_title = tk.Label(frame_login_main, text="🔐 Login", 
                               font=("Arial", 20, "bold"), fg=COLOR_PRIMARY, bg="white")
    label_login_title.pack(pady=20)
    
    # Phone
    tk.Label(frame_login_main, text="📱 Phone Number:", font=("Arial", 11),
            fg=COLOR_TEXT, bg="white").pack(anchor="w", padx=30, pady=(10, 0))
    global entry_login_phone
    entry_login_phone = tk.Entry(frame_login_main, font=("Arial", 11), width=30, 
                                relief=tk.SOLID, bd=2, bg="white", fg=COLOR_TEXT)
    entry_login_phone.pack(padx=30, pady=(0, 15), ipady=8)
    entry_login_phone.focus()
    
    # Password
    tk.Label(frame_login_main, text="🔒 Password:", font=("Arial", 11),
            fg=COLOR_TEXT, bg="white").pack(anchor="w", padx=30, pady=(10, 0))
    global entry_login_password
    entry_login_password = tk.Entry(frame_login_main, font=("Arial", 11), width=30,
                                   relief=tk.SOLID, bd=2, bg="white", fg=COLOR_TEXT, show="●")
    entry_login_password.pack(padx=30, pady=(0, 20), ipady=8)
    
    # Login button
    tk.Button(frame_login_main, text="▶ Login", command=login_user,
             bg=COLOR_PRIMARY, fg="white", font=("Arial", 12, "bold"),
             width=30, relief=tk.FLAT).pack(padx=30, pady=10, ipady=8)
    
    # Register button
    tk.Button(frame_login_main, text="✍️ Create Account", command=show_registration_screen,
             bg=COLOR_ACCENT, fg="white", font=("Arial", 10),
             width=30, relief=tk.FLAT).pack(padx=30, pady=5, ipady=6)

def show_login_window():
    """Show login/registration window."""
    global login_root, frame_login_main
    
    login_root = tk.Tk()
    login_root.title("Study Planner - Login")
    login_root.geometry("500x650")
    login_root.config(bg=COLOR_BG)
    
    # Header
    frame_header = tk.Frame(login_root, bg=COLOR_PRIMARY, height=80)
    frame_header.pack(fill=tk.X)
    frame_header.pack_propagate(False)
    
    label_header = tk.Label(frame_header, text="📚 Study Planner", 
                           font=("Arial", 24, "bold"), fg="white", bg=COLOR_PRIMARY)
    label_header.pack(pady=20)
    
    # Main login frame
    frame_login_main = tk.Frame(login_root, bg="white", relief=tk.RAISED, bd=2)
    frame_login_main.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
    
    # Show login screen
    show_login_screen()
    
    def on_closing():
        login_root.destroy()
        exit()
    
    login_root.protocol("WM_DELETE_WINDOW", on_closing)
    login_root.mainloop()

def destroy_login_screen():
    """Close login window."""
    if 'login_root' in globals():
        login_root.destroy()

# =============================================
# Task Management Functions
# =============================================

def load_tasks():
    """Load tasks from JSON file."""
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, 'r') as file:
                data = json.load(file)
                if isinstance(data, list):
                    return {"__default__": data}
                if isinstance(data, dict):
                    return data
        except (json.JSONDecodeError, IOError):
            return {}
    return {}


def save_tasks(task_data):
    """Save tasks to JSON file."""
    try:
        with open(TASKS_FILE, 'w') as file:
            json.dump(task_data, file, indent=2)
    except IOError as e:
        messagebox.showerror("Error", f"Failed to save tasks: {e}")


def set_user_tasks(new_tasks):
    """Set tasks for the current user and save."""
    global tasks_data, current_user
    if current_user is None:
        return
    tasks_data[current_user] = new_tasks
    save_tasks(tasks_data)


def add_task():
    """Add a new task to the list."""
    task_text = entry_task.get().strip()
    
    if not task_text:
        messagebox.showwarning("Empty Task", "Please enter a task before adding.")
        return
    
    # Create new task object
    new_task = {
        "text": task_text,
        "completed": False,
        "created_date": datetime.now().strftime("%Y-%m-%d")
    }
    
    # Add to global tasks list and save
    tasks.append(new_task)
    set_user_tasks(tasks)
    
    # Clear entry and refresh display
    entry_task.delete(0, tk.END)
    update_task_display()
    messagebox.showinfo("Success", "Task added successfully!")

def delete_task():
    """Delete the selected task from the list."""
    try:
        selected_index = listbox_tasks.curselection()
        if not selected_index:
            messagebox.showwarning("No Selection", "Please select a task to delete.")
            return
        
        # Remove task from list and save
        tasks.pop(selected_index[0])
        set_user_tasks(tasks)
        update_task_display()
        messagebox.showinfo("Success", "Task deleted successfully!")
    except IndexError:
        messagebox.showerror("Error", "Failed to delete task.")

def mark_completed():
    """Mark the selected task as completed."""
    try:
        selected_index = listbox_tasks.curselection()
        if not selected_index:
            messagebox.showwarning("No Selection", "Please select a task to mark as completed.")
            return
        
        # Toggle completion status
        task_index = selected_index[0]
        tasks[task_index]["completed"] = not tasks[task_index]["completed"]
        set_user_tasks(tasks)
        update_task_display()
        
        status = "completed" if tasks[task_index]["completed"] else "marked as incomplete"
        messagebox.showinfo("Success", f"Task {status}!")
    except IndexError:
        messagebox.showerror("Error", "Failed to update task status.")

def update_task_display():
    """Update the task listbox with current tasks and completion status."""
    listbox_tasks.delete(0, tk.END)
    completed_count = 0
    
    for i, task in enumerate(tasks):
        # Format task with checkmark or empty box
        status_symbol = "✓" if task["completed"] else "○"
        display_text = f"[{status_symbol}] {task['text']}"
        
        # Add to listbox
        listbox_tasks.insert(tk.END, display_text)
        
        # Color completed tasks differently
        if task["completed"]:
            listbox_tasks.itemconfig(i, {"fg": COLOR_SUCCESS, "bg": "#f5f5f5"})
            completed_count += 1
        else:
            listbox_tasks.itemconfig(i, {"fg": COLOR_TEXT})
    
    # Update completed task counter
    label_completed.config(text=f"Completed: {completed_count}/{len(tasks)}")


def play_alarm():
    """Play a sound when timer completes."""
    try:
        if winsound:
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
        else:
            root.bell()
    except Exception:
        try:
            root.bell()
        except Exception:
            pass


# =============================================
# Pomodoro Timer Functions
# =============================================

def start_timer():
    """Start the Pomodoro timer."""
    global timer_running, remaining_time
    
    if timer_running:
        return
    
    timer_running = True
    button_start.config(state=tk.DISABLED)
    button_pause.config(state=tk.NORMAL)
    
    # Start countdown
    countdown()

def pause_timer():
    """Pause the Pomodoro timer."""
    global timer_running
    timer_running = False
    button_start.config(state=tk.NORMAL)
    button_pause.config(state=tk.DISABLED)

def reset_timer():
    """Reset the Pomodoro timer."""
    global timer_running, remaining_time, is_study_session
    
    timer_running = False
    remaining_time = study_time_minutes.get() * 60
    is_study_session = True
    
    # Reset UI
    button_start.config(state=tk.NORMAL)
    button_pause.config(state=tk.DISABLED)
    label_session_type.config(text="Study Session", fg=COLOR_PRIMARY)
    update_timer_display()

def countdown():
    """Handle the countdown logic."""
    global timer_running, remaining_time, is_study_session
    
    if not timer_running:
        return
    
    if remaining_time > 0:
        remaining_time -= 1
        update_timer_display()
        # Schedule next update (1000 ms = 1 second)
        root.after(1000, countdown)
    else:
        # Timer finished
        timer_finished()

def timer_finished():
    """Handle timer completion."""
    global timer_running, remaining_time, is_study_session
    
    timer_running = False
    play_alarm()
    
    if is_study_session:
        # Switch to break session
        messagebox.showinfo("Timer Complete! 🎉", 
                          "Study session complete! Time for a break.")
        is_study_session = False
        remaining_time = break_time_minutes.get() * 60
        label_session_type.config(text="Break Time", fg=COLOR_WARNING)
    else:
        # Switch back to study session
        messagebox.showinfo("Break Complete! 📚", 
                          "Break is over! Ready for another study session?")
        is_study_session = True
        remaining_time = study_time_minutes.get() * 60
        label_session_type.config(text="Study Session", fg=COLOR_PRIMARY)
    
    update_timer_display()
    button_start.config(state=tk.NORMAL)
    button_pause.config(state=tk.DISABLED)

def update_timer_display():
    """Update the timer display on the label."""
    minutes = remaining_time // 60
    seconds = remaining_time % 60
    time_text = f"{minutes:02d}:{seconds:02d}"
    label_timer.config(text=time_text)

# =============================================
# Main Window Setup
# =============================================

# Global variables
current_user = None
tasks_data = load_tasks()
tasks = []
timer_running = False
remaining_time = DEFAULT_STUDY_TIME * 60
is_study_session = True

# Create root window
root = tk.Tk()
root.title("Study Planner with Pomodoro Timer")
root.geometry("700x900")
root.config(bg=COLOR_BG)
root.withdraw()  # Hide initially, show after login

# Create IntVar AFTER root window is created
study_time_minutes = tk.IntVar(value=DEFAULT_STUDY_TIME)
break_time_minutes = tk.IntVar(value=DEFAULT_BREAK_TIME)

# Set window icon (optional)
try:
    root.iconbitmap("study_icon.ico")
except:
    pass  # Icon file not required

# =============================================
# Header Section
# =============================================

frame_header = tk.Frame(root, bg=COLOR_PRIMARY, height=80)
frame_header.pack(fill=tk.X, padx=0, pady=0)
frame_header.pack_propagate(False)

label_title = tk.Label(
    frame_header, 
    text="📚 Study Planner", 
    font=("Arial", 28, "bold"),
    fg="white",
    bg=COLOR_PRIMARY
)
label_title.pack(pady=15)

frame_profile = tk.Frame(root, bg="white", relief=tk.RAISED, bd=2)
frame_profile.pack(fill=tk.X, padx=15, pady=(10, 0))

label_profile_info = tk.Label(frame_profile, text="Not logged in", font=("Arial", 11), fg=COLOR_TEXT, bg="white")
label_profile_info.pack(side=tk.LEFT, padx=12, pady=8)

button_profile = tk.Button(frame_profile, text="👤 Profile", state=tk.DISABLED, command=show_profile_window, bg=COLOR_ACCENT, fg="white", font=("Arial", 9, "bold"), width=10)
button_profile.pack(side=tk.LEFT, padx=10)

button_logout = tk.Button(frame_profile, text="🚪 Logout", state=tk.DISABLED, command=logout_user, bg=COLOR_WARNING, fg="white", font=("Arial", 9, "bold"), width=10)
button_logout.pack(side=tk.LEFT, padx=10)

# =============================================
# Timer Section
# =============================================

frame_timer = tk.Frame(root, bg="white", relief=tk.RAISED, bd=2)
frame_timer.pack(fill=tk.X, padx=15, pady=15)

label_session_type = tk.Label(
    frame_timer,
    text="Study Session",
    font=("Arial", 14, "bold"),
    fg=COLOR_PRIMARY,
    bg="white"
)
label_session_type.pack(pady=5)

label_timer = tk.Label(
    frame_timer,
    text="25:00",
    font=("Arial", 60, "bold"),
    fg=COLOR_PRIMARY,
    bg="white"
)
label_timer.pack(pady=10)

# Timer buttons frame
frame_timer_buttons = tk.Frame(frame_timer, bg="white")
frame_timer_buttons.pack(pady=10, padx=15, fill=tk.X)

button_start = tk.Button(
    frame_timer_buttons,
    text="▶ Start",
    command=start_timer,
    bg=COLOR_PRIMARY,
    fg="white",
    font=("Arial", 11, "bold"),
    width=15,
    cursor="hand2"
)
button_start.grid(row=0, column=0, padx=5)

button_pause = tk.Button(
    frame_timer_buttons,
    text="⏸ Pause",
    command=pause_timer,
    bg=COLOR_ACCENT,
    fg="white",
    font=("Arial", 11, "bold"),
    width=15,
    state=tk.DISABLED,
    cursor="hand2"
)
button_pause.grid(row=0, column=1, padx=5)

button_reset = tk.Button(
    frame_timer_buttons,
    text="⟲ Reset",
    command=reset_timer,
    bg=COLOR_WARNING,
    fg="white",
    font=("Arial", 11, "bold"),
    width=15,
    cursor="hand2"
)
button_reset.grid(row=0, column=2, padx=5)

# =============================================
# Custom Timer Settings Section
# =============================================

frame_timer_settings = tk.Frame(root, bg="white", relief=tk.RAISED, bd=2)
frame_timer_settings.pack(fill=tk.X, padx=15, pady=(0, 15))

label_settings_title = tk.Label(
    frame_timer_settings,
    text="⚙️ Timer Settings",
    font=("Arial", 12, "bold"),
    fg=COLOR_TEXT,
    bg="white"
)
label_settings_title.pack(pady=(10, 10), padx=10, anchor="w")

# Study time and Break time in one row
frame_settings_row = tk.Frame(frame_timer_settings, bg="white")
frame_settings_row.pack(fill=tk.X, padx=10, pady=(0, 10))

# Study time
label_study = tk.Label(
    frame_settings_row,
    text="📚 Study Time (min):",
    font=("Arial", 11, "bold"),
    fg=COLOR_TEXT,
    bg="white"
)
label_study.pack(side=tk.LEFT, padx=(0, 10))

spinbox_study = tk.Spinbox(
    frame_settings_row,
    from_=1,
    to=120,
    textvariable=study_time_minutes,
    font=("Arial", 11),
    width=5,
    relief=tk.FLAT,
    bd=1
)
spinbox_study.pack(side=tk.LEFT, padx=(0, 30))

# Break time
label_break = tk.Label(
    frame_settings_row,
    text="☕ Break Time (min):",
    font=("Arial", 11, "bold"),
    fg=COLOR_TEXT,
    bg="white"
)
label_break.pack(side=tk.LEFT, padx=(0, 10))

spinbox_break = tk.Spinbox(
    frame_settings_row,
    from_=1,
    to=60,
    textvariable=break_time_minutes,
    font=("Arial", 11),
    width=5,
    relief=tk.FLAT,
    bd=1
)
spinbox_break.pack(side=tk.LEFT, padx=(0, 20))

# Apply button
button_apply_settings = tk.Button(
    frame_settings_row,
    text="✓ Apply",
    command=reset_timer,
    bg=COLOR_SUCCESS,
    fg="white",
    font=("Arial", 10, "bold"),
    width=10,
    cursor="hand2"
)
button_apply_settings.pack(side=tk.LEFT)

# =============================================
# Task Input Section
# =============================================

frame_input = tk.Frame(root, bg="white", relief=tk.RAISED, bd=2)
frame_input.pack(fill=tk.X, padx=15, pady=(0, 15))

label_input = tk.Label(
    frame_input,
    text="📝 Add New Task",
    font=("Arial", 12, "bold"),
    fg=COLOR_TEXT,
    bg="white"
)
label_input.pack(pady=(10, 5), padx=10, anchor="w")

# Entry and button in one row
frame_input_row = tk.Frame(frame_input, bg="white")
frame_input_row.pack(fill=tk.X, padx=10, pady=(0, 10))

entry_task = tk.Entry(
    frame_input_row,
    font=("Arial", 11),
    width=40,
    relief=tk.FLAT,
    bd=1
)
entry_task.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
entry_task.config(highlightthickness=1, highlightcolor=COLOR_PRIMARY)

button_add = tk.Button(
    frame_input_row,
    text="+ Add",
    command=add_task,
    bg=COLOR_PRIMARY,
    fg="white",
    font=("Arial", 11, "bold"),
    width=8,
    cursor="hand2"
)
button_add.pack(side=tk.LEFT)

# =============================================
# Task List Section
# =============================================

frame_tasks = tk.Frame(root, bg="white", relief=tk.RAISED, bd=2)
frame_tasks.pack(fill=tk.BOTH, expand=True, padx=15, pady=(0, 15))

label_tasks_title = tk.Label(
    frame_tasks,
    text="📋 Your Tasks",
    font=("Arial", 12, "bold"),
    fg=COLOR_TEXT,
    bg="white"
)
label_tasks_title.pack(pady=(10, 5), padx=10, anchor="w")

# Listbox with scrollbar
frame_listbox = tk.Frame(frame_tasks, bg="white")
frame_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))

scrollbar = tk.Scrollbar(frame_listbox)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks = tk.Listbox(
    frame_listbox,
    font=("Arial", 11),
    yscrollcommand=scrollbar.set,
    relief=tk.FLAT,
    bd=1,
    height=8
)
listbox_tasks.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=listbox_tasks.yview)

# =============================================
# Task Management Buttons
# =============================================

frame_task_buttons = tk.Frame(frame_tasks, bg="white")
frame_task_buttons.pack(fill=tk.X, padx=10, pady=(0, 10))

button_mark = tk.Button(
    frame_task_buttons,
    text="✓ Mark Completed",
    command=mark_completed,
    bg=COLOR_SUCCESS,
    fg="white",
    font=("Arial", 10, "bold"),
    width=20,
    cursor="hand2"
)
button_mark.pack(side=tk.LEFT, padx=(0, 10))

button_delete = tk.Button(
    frame_task_buttons,
    text="🗑 Delete Task",
    command=delete_task,
    bg=COLOR_WARNING,
    fg="white",
    font=("Arial", 10, "bold"),
    width=20,
    cursor="hand2"
)
button_delete.pack(side=tk.LEFT)

# =============================================
# Progress Section
# =============================================

frame_progress = tk.Frame(root, bg="white", relief=tk.RAISED, bd=2)
frame_progress.pack(fill=tk.X, padx=15, pady=(0, 15))

label_completed = tk.Label(
    frame_progress,
    text="Completed: 0/0",
    font=("Arial", 12, "bold"),
    fg=COLOR_SUCCESS,
    bg="white"
)
label_completed.pack(pady=15)

# =============================================
# Footer Section
# =============================================

frame_footer = tk.Frame(root, bg=COLOR_BG)
frame_footer.pack(fill=tk.X, padx=15, pady=10)

label_footer = tk.Label(
    frame_footer,
    text="🎯 Stay focused and make the most of your study time!",
    font=("Arial", 9, "italic"),
    fg="#777777",
    bg=COLOR_BG
)
label_footer.pack()

# =============================================
# Initialize and Run
# =============================================

# Load initial task display
update_task_display()
update_timer_display()

# Handle window close
def on_closing():
    """Handle window closing event."""
    if messagebox.askokcancel("Quit", "Do you want to save and quit?"):
        set_user_tasks(tasks)
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

# Show login window first
show_login_window()
