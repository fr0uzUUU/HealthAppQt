# HealthAppQt 

### Description

**HealthAppQt is a desktop application written 
in Python using PySide6 (Qt), designed to help 
users manage their health data. It supports user 
registration, login, BMI calculation, medication 
management, and data export.**

### Structure
<pre>
HealthAppQt/
├── main.py                   # Application entry point
├── auth/
│   └── user_auth.py          # User authentication functions
├── dialogs/
│   ├── login_dialog.py       # Login window
│   ├── main_window.py        # Main user panel
│   ├── bmi_dialog.py         # BMI calculator
│   ├── add_med_dialog.py     # Add medication dialog
│   ├── history_dialog.py     # Medication history dialog
│   ├── export_dialog.py      # Export history to TXT
│   ├── motivation_dialog.py  # Display motivational messages
│   └── ui/
│       └── *.ui               # GUI design files (Qt Designer)
├── data/
│   └── users.json             # User login data
</pre>

Installation and Running

1.Create and activate venv<br>
<code>python -m venv .venv</code>
<br>
<code>.venv\Scripts\activate</code>
<br>

2.Install PySide6<br>
<code>pip install PySide6</code>
<br>

3.Running Application<br>
<code>python main.py</code>
<br>