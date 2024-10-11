import os # operating system import
import re # regular expression import
from pathlib import Path # filesystem path import
from constants import COURSE_CODE


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
  
  return files_matching_pattern

# If any case insensitive "XLog.csv" files are found, create or open a file for writing
def create_validity_file(valid_named_files):
  if len(valid_named_files) > 0:
    with open("ValidityChecks.txt", "w") as validityCheckFile: # Resource #2
      return validityCheckFile

# Function to validate the contents of the CSV file
def validate_csv_files(valid_csv_files):
  name_regex_pattern = "[A-Z][a-z]*,[A-Z][a-z]*" # Capture regex to match format "Lastname,Firstname". Resource #4

  for valid_csv_file in valid_csv_files:
    
    name_in_line = [] # Empty list to store name information
    course_in_line = [] # Empty list to store course code information
    
    try:
      with open(valid_csv_file, 'r') as file:
        lines = file.readlines() # Read all lines from the CSV file
    except:
      raise Exception("CSV File is not formatted correctly.")
    
    # Ensure the CSV file has at least two lines (name and class ID)
    if len(lines) < 2:
      raise Exception("There should be at least two lines of data in the CSV file.")
    
    # Validate the first line with name_regex_pattern. Resource #6
    if re.match(name_regex_pattern, lines[0]):
      # Split the first line by commas, add non-empty, stripped values to name_in_line list
      for data in lines[0].split(','):
        data = data.strip()
        if data:
          name_in_line.append(data)
      print(f"\nLast Name, First Name: {name_in_line[0]}, {name_in_line[1]}") # Output last and first name from name_in_line list
    else:
      raise Exception("The name data in the CSV file is not formatted correctly.") # Raise an exception if the name format is incorrect
    
    # Validate the second line with COURSE_CODE from constants "CS 4500". 
    if re.match(COURSE_CODE, lines[1]):
      for data in lines[1].split(','):
        data = data.strip()
        if data:
          course_in_line.append(data)
      print(f"Class ID: {course_in_line[0]}\n")
    else:
      raise Exception("The Class ID data in the CSV file is not formatted correctly.")
    