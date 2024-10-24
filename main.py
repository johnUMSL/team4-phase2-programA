# Class: CS 4500, Phase 2A Program Name: team4-phase2-programA.py, Date: 10/03/2024, Last Modified: 10/18/2024
# Programmed using Python 3.10.4, the development environment is Visual Studio Code.
# Primarily programmed by Lead Programmer John Garrett. Received debugging assistance from Matthew Dobbs.

# Description of program:
# This program checks multiple log files in the current directory, identifying CSV files that match the pattern XLog.csv. 
# It ensures files are not empty, validates that the first line contains a last name and first name, and that the second line 
# has the course code CS 4500. For time entries, the program checks if dates and times are valid, and that additional details, 
# like activity codes and notes, meet specific criteria.
# If a time entry exceeds four hours, a warning is issued, though the file is not invalidated. 
# The program generates a report both on-screen and in a text file (ValidityChecks.txt), indicating whether each file is valid or, 
# if not, the first error found. After all files are checked, it prints a final report and closes with a goodbye message.

# Build instructions: 
# To compile and build an executable file for this program, make sure you have pyinstaller in your virtual environment.
# Once your virtual environment has been activated, you can install pyinstaller by typing in the terminal "pip install pyinstaller" (Do not include "")
# Once installed, then type in the terminal "pyinstaller --onefile main.py" (Do not include "")
# The file will build and an executable file named "main.exe" and save it in the dist folder within your project.
# main.exe can be moved and run from any location, but the CSV files you are reading MUST be in the same location.
# In your terminal, navigate to the location of main.exe, confirm the existense of your CSV files, 
# and run the executable using the command "./main.exe".

# Resources used in Program
# 1. https://stackoverflow.com/questions/500864/case-insensitive-regular-expression-without-re-compile - ignore case flag for regex (re) library
# 2. https://stackoverflow.com/questions/48959098/how-to-create-a-new-text-file-using-python
# 3. https://www.geeksforgeeks.org/how-to-read-specific-lines-from-a-file-in-python/
# 4. https://docs.python.org/3/library/functions.html#enumerate
# 5. https://stackoverflow.com/questions/2489669/how-do-python-functions-handle-the-types-of-parameters-that-you-pass-in
# 7. https://strftime.org/
# 8. https://discuss.python.org/t/best-way-to-validate-an-entered-date/49406/3
# 9. https://stackoverflow.com/questions/40097590/detect-whether-a-python-string-is-a-number-or-a-letter

from constants import SUMMARY, GOODBYE
from helpers import *
from csv_functions import *

def main():
  clear_console() # clear the console
  print(SUMMARY) # print the SUMMARY from constants.py
  readyToContinue() # wait for user to procedd by entering input

  files_matching_pattern = find_csv_files() 
  create_validity_file(files_matching_pattern)

  errors = validate_csv_files(files_matching_pattern)
  write_errors_to_file(errors)

  print(GOODBYE)

  

# entry point
if __name__=='__main__':
  main()