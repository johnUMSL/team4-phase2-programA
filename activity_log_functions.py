from datetime import datetime, timedelta
from constants import ACTIVITY_CODES

def validate_activity_log_entries(line, line_number, filename, errors_in_files: list): # Resource #5
  data_points = line.split(',')
  
  # Make sure the entered date is valid and in MM/DD/CCYY format
  try: # Resource #7 and Resource #8
    if len(data_points[0]) != 10:
      raise ValueError 
    
    date = datetime.strptime(data_points[0], '%m/%d/%Y') # Automatically raises value error if invalid date
    if date > datetime.now():
      errors_in_files.append(f"{filename}:INVALID - {line_number}: Date must be from today or before today.")
      return False   
    
  except ValueError:
    errors_in_files.append(f"{filename}:INVALID - Line {line_number}: Date is not formatted correctly.")
    return False

  # Make sure entered start time is valid and in the HH:MM 24 hour format
  try:
    if len(data_points[1]) != 5:
      raise ValueError
    
    start_time = datetime.strptime(data_points[1], '%H:%M')

  except ValueError:
    errors_in_files.append(f"{filename}:INVALID - Line {line_number}: Start time is not formatted correctly.")
    return False  

  # Make sure end time is valid, in the HH:MM 24 hour format, and later than start time
  try:
    if len(data_points[2]) != 5:
      raise ValueError
    
    end_time = datetime.strptime(data_points[2], '%H:%M')

    if start_time > end_time:
      errors_in_files.append(f"{filename}:INVALID - Line {line_number}: Start time must be before End time.")
      return False
    
    if (end_time - start_time) > timedelta(hours=4):
      errors_in_files.append(f"{filename}:WARNING - Line {line_number}: Work entry exceeds 4 hours")

  except ValueError:
    errors_in_files.append(f"{filename}:INVALID - Line {line_number}: End time is not formatted correctly.")
    return False  
  

  # Validate number of people entry. A number between 1 and 50 inclusive
  if data_points[3].isdigit() == False or int(data_points[3]) < 1 or int(data_points[3]) > 50:
    errors_in_files.append(f"{filename}:INVALID - Line {line_number}: The fourth item should be an integer between 1 and 50 inclusive.")
    return False
  
  # Validate Activity code entry
  if data_points[4].strip() not in ACTIVITY_CODES:
    errors_in_files.append(f"{filename}:INVALID - Line {line_number}: Activity code is Invalid.")
    return False
  
  # Validate if required note has been entered
  if data_points[4] == "D" and not data_points[5].strip():
    errors_in_files.append(f"{filename}:INVALID - Line {line_number}: A Note is Required.")
    return False
  
  # Validate note contains no commas
  if len(data_points) > 6:
    errors_in_files.append(f"{filename}:INVALID - Line {line_number}: Notes cannot contain a comma.")
    return False
  
  # Validate note is less than 81 characters
  if len(data_points[5]) > 80:
    errors_in_files.append(f"{filename}:INVALID - Line {line_number}: Notes cannot be longer than 80 characters.")
    return False
