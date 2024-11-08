import ttkbootstrap as ttkb
from playsound import playsound
import threading
import time
from datetime import datetime, timedelta

# Alarm interval (e.g., 1 hour in seconds)
ALARM_INTERVAL = 10  # For testing, we set to 10 seconds

# Function to play sound (remove if you don't have an "alarm_sound.mp3" file)
def play_alarm_sound():
    playsound("alarm_sound.mp3")

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
    label = ttkb.Label(frame, text="Time to Drink Water!", font=("Montserrat", 16))
    label.pack(pady=10)

    # Dismiss button
    dismiss_button = ttkb.Button(frame, text="Dismiss", command=root.destroy)
    dismiss_button.pack(side="left", padx=10)

    # Start playing alarm sound
    threading.Thread(target=play_alarm_sound, daemon=True).start()

    root.mainloop()

# Function to schedule the next alarm based on the interval
def schedule_next_alarm():
    while True:
        # Wait for the next interval
        time.sleep(ALARM_INTERVAL)
        # Show the reminder window
        show_reminder()

# Start the scheduler in a separate thread
def main():
    threading.Thread(target=schedule_next_alarm, daemon=True).start()

# Start the main function
main()

# Keep the program running with a persistent main window
main_root = ttkb.Window()
main_root.title("Water Reminder App")
main_root.geometry("200x100")
ttkb.Label(main_root, text="Water Reminder Running...").pack(pady=20)
main_root.mainloop()
