# Constants used in the activity log program.

# A description of the program 
SUMMARY = """\nThis program validates internal log files. It first checks for properly formatted file names
(XLog.csv - where X is a string of alphabetic characters), then checks for properly formatted file contents. 
The program outputs errors and/or incorrect formats to an external report file and to the screen. 
After the program processes all the files with a valid filename, the program outputs a final report
and halts with a goodbye message.
"""

# Course Code
COURSE_CODE = "CS 4500"

# Activity Codes and definitions
ACTIVITY_CODES = {
  "0": "Reading Canvas Site or Textbook",
  "1": "Studying Using a Practice Quiz",
  "2": "Taking a Scoring Quiz",
  "3": "Participating in a Canvas Discussion, DX",
  "4": "Meeting with your Team",
  "5": "Working on Documentation",
  "6": "Working on Designs",
  "7": "Programming",
  "8": "Working on a Test Plan or Doing Testing",
  "9": "Studying for the Final Exam",
  "A": "Conferring with the Instructor Outside of a Team Meeting",
  "B": "Working on a Mini-Lecture Video or Reading",
  "C": "Viewing a Video or Website that is not a Mini-Lecture, but Relevant to the Course",
  "D": "Other" 
}

# Goodbye message
GOODBYE = """\nThank you for validating the your activity log files.
The report has been saved to ValidityChecks.txt
Goodbye.
"""

#index values to access clearly elements in a log file row
DATE_INDEX = 0
START_TIME_INDEX = 1
END_TIME_INDEX = 2
GROUP_SIZE_INDEX = 3
ACTIVITY_CODE_INDEX = 4
NOTE_INDEX = 5
#index values for headers (first row)
FIRST_NAME_INDEX = 1
LAST_NAME_INDEX = 0