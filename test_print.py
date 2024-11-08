from log_entry import LogEntry
#temporary
#for debugging
#if you have an issue with the activity log files by student data structure,
# you can use this function to print all the data in the data structure for examination
def print_main_data_struct(activity_logs_by_student: dict[str, list[LogEntry]] ):
  for key in activity_logs_by_student:
    print("\n\n\n" + key + "'s Activity Log File:\n\n")
    for log_entry in activity_logs_by_student[key]:
      print(log_entry)