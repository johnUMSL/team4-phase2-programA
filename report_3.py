from datetime import datetime
from log_entry import LogEntry

def calculate_time_spent(start_time, end_time):
  format = "%H:%M"
  start = datetime.strptime(start_time, format)
  end = datetime.strptime(end_time, format)
  time = int((end - start).total_seconds() / 60)
  return time

def compile_activity_log_data(activity_logs):
  data = {}
  activity_minutes = {hex(i)[2:].upper(): 0 for i in range(14)}
  for student, log_entries in activity_logs.items():
    if student not in data:
      data[student] = {}
    for log_entry in log_entries:
      time_spent = calculate_time_spent(log_entry.start_time, log_entry.end_time)
      if log_entry.activity_code not in activity_minutes:
        activity_minutes[log_entry.activity_code] = 0
      activity_minutes[log_entry.activity_code] += time_spent
  return activity_minutes