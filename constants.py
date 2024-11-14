# Constants used in the activity log program.

# A description of the program 
SUMMARY = """\nThis program processes time logs for a team. It starts by checking if the correct number
of time log files are present (between 2 and 10). It stops and shows an error if there are too few, too many, 
or if any files have duplicate names. It then verifies that each file is valid and that the names inside of
each file are unique. Next, it ensures all logs share the same Class ID, halting with an error if there are
differnces. If there the correct number of files, and all are valid, the program collects data from the
time logs to generate and display reports and graphs. These reports are saved as text files. 
Graphs are shown one at a time, pausing for user input before moving on. The program then ends with a
goodbye message.
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
GOODBYE = """\nThank you for validating your activity log files
before generating your reports.
Your reports have been saved as .txt files.
Goodbye.
"""