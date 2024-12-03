## Report 4, Programmer: Logan Bessinger
## The Report will contain the days of the Week and how many minutes were worked durring thoses days for all the Logs combined.
import copy
from log_entry import LogEntry
from tabulate import tabulate
import datetime 

## Get Weekday from Date
def check_weekday(date):
    month, day, year = (int(i) for i in date.split('/'))    
    the_date = datetime.date(year, month, day)
    day_of_week = the_date.weekday()  # Monday is 0 and Sunday is 6
    return day_of_week
## Get Minutes Spent Working
def get_minutes(start_time, end_time):
    start_hour, start_minutes = (int(i) for i in start_time.split(':'))    
    end_hour, end_minutes = (int(i) for i in end_time.split(':'))
    minutes = end_minutes - start_minutes + (end_hour - start_hour) * 60
    return minutes

def report4(activity_logs_by_student: dict[str, list[LogEntry]]):
    ## Set up Weekday Data. Start at 0
    MondayMinutes = 0
    TuesdayMinutes = 0
    WednesdayMinutes = 0
    ThursdayMinutes = 0
    FridayMinutes = 0
    SaturdayMinutes = 0
    SundayMinutes = 0
    ## Run through all data entries
    for key in activity_logs_by_student:
        for log_entry in activity_logs_by_student[key]:
            date = check_weekday(log_entry.date)
            minutes = get_minutes(log_entry.start_time,log_entry.end_time)
            ## Add minutes to date data
            if (date == 0):
                MondayMinutes += minutes
            if (date == 1):
                TuesdayMinutes += minutes
            if (date == 2):
                WednesdayMinutes += minutes
            if (date == 3):
                ThursdayMinutes += minutes
            if (date == 4):
                FridayMinutes += minutes
            if (date == 5):
                SaturdayMinutes += minutes
            if (date == 6):
                SundayMinutes += minutes
    ## Write Entry and Data to file
    file = open("PhaseThreeReport4.txt", "w")
    file.write("Report 4: Minutes Worked by the Day of the Week\n")
    file.write("Class ID: CS 4500\n")
    file.write("Team 7: Matthew Dobbs, John Garrett, Logan Bessinger, Connor Gilmore, Alewiya Duressa, and Aaron Graham.\n")
    file.write("The following is a report containing the days of the week and \nhow many minutes were worked each day by the people included in the Logs.\n")
    file.write("People Inckuded in the report:\n\n")
    for key in activity_logs_by_student:
        file.write(key)
        file.write("\n")
    tabledata = [
        ["Monday", MondayMinutes], 
        ["Tuesday", TuesdayMinutes], 
        ["Wendesday", WednesdayMinutes],
        ["Thursday", ThursdayMinutes], 
        ["Friday", FridayMinutes], 
        ["Saturday", SaturdayMinutes],
        ["Sunday", SundayMinutes]
    ]
    header = ["Day", "Minutes Worked"]
    file.write(tabulate(tabledata, headers=header, tablefmt="grid"))

    file.close()
