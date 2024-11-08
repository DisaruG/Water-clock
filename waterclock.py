import ttkbootstrap as ttkb
from playsound import playsound
import threading
import time
from datetime import datetime, timedelta

# Alarm interval (e.g., 1 hour in seconds)
ALARM_INTERVAL = 3600  # 1 hour

# Function to play sound
def play_alarm_sound():
    playsound("alarm_sound.mp3")  # Make sure you have an alarm sound file in the same directory

# Function to display the reminder window
def show_reminder():
    # Create a new window with a custom theme
    root = ttkb.Window(themename="darkly")
    root.geometry("300x150")
    root.title("Water Reminder")

    # Frame and widgets
    frame = ttkb.Frame(root, padding=20)
    frame.pack(fill="both", expand=True)

    # Reminder label
    label = ttkb.Label(frame, text="Time to Drink Water!", font=("Montserrat", 16), bootstyle="info")
    label.pack(pady=10)

    # Dismiss button
    dismiss_button = ttkb.Button(frame, text="Dismiss", bootstyle="danger-outline", command=root.destroy)
    dismiss_button.pack(side="left", padx=10)

    # Snooze button
    snooze_button = ttkb.Button(frame, text="Snooze", bootstyle="primary-outline", command=lambda: snooze_alarm(root))
    snooze_button.pack(side="right", padx=10)

    # Start playing alarm sound
    threading.Thread(target=play_alarm_sound, daemon=True).start()

    root.mainloop()

# Function to snooze the alarm
def snooze_alarm(root):
    root.destroy()
    next_alarm = datetime.now() + timedelta(minutes=10)  # Snooze for 10 minutes
    schedule_next_alarm(next_alarm)

# Function to schedule the next alarm based on the interval
def schedule_next_alarm(start_time):
    # Calculate when the next reminder should go off
    while True:
        now = datetime.now()
        if now >= start_time:
            show_reminder()
            start_time = now + timedelta(seconds=ALARM_INTERVAL)
        time.sleep(1)  # Check every second

# Start the alarm when the application starts
def main():
    # Set the first alarm time to 1 hour from startup
    start_time = datetime.now() + timedelta(seconds=ALARM_INTERVAL)
    # Schedule the first reminder
    schedule_next_alarm(start_time)

# Run the main function in a separate thread to keep the GUI responsive
threading.Thread(target=main, daemon=True).start()
