from datetime import datetime
import pandas as pd
from tabulate import tabulate

def calculate_time_spent(start_time, end_time):
  format = "%H:%M"
  start = datetime.strptime(start_time, format)
  end = datetime.strptime(end_time, format)
  time = int((end - start).total_seconds() / 60)
  return time

def compile_activity_log_data(activity_logs):
  data = {}
  for student, log_entries in activity_logs.items():
    if student not in data:
      data[student] = {}
    for log_entry in log_entries:
      time_spent = calculate_time_spent(log_entry.start_time, log_entry.end_time)
      if log_entry.activity_code not in data[student]:
        data[student][log_entry.activity_code] = 0
      data[student][log_entry.activity_code] += time_spent
  return data

def create_report_three(data, file='PhaseThreeReport4.txt'):
  column_order = [hex(i)[2:].upper() for i in range(14)]
  df = pd.DataFrame.from_dict(data, orient='index').fillna(0).astype(int)
  df = df.reindex(columns=column_order, fill_value=0)
  df.reset_index(inplace=True)
  df.rename(columns={'index': 'Names'}, inplace=True)
  with open(file, 'w') as f:
    f.write(tabulate(df, headers='keys', tablefmt='grid', showindex=False))
    print(f"Report saved to {file}")
  return df
