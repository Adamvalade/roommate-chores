🧹 Roommate Chore Scheduler

A lightweight Python automation script that rotates weekly chores among five roommates and emails each person their assignment. Designed to run locally on a schedule using a cron job, with minimal maintenance required.

📋 Features

Rotates five unique chores across five roommates
Sends personalized emails via Gmail SMTP
Prevents duplicate runs using timestamp tracking
Toggle system to enable/disable execution
Dynamically formats the week range (e.g., 04-22 - 04-28)
Compatible with cron jobs for scheduled automation

🛠️ Technologies Used

Python 3
smtplib + email.message for email automation
File I/O for rotation and state persistence
datetime for week handling and timing logic

🗂️ File Overview

roommate_chores.py — main script
ChoresIndex.txt — tracks current rotation index
last_run_time.txt — stores the timestamp of the last execution
Enabled.txt — acts as a manual toggle (Y to run, N to skip)

🕒 Running with a Cron Job (macOS/Linux)

Use bash run the script every Sunday at 12 PM:
0 12 * * 0 /usr/bin/python3 /path/to/roommate_chores.py
You can edit your crontab with:
crontab -e

Make sure the file paths in the script match your machine’s directory structure.

⚠️ Security Note

This script uses email credentials. Do not hardcode real passwords in plaintext.
Instead, use a .env file and load credentials via environment variables like this:

import os
password = os.getenv('EMAIL_PASSWORD')
Then run your script like this:
EMAIL_PASSWORD=your-password python3 roommate_chores.py

📦 Setup Instructions

git clone https://github.com/YOUR_USERNAME/roommate-chores.git
cd roommate-chores

Edit the names, chores, email list, and file paths as needed for your setup.
