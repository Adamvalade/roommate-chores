# 🧹 Roommate Chore Scheduler

A lightweight Python automation script that rotates weekly chores among five roommates and emails each person their assignment. Built to run locally on a schedule with minimal maintenance.

## 📋 Features

- Rotates five unique chores across five roommates
- Sends personalized emails via Gmail SMTP
- Prevents duplicate runs using timestamp tracking
- Toggle system to enable/disable execution
- Dynamically formats the week range (e.g. "04-22 - 04-28")

## 🛠️ Technologies Used

- Python 3
- `smtplib` + `email.message` for email automation
- File I/O for state persistence
- `datetime` for scheduling logic

## 📁 Files

- `roommate_chores.py` — main script
- `ChoresIndex.txt` — tracks current rotation index
- `last_run_time.txt` — stores last execution time
- `Enabled.txt` — acts as a manual toggle (`Y` or `N`)

> **Note**: File paths are currently configured for macOS. They can be modified for other operating systems.

## 🔒 Setup Instructions

1. Clone the repo:
   ```bash
   git clone https://github.com/YOUR_USERNAME/roommate-chores.git
   cd roommate-chores

This script is meant for personal use. Please don't store real passwords in plaintext. Use .env files and environment variables.