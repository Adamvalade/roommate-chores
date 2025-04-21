import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
import time
import os
import datetime

chores = ["floors", "living room", "cleaning kitchen",
          "trash", "dishes"]

people = ["Adam", "Rishab", "Leo", "Eli", "Leon"]

emails = ["advalade@umich.edu", "rishabj@umich.edu", "leobayer@umich.edu",
          "eliw@umich.edu", "wangleon@umich.edu"]

index_file_path = '/Users/adamvalade/Desktop/Python/Chores/ChoresIndex.txt'
filename = '/Users/adamvalade/Desktop/Python/Chores/last_run_time.txt'

def is_right_time():
    now = datetime.datetime.now()
    if now.weekday() == 6:
        return True
    else:
        return False

def save_run_time(filename):
    with open(filename, 'w') as file:
        file.write(datetime.datetime.now().isoformat())
        
def ran_in_last_24_hours(filename):
    if not os.path.exists(filename):
        return False

    with open(filename, 'r') as file:
        last_run_time_str = file.read().strip()
        if not last_run_time_str:  # Check if the string is empty
            return False

    try:
        last_run_time = datetime.datetime.strptime(last_run_time_str, '%Y-%m-%dT%H:%M:%S.%f')
    except ValueError:
        return False  # If the format is incorrect, assume the script hasn't run

    return (datetime.datetime.now() - last_run_time) < datetime.timedelta(hours=24)
                 

def read_index():
    if os.path.exists(index_file_path):
        with open(index_file_path, 'r') as file:
            return int(file.read().strip())
    return 0

# Function to save the index to the file
def save_index(index):
    with open(index_file_path, 'w') as file:
        file.write(str(index))

def check_enabled():
    file_path = '/Users/adamvalade/Desktop/Python/Chores/Enabled.txt'
    
    try:
        with open(file_path, 'r') as file:
            content = file.read().strip()
            if content.upper() == 'Y':
                return True
            elif content.upper() == 'N':
                return False
            else:
                print("Invalid content in file. Expected 'Y' or 'N'.")
                return False
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    
def get_next_week_range():
    today = datetime.date.today()
    days_to_next_monday = 1 if today.weekday() == 6 else (7 - today.weekday())
    next_monday = today + datetime.timedelta(days=days_to_next_monday)
    next_sunday = next_monday + datetime.timedelta(days=6)
    
    # Format dates to 'MM-DD' format
    next_monday_str = next_monday.strftime("%m-%d")
    next_sunday_str = next_sunday.strftime("%m-%d")

    return f"{next_monday_str} - {next_sunday_str}"

def write_other_chores(current_person_index, start_index):
    message_lines = ["You can see everyone else's chores below:"]
    
    for index, person in enumerate(people):
        # Skip the current person to exclude their chore from their own email
        if index == current_person_index:
            continue

        chore_index = (start_index + index) % len(chores)
        message_lines.append(f"{person} is on {chores[chore_index]}.")

    # Join all message lines into a single string separated by new lines
    return "\n".join(message_lines)

def send_email(start_index):

    from_email = os.environ.get("GMAIL")
    password = os.environ.get("GMAIL_PASSWORD")

    # Email server configuration
    
    smtp_server = "smtp.gmail.com"
    smtp_port = 587 


    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Upgrade the connection to secure
    server.login(from_email, password)

    for i, person in enumerate(people):
        chore_index = (start_index + i) % len(chores)
        message_text = (f"Hello {person}, this is your weekly chore assignment. For "
           f"the week of {get_next_week_range()}, your chore is: {chores[chore_index]}.")
        
        message_text += "\n\n"
        message_text += write_other_chores(i, start_index)
        message_text += "\n\n-Adaddy bot"
        msg = EmailMessage()
        msg['Subject'] = 'Chores'
        msg['From'] = 'Adaddy'
        msg['To'] = emails[i]
        msg.set_content(message_text)
        server.send_message(msg)
        
    server.quit()

#driver
if (not ran_in_last_24_hours(filename)) and is_right_time() and check_enabled():
    index = read_index()
    send_email(index)
    index = (index + 1) % 5
    save_run_time(filename)
    save_index(index)
    #/Library/Frameworks/Python.framework/Versions/3.12/bin/python3 /Users/adamvalade/Desktop/Python/Chores/NotGayChoreChart.py
