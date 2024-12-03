"""lead programmer: Alewiya Duressa
 Phase-3 Report-2
 The program reads time log files containing team member activities, 
 calculates the total time spent on each activity code (from 0 to D in hexadecimal order), 
 and generates a report in a table format.
 https://stackoverflow.com/questions/48447123/convert-time-hhmmss-to-minutes-in-python
 https://stackoverflow.com/questions/5082452/string-formatting-vs-format-vs-f-string-literal
"""
from log_entry import LogEntry
from datetime import datetime
#https://stackoverflow.com/questions/48447123/convert-time-hhmmss-to-minutes-in-python
#https://stackoverflow.com/questions/5082452/string-formatting-vs-format-vs-f-string-literal
## Calcualtes the total time spent on each activity by all memebers
## Takes dictionary where the key is fullname and value is array of all the log entries object for that person
# it calculate time spent on each activitycode by all team members 
# return dictionary key activityCode and value total time spent in munites 
def calculate_activity_minutes(activity_logs: dict[str, list[LogEntry]]) -> dict[str, int]:
    #initialize activity minutes for hexadecimal codes 0 to D
    activity_minutes =  activity_minutes = {hex(i)[2:].upper(): 0 for i in range(14)}
    # for activitycode calculate each person time spent 
    for logs in activity_logs.values():
        #get the start time,end time and calcualte the duration 
        for log_entry in logs:
            start_time = datetime.strptime(log_entry.start_time, "%H:%M")
            end_time = datetime.strptime(log_entry.end_time, "%H:%M")
            duration_minutes = (end_time - start_time).seconds // 60
            if log_entry.activity_code not in activity_minutes:
                activity_minutes[log_entry.activity_code] = 0
            activity_minutes[log_entry.activity_code] += duration_minutes
    return activity_minutes

# Function to generate a formatted report 2 time spent in munites for all activitycode by all memeber
"""
call calculate_activity_minutes set to activity_minutes variable 
activity_minutes (dict[str, int]): Dictionary with activity codes
Generates a formatted table of total minutes spent on each activity code.
Parameters:
activity_log dicitionary
Returns:
report str: Formatted table as a string.
"""
def generate_report2(teams_log_entries):
    output_file="PhaseThreeReport2.txt"
    activity_minutes=calculate_activity_minutes(teams_log_entries)
    table_header = "ACTIVITY CODE        MINUTES SPENT BY ALL TEAM MEMBERS\n"
    table_rows = ""
    for code in sorted(activity_minutes.keys(), key=lambda x: int(x, 16)):  # Sort in hexadecimal order
        #https://stackoverflow.com/questions/5082452/string-formatting-vs-format-vs-f-string-literal
        table_rows += f"{code:<20}{activity_minutes[code]}\n"
    report_content= table_header + table_rows
     # Save the report to the specified file
    """with open(output_file, "w") as file:
        file.write(report_content)
    print("Report-2 has beem generated and saved to PhaseThreeReport2.txt file.")"""
    try:
        with open(output_file, "w") as file:
            file.write("Report 2: Minutes Spent on each Activity by Each Team Member\n"
            "Class ID: CS 4500\n"
            "Team 7: Matthew Dobbs, John Garrett, Logan Bessinger, Connor Gilmore, Alewiya Duressa, and Aaron Graham\n"
            "Report 2 contians activityCode (from 0 to D in hexadecimal order) as first column and total time spent on each activity code in munities\n\n")
            file.write(report_content)
        print("Report-2 has been generated and saved to PhaseThreeReport2.txt file.")
    except Exception as e:
        print(f"An error occurred while saving the report: {e}")
