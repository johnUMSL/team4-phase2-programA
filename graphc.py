from datetime import datetime
from log_entry import LogEntry
from helpers import readyToContinue
import plotext as plot  # external dependency; must be installed
import numpy as np

def print_graph_c(activity_logs_by_student: dict[str, list[LogEntry]] ):
  # TODO instantiate array to sum minutes per day
  
  minutes_by_date = {}

  for key in activity_logs_by_student:
    print("\n\n\n" + key + "'s Activity Log File:\n\n")
    for log_entry in activity_logs_by_student[key]:
      date_convert = datetime.strptime(log_entry.date, '%m/%d/%Y').date().strftime('%Y%m%d')
      time1_convert = datetime.strptime(log_entry.start_time, '%H:%M')
      time2_convert = datetime.strptime(log_entry.end_time, '%H:%M')
      # source: https://pynative.com/python-get-time-difference/
      # print('START: ', time1_convert.time(), ' END: ', time2_convert.time())
      delta = time2_convert - time1_convert

      if date_convert in minutes_by_date:
        minutes_by_date[date_convert] += int(delta.seconds/60)
      else:
        minutes_by_date[date_convert] = int(delta.seconds/60)
      # print(minutes_by_date[date_convert])
      # print('DELTA: ', delta)
      # print(date_convert)

  list_to_sort = list(minutes_by_date.keys())
  list_to_sort.sort()
  sorted_minutes_by_date = {i: minutes_by_date[i] for i in list_to_sort}
  # print(sorted_minutes_by_date)
  dates = list(sorted_minutes_by_date.keys())
  minutes = list(sorted_minutes_by_date.values())

  plot.bar(dates, minutes)
  plot.title("Graph C - Total Team Minutes by Date")
  plot.xlabel('Date')
  plot.ylabel('Team Minutes')
  # whole_x_ticks = np.arange(int(min(dates)), int(max(dates)) + 1)
  # plot.xticks(whole_x_ticks)

  # Set y ticks to whole numbers (if needed)
  whole_y_ticks = np.arange(int(min(minutes)), int(max(minutes)))
  plot.yticks(whole_y_ticks)
  plot.show()

  readyToContinue()