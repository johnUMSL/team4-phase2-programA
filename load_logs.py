import csv
from constants import FIRST_NAME_INDEX,LAST_NAME_INDEX,DATE_INDEX, START_TIME_INDEX, END_TIME_INDEX, GROUP_SIZE_INDEX, ACTIVITY_CODE_INDEX, NOTE_INDEX
from log_entry import LogEntry
#parses all valid csv files
#collects username from header to create dictionary key 
#calls function to parse remaning log rows to create dictionary value
#returns dictionary where each key value is a student name and each value is all the activity log entities associated with that student
def load_activity_logs(file_paths: list) -> dict[str, list[LogEntry]]:
   results:dict[str, list[LogEntry]] = {}
   for file_path in file_paths:
    with open(file_path, mode='r') as file:
       file_reader_obj = csv.reader(file)
       username: list[str] = next(file_reader_obj) #https://stackoverflow.com/questions/14551484/trying-to-understand-python-csv-next
       course = next(file_reader_obj) #just iterating over, not doing anything with course here
       first_name = username[FIRST_NAME_INDEX]
       last_name = username[LAST_NAME_INDEX]
       full_name_key = first_name + " " + last_name
       results[full_name_key] = read_student_log_entries(file_reader_obj)

   return results
    
#reads through all logs in a csv file. 
#converts each log row into a log object and appends it to list. 
#returns list to represent all log entries in file being parsed
def read_student_log_entries(file_reader_obj) -> list[LogEntry]:
     results: list[LogEntry] = []
     for log_row in file_reader_obj:
        log_entry = build_log_entry(log_row)
        results.append(log_entry)
     return results

 #creates Logn Entry Object to represent log row
def build_log_entry(log_row: list[str]) -> LogEntry:

    result = LogEntry(date=log_row[DATE_INDEX], 
                     start_time=log_row[START_TIME_INDEX],
                     end_time=log_row[END_TIME_INDEX],
                     group_size=int(log_row[GROUP_SIZE_INDEX]),
                     activity_code=log_row[ACTIVITY_CODE_INDEX],
                     note=log_row[NOTE_INDEX]
                     )
    return result