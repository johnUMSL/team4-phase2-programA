from datetime import datetime

def validate_activity_log_entries(line, line_number, filename, errors_in_files: list): # Resource #5
  data_points = line.split(',')
  # Make sure there are at least 5 data points in the log entry
  if len(data_points) < 5:
    errors_in_files.append(f"{filename} - {line_number}: There are less than 5 data points in the log entry.")
    return False
  
  # Make sure there are at most 6 data points in the log entry
  if len(data_points) > 6:
    errors_in_files.append(f"{filename} - {line_number}: There are more than 6 data points in the log entry.")
    return False
  
  # Make sure the entered date is valid and in MM/DD/CCYY format
  try: # Resource #7 and Resource #8
    if len(data_points[0]) != 10:
      raise ValueError 
    
    date = datetime.strptime(data_points[0], '%m/%d/%Y') # Automatically raises value error if invalid date
    if date > datetime.now():
      errors_in_files.append(f"{filename} - {line_number}: Date must be from today or before today.")
      return False   
    
  except ValueError:
    errors_in_files.append(f"{filename} - {line_number}: Date is not formatted correctly.")
    return False

    

