# Water Reminder App

A Python-based application that reminds users to stay hydrated by drinking water at regular intervals. The app uses desktop notifications, a user-friendly graphical interface, and motivational quotes to keep users on track with their hydration goals.

---

## Features

- **Customizable Reminder Intervals**: Set your preferred interval for hydration reminders.
- **Progress Tracking**: Track your daily water intake progress towards your hydration goal.
- **Desktop Notifications**: Get timely reminders through desktop notifications.
- **Snooze Option**: Snooze reminders for 1 minute if you're busy.
- **Motivational Quotes**: Display random motivational quotes to encourage hydration.
- **Daily Reset**: Automatically resets progress at midnight.
- **Clock Display**: Shows the current time on the main settings window.

---

## Technologies Used

- **Python**: Core programming language.
- **ttkbootstrap**: For creating the graphical user interface (GUI).
- **Plyer**: For desktop notifications.
- **Playsound**: For alarm sounds.

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/water-reminder.git
   cd water-reminder
   ```

2. **Install Dependencies**:
   Make sure you have Python 3.x installed. Then, install the required packages:
   ```bash
   pip install ttkbootstrap playsound plyer
   ```

3. **Add Alarm Sound**:
   Place your alarm sound file (e.g., `alarm_sound.mp3`) in the same directory as the script.

4. **Run the Application**:
   ```bash
   python water_reminder.py
   ```

---

## Usage

1. Launch the app by running the script.
2. Set your preferred reminder interval in minutes using the input field.
3. Receive reminders with motivational quotes and desktop notifications.
4. Track your daily water intake progress using the progress bar.
5. Use the "Snooze" button to delay the reminder by 1 minute if needed.

---

## File Structure

```
water-reminder/
├── settings.json           # Stores user settings (interval and progress)
├── alarm_sound.mp3         # Alarm sound file
└── water_reminder.py       # Main Python script
```

---

## Screenshots

_Add screenshots of the application interface and notifications here._

---

## Contributing

1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a pull request.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contact

For questions or suggestions, feel free to contact me at [your-email@example.com].

