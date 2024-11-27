# Class: CS 4500, Phase 3 Program Name: team7-phase3, Date: 10/03/2024, Last Modified: 10/18/2024
# Programmed using Python 3.10.4, the development environment is Visual Studio Code.
# Programmed by John Garrett, Connor Gilmore, and Matthew Dobbs.

#Who Did What:
#Connor Gilmore: Report 5 and central data structure
#Aaron Graham: Report 1 and Graph A
#Matthew Dobbs: Graph C
#Alewiya Duressa: Report 2
#Logan Bessinger: Report 4
#John Garrett: Report 3 and Graph B and Validation


# Description of program:
# This program processes time logs for a team. It starts by checking if the correct number
# of time log files are present (between 2 and 10). It stops and shows an error if there are too few, too many, 
# or if any files have duplicate names. It then verifies that each file is valid and that the names inside of
# each file are unique. Next, it ensures all logs share the same Class ID, halting with an error if there are
# differnces. If there the correct number of files, and all are valid, the program collects data from the
# time logs to generate and display reports and graphs. These reports are saved as text files. 
# Graphs are shown one at a time, pausing for user input before moving on. The program then ends with a
# goodbye message.

# Build instructions: 
# To compile and build an executable file for this program, make sure you have pyinstaller in your virtual environment.
# Once your virtual environment has been activated, you can install pyinstaller by typing in the terminal "pip install pyinstaller" (Do not include "")
# Once installed, then type in the terminal "pyinstaller --onefile main.py" (Do not include "")
# The file will build and an executable file named "main.exe" and save it in the dist folder within your project.
# main.exe can be moved and run from any location, but the CSV files you are reading MUST be in the same location.
# In your terminal, navigate to the location of main.exe, confirm the existense of your CSV files, 
# and run the executable using the command "./main.exe".

#central data structure:  dict[str, list[LogEntry]]
#dictionary where the unique is a the name of student from a csv file
#and the dictionary value is a list of log entry objects from that csv file 
#where each log entry represents a log csv row

# Resources used in Program
# 1. https://stackoverflow.com/questions/500864/case-insensitive-regular-expression-without-re-compile - ignore case flag for regex (re) library
# 2. https://stackoverflow.com/questions/48959098/how-to-create-a-new-text-file-using-python
# 3. https://www.geeksforgeeks.org/how-to-read-specific-lines-from-a-file-in-python/
# 4. https://docs.python.org/3/library/functions.html#enumerate
# 5. https://stackoverflow.com/questions/2489669/how-do-python-functions-handle-the-types-of-parameters-that-you-pass-in
# 7. https://strftime.org/
# 8. https://discuss.python.org/t/best-way-to-validate-an-entered-date/49406/3
# 9. https://stackoverflow.com/questions/40097590/detect-whether-a-python-string-is-a-number-or-a-letter
#10. https://docs.python.org/3/tutorial/classes.html
#11. https://www.w3schools.com/python/python_tuples.asp
#12. https://www.geeksforgeeks.org/using-else-conditional-statement-with-for-loop-in-python/
#13. https://stackoverflow.com/questions/14472795/how-do-i-sort-a-list-of-datetime-or-date-objects
#14. https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.from_dict.html
#15. https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reindex.html
#16. https://pypi.org/project/tabulate/

from constants import SUMMARY, GOODBYE
from helpers import *
from csv_functions import *
from load_logs import load_activity_logs
from validate_name_course_id import unique_name_check, class_id_check
from report_2 import generate_report2
from report_3 import compile_activity_log_data, create_report_three
from report4 import report4
from report5 import report5

from graphc import print_graph_c

def main():

  clear_console() # clear the console
  print(SUMMARY) # print the SUMMARY from constants.py
  readyToContinue() # wait for user to proceed by entering input

  files_matching_pattern = find_csv_files() 

  valid_files = validate_csv_files(files_matching_pattern)
  for valid_file in valid_files:
    print(f"{valid_file}: VALID")

  unique_name_check(valid_files)
  class_id_check(valid_files)
  
  ## report-2 calculate each team memeber timespent by munites for each activityCode and generateReport 
  generate_report2(load_activity_logs(files_matching_pattern))

  create_report_three(compile_activity_log_data(load_activity_logs(files_matching_pattern)))
  ## report 4: minutes worked by day of the week
  report4(load_activity_logs(files_matching_pattern))
  report5(load_activity_logs(files_matching_pattern))
  
  
  print_graph_c(load_activity_logs(files_matching_pattern))
  
  print(GOODBYE)

# entry point
if __name__=='__main__':
  main()