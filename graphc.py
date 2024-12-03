from datetime import datetime
from log_entry import LogEntry
from helpers import readyToContinue
import plotext as plot  # external dependency; must be installed
import numpy as np

def print_graph_c(activity_logs_by_student: dict[str, list[LogEntry]] ):
  """
  print_graph_c
  AUTHOR:  Matthew Dobbs
  PURPOSE: gathers graph c data from common dictionary, generates graph, and exits
  INPUTS:  dict: k,v store comprised of log files and log entries in log files
  OUTPUTS: none (console output only) 
  """

  # dict to store dates and minutes from log files
  minutes_by_date = {}

  for key in activity_logs_by_student:
    for log_entry in activity_logs_by_student[key]:
      # convert date, start time, and end time fields to datetime format
      date_convert = datetime.strptime(log_entry.date, '%m/%d/%Y').date().strftime('%Y%m%d')
      time1_convert = datetime.strptime(log_entry.start_time, '%H:%M')
      time2_convert = datetime.strptime(log_entry.end_time, '%H:%M')
      # source: https://pynative.com/python-get-time-difference/
      # print('START: ', time1_convert.time(), ' END: ', time2_convert.time())
      delta = time2_convert - time1_convert

      # if date exists in dict, add minutes logged to existing dict.
      # else, create dict and set value equal to minutes logged in current entry
      if date_convert in minutes_by_date:
        minutes_by_date[date_convert] += int(delta.seconds/60)
      else:
        minutes_by_date[date_convert] = int(delta.seconds/60)


  # convert generated dict to sorted lists for graph
  list_to_sort = list(minutes_by_date.keys())
  list_to_sort.sort()
  sorted_minutes_by_date = {i: minutes_by_date[i] for i in list_to_sort}
  dates = list(sorted_minutes_by_date.keys())
  minutes = list(sorted_minutes_by_date.values())

  plot.bar(dates, minutes)
  plot.title("Graph C - Total Team Minutes by Date")
  plot.xlabel('Date')
  plot.ylabel('Team Minutes')
  # Reduce plot size to fit terminal window with continue msg
  plot.plot_size(plot.terminal_width(), plot.terminal_height()-2)

  # Set y ticks to whole numbers (if needed)
  whole_y_ticks = np.arange(int(min(minutes)), int(max(minutes)))
  plot.yticks(whole_y_ticks)
  plot.show()

  readyToContinue()