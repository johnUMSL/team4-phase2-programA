"""lead programmer: Alewiya Duressa
 Phase-3 Report-2
 The program reads time log files containing team member activities, 
 calculates the total time spent on each activity code (from 0 to D in hexadecimal order), 
 and generates a report in a table format.
 https://stackoverflow.com/questions/48447123/convert-time-hhmmss-to-minutes-in-python
"""
from constants import ACTIVITY_CODES,COURSE_CODE
from load_logs import load_activity_logs
from log_entry import LogEntry
from datetime import datetime
from helpers import readyToContinue
#https://stackoverflow.com/questions/48447123/convert-time-hhmmss-to-minutes-in-python
def calculate_activity_minutes(activity_logs: dict[str, list[LogEntry]]) -> dict[str, int]:
    #initialize activity minutes for hexadecimal codes 0 to D
    activity_minutes =  activity_minutes = {hex(i)[2:].upper(): 0 for i in range(14)}
    # for activitycode calculate each person time spent 
    for logs in activity_logs.values():
        for log_entry in logs:
            start_time = datetime.strptime(log_entry.start_time, "%H:%M")
            end_time = datetime.strptime(log_entry.end_time, "%H:%M")
            duration_minutes = (end_time - start_time).seconds // 60
            if log_entry.activity_code not in activity_minutes:
                activity_minutes[log_entry.activity_code] = 0
            activity_minutes[log_entry.activity_code] += duration_minutes
    return activity_minutes

# Function to generate a formatted report
def generate_report2(activity_minutes):
    """
    Generates a formatted table of total minutes spent on each activity code.

    Parameters:
    activity_minutes (dict[str, int]): Dictionary with activity codes as keys and total minutes as values.

    Returns:
    str: Formatted table as a string.
    """
    print("Report-2")
    table_header = "ACTIVITY CODE        MINUTES SPENT BY ALL TEAM MEMBERS\n"
    table_rows = ""
    for code in sorted(activity_minutes.keys(), key=lambda x: int(x, 16)):  # Sort in hexadecimal order
        table_rows += f"{code:<20}{activity_minutes[code]}\n"
    return table_header + table_rows