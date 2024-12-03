import os # operating system import
import re # regular expression import
from pathlib import Path # filesystem path import
from activity_log_functions import validate_activity_log_entries


# Function to find a correctly formatted CSV file in the current directory
def find_csv_files():
  print("\nValidating number of log files and log file names.....\n") # Once valid input is entered, print statement and continue
  base_path = os.path.abspath(".")  # capture absolute path of the current directory, Resource #3
  csv_files = list(Path(base_path).glob("*.csv")) # List all CSV files in the directory using pathlib's glob method
  regex_pattern = "[A-Z][a-z]*[A-Z][a-z]*Log\.csv" # Capture regex to match CSV file names in the format: "LastnameFirstnameLog.csv", Resource #4
  files_matching_pattern = [] # Empty list to store files that match the regex pattern
  
  # Loop over CSV files and check if they match the the case insensitive format: "XLog.csv"
  for file in csv_files:
    if re.match(regex_pattern, file.name): 
      files_matching_pattern.append(file) # Append the file if it matches the format "LastnameFirstnameLog.csv"
  
  # Raise an exception if zero, one, or more than 10 "LastnameFirstnameLog.csv" files are found
  if not files_matching_pattern:
    raise Exception("There are no CSV files with the correctly formatted name.")
  elif len(files_matching_pattern) == 1:
    raise Exception("There is only one CSV file with the correctly formatted name.")
  elif len(files_matching_pattern) > 10:
    raise Exception("There are more than 10 CSV files with the correctly formatted name.")
  else:
    return files_matching_pattern # return the list of files with matching names

# Function to validate the contents of the CSV file
def validate_csv_files(valid_named_files):
  print("Validating contents of each log file.....\n")
  name_regex_pattern = "[A-Z][a-z]*,[A-Z][a-z]*" # Capture regex to match format "Lastname,Firstname". 
  course_regex_pattern = "[A-Z]{2}\s\d{4}" # Capture regex to match Course Codes. For example, "CS 4500".
  valid_files = [] # Empty list to store validity of CSV files

  # Loop through each file with a valid name
  for valid_named_file in valid_named_files:
    filename = os.path.basename(valid_named_file) # extract filename from full path

    try:
      with open(valid_named_file, 'r') as file:
        lines = file.readlines() # Read all lines from the CSV file

    except:
      raise Exception("Unable to open CSV file.")
 
    # Ensure the CSV file is not empty
    if len(lines) < 1:
      raise Exception(f"{filename}: INVALID - This file is empty.")
    
    # Ensure the CSV file has 2 lines of data
    elif len(lines) < 2:
      raise Exception(f"{filename}: INVALID - There should be at least two lines of data in the CSV file.")

    # Validate the first line with name_regex_pattern. 
    elif re.match(name_regex_pattern, lines[0]) is None: 
      raise Exception(f"{filename}: INVALID - Line 1: A valid file starts with 2 strings seperated by a comma.")

    # Validate the second line with course_regex_pattern. 
    elif len(lines) >= 2 and re.match(course_regex_pattern, lines[1]) is None:
      raise Exception(f"{filename}: INVALID - Line 2: Course code must be in the correc format.")

    # Validate all activity log entries, starting on line #3
    if len(lines) > 2:
      for line_number, line in enumerate(lines[2:], start=3): # Resource #3 and Resource #4
        validate_activity_log_entries(line, line_number, filename, valid_files)
        
    # Only mark as VALID if no errors were found for this file
    valid_files.append(filename)

  # return the list of valid activity log files
  return valid_files 
  
