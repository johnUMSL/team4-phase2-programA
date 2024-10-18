import os # operating system import
import re # regular expression import
from pathlib import Path # filesystem path import
from constants import COURSE_CODE
from activity_log_functions import validate_activity_log_entries


# Function to find a correctly formatted CSV file in the current directory
def find_csv_files():
  base_path = os.path.abspath(".")  # capture absolute path of the current directory, Resource #3
  csv_files = list(Path(base_path).glob("*.csv")) # List all CSV files in the directory using pathlib's glob method
  regex_pattern = "[\w]*Log\.csv"  # Capture regex to match CSV file names in the format: "XLog.csv", Resource #4
  files_matching_pattern = [] # Empty list to store files that match the regex pattern
  
  # Loop over CSV files and check if they match the the case insensitive format: "XLog.csv"
  for file in csv_files:
    if re.match(regex_pattern, file.name, flags=re.I): # Resource #1
      files_matching_pattern.append(file) # Append the file if it matches the format "LastnameFirstname.csv"
  
  # Raise an exception if no case insensitive "XLog.csv" files are found
  if not files_matching_pattern:
    raise Exception("There is no CSV file with the correctly formatted name.")
  
  return files_matching_pattern # return the list of files with matching names

# Create or open a file for writing
def create_validity_file(valid_named_files):
  if len(valid_named_files) > 0: # If any case insensitive "XLog.csv" files are found
    with open("ValidityChecks.txt", "w") as file: # Resource #2
      return # nothing to return, file will be created

# Append errors to validity check file
def write_errors_to_file(errors):
  with open("ValidityChecks.txt", "w") as file: # Open file for writing
    for error in errors:
      print(error) # Print each error to the console
      file.write(f"{error}\n") # Write each error to the text file

# Function to validate the contents of the CSV file
def validate_csv_files(valid_named_files):
  name_regex_pattern = "[A-Z][a-z]*,[A-Z][a-z]*" # Capture regex to match format "Lastname,Firstname". 
  errors_in_files =[] # Empty list to store formatting errors in CSV files

  # Loop through each file with a valid name
  for valid_named_file in valid_named_files:
    filename = os.path.basename(valid_named_file) # extract filename from full path
    course_in_line = [] # Empty list to store course code information
    file_has_errors = False # flag used to track if errors are found in the file

    try:
      with open(valid_named_file, 'r') as file:
        lines = file.readlines() # Read all lines from the CSV file

    except:
      raise Exception("Unable to open CSV file.")
 
    # Ensure the CSV file is not empty
    if len(lines) < 1:
      errors_in_files.append(f"{filename}:INVALID - This file is empty.")
      file_has_errors = True # Flag file for having errors

    # Validate the first line with name_regex_pattern. 
    elif len(lines) > 0 and re.match(name_regex_pattern, lines[0], flags=re.I) is None: # Resource #1
      errors_in_files.append(f"{filename}:INVALID - Line 1: A valid file starts with 2 strings seperated by a comma.")
      file_has_errors = True # Flag file for having errors

    # Validate the second line with constant.COURSE_CODE. 
    elif len(lines) >= 2:
      for data in lines[1].split(','):
        data = data.strip()
        if data:
          course_in_line.append(data)
      if course_in_line[0] != COURSE_CODE:
        errors_in_files.append(f"{filename}:INVALID - Line 2: Course code must be CS 4500.")
        file_has_errors = True # Flag file for having errors

    # Validate all activity lof entries, starting on line #3
    if len(lines) > 2:
      for line_number, line in enumerate(lines[2:], start=3): # Resource #3 and Resource #4
        if validate_activity_log_entries(line, line_number, filename, errors_in_files) == False:
          file_has_errors = True # Flag file for having errors
          break

    # Only mark as VALID if no errors were found for this file
    if not file_has_errors:
      errors_in_files.append(f"{filename}:VALID")

  # return the list of errors and valid status for all files
  return errors_in_files 
    