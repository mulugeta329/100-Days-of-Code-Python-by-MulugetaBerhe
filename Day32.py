import datetime as dt
import os
import random
import smtplib

# --- CONFIGURATION (Replace with your actual details to send live emails) ---
MY_EMAIL = 'your_email@gmail.com'
MY_PASSWORD = 'your_app_password'  # Use a Gmail App Password, not your real password
# --------------------------------------------------------------------------


def clear_terminal():
  os.system('cls' if os.name == 'nt' else 'clear')


clear_terminal()

# 1. Working with the datetime module
now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(f'Current Date: {year}-{month:02d}, Day of Week Index: {day_of_week}')

# Example: Check if today is a specific day (e.g., Monday = 0)
if day_of_week == 0:
  print("It's Monday! Time for a motivational quote.")

  # Sample quotes list
  quotes = [
      'Keep pushing forward!',
      'Consistency is key to mastering Python.',
      'Every expert was once a beginner.',
  ]
  quote_to_send = random.choice(quotes)

  # 2. Sending Email via smtplib
  # Note: To test live, configure MY_EMAIL and MY_PASSWORD above.
  if MY_EMAIL != 'your_email@gmail.com':
    try:
      with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()  # Secure the connection
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,  # Sending to yourself as a test
            msg=(
                'Subject: Monday Motivation\n\nHi!\n\nHere is your motivation'
                f' for today:\n{quote_to_send}'
            ),
        )
      print('Email sent successfully!')
    except Exception as e:
      print(f'Failed to send email: {e}')
  else:
    print(
        '[Simulation Mode] Update MY_EMAIL and MY_PASSWORD to send live'
        ' emails.'
    )