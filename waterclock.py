import ttkbootstrap as ttkb
from playsound import playsound
import threading
import json
from datetime import datetime, timedelta
import time
import os
import random
from plyer import notification  # For desktop notifications

# Default settings
DEFAULT_INTERVAL = 3600  # 1 minute in seconds for frequent reminders
HYDRATION_GOAL = 8  # 8 glasses per day
progress = 0  # Track daily water intake progress
interval = DEFAULT_INTERVAL  # Set default interval
settings_file = "settings.json"
quotes = ["Stay hydrated!", "Water is life!", "Drink to your health!", "Keep going!"]

# Load or save settings
def load_settings():
    global interval, progress
    if os.path.exists(settings_file):
        with open(settings_file, "r") as file:
            settings = json.load(file)
            interval = settings.get("interval", DEFAULT_INTERVAL)
            progress = settings.get("progress", 0)

def save_settings():
    with open(settings_file, "w") as file:
        json.dump({"interval": interval, "progress": progress}, file)

# Function to play alarm sound
def play_alarm_sound():
    playsound("alarm_sound.mp3")

# Function to show desktop notification
def show_desktop_notification():
    notification.notify(
        title="Water Reminder",
        message="It's time to drink water! Stay hydrated.",
        timeout=10  # Duration in seconds
    )

# Function to display the reminder window
def show_reminder():
    global progress
    root = ttkb.Window(themename="darkly")
    root.geometry("300x200")
    root.title("Water Reminder")

    # Display motivational quote
    quote_label = ttkb.Label(root, text=random.choice(quotes), font=("Helvetica", 14), wraplength=250)
    quote_label.pack(pady=10)

    # Progress bar for hydration tracking
    progress_label = ttkb.Label(root, text=f"Daily Goal: {progress}/{HYDRATION_GOAL} glasses", font=("Helvetica", 12))
    progress_label.pack(pady=5)
    progress_bar = ttkb.Progressbar(root, value=progress / HYDRATION_GOAL * 100, length=200)
    progress_bar.pack(pady=10)

    # Dismiss button
    dismiss_button = ttkb.Button(root, text="Dismiss", command=lambda: dismiss_reminder(root))
    dismiss_button.pack(side="left", padx=10)

    # Snooze button
    snooze_button = ttkb.Button(root, text="Snooze", command=lambda: snooze_alarm(root))
    snooze_button.pack(side="right", padx=10)

    # Start playing alarm sound
    threading.Thread(target=play_alarm_sound, daemon=True).start()

    root.mainloop()

# Function to dismiss reminder and update progress
def dismiss_reminder(root):
    global progress
    progress += 1  # Increase hydration count
    save_settings()  # Save progress
    root.destroy()  # Close the reminder window

# Function to snooze the alarm
def snooze_alarm(root):
    root.destroy()
    next_alarm = datetime.now() + timedelta(minutes=1)  # Snooze for 1 minute
    schedule_next_alarm(next_alarm)

# Function to schedule the next alarm based on the interval
def schedule_next_alarm(start_time):
    global interval
    while True:
        now = datetime.now()
        if now >= start_time:
            show_reminder()
            show_desktop_notification()  # Show desktop notification every minute
            start_time = now + timedelta(seconds=interval)
        time.sleep(1)

# Clock update function
def update_clock(clock_label):
    while True:
        current_time = datetime.now().strftime("%H:%M:%S")
        clock_label.config(text=current_time)
        time.sleep(1)

# Daily reset check function
def daily_reset():
    global progress
    while True:
        if datetime.now().hour == 0:  # Reset at midnight
            progress = 0
            save_settings()
        time.sleep(3600)  # Check every hour

# Start the alarm when the application starts
def main():
    load_settings()  # Load saved interval and progress
    threading.Thread(target=daily_reset, daemon=True).start()  # Start daily reset check

    # Set the first alarm time
    start_time = datetime.now() + timedelta(seconds=interval)
    threading.Thread(target=schedule_next_alarm, args=(start_time,), daemon=True).start()

    # Main window for settings
    main_root = ttkb.Window(themename="darkly")
    main_root.title("Water Reminder")
    main_root.geometry("300x200")

    # Clock
    clock_label = ttkb.Label(main_root, font=("Helvetica", 14))
    clock_label.pack(pady=10)
    threading.Thread(target=update_clock, args=(clock_label,), daemon=True).start()

    # Interval set option
    ttkb.Label(main_root, text="Set Interval (minutes):").pack(pady=5)
    interval_entry = ttkb.Entry(main_root)
    interval_entry.pack(pady=5)
    interval_button = ttkb.Button(main_root, text="Set", command=lambda: set_interval(interval_entry))
    interval_button.pack(pady=5)

    main_root.mainloop()

# Set interval function
def set_interval(entry):
    global interval
    try:
        new_interval = int(entry.get()) * 60  # Convert minutes to seconds
        if new_interval > 0:
            interval = new_interval
            save_settings()  # Save the new interval setting
    except ValueError:
        pass  # Ignore invalid inputs

main()
