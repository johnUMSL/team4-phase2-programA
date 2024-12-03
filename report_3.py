from datetime import datetime
import pandas as pd
from tabulate import tabulate
import seaborn as sns
import matplotlib.pyplot as plt

# alculate the time spent between a start time and an end time in minutes
def calculate_time_spent(start_time, end_time):
  format = "%H:%M" # set the time format
  start = datetime.strptime(start_time, format) #convert start_time to datetime
  end = datetime.strptime(end_time, format) #convert end_time to datetime
  time = int((end - start).total_seconds() / 60) # caclulate the difference in minutes; convert to an integer
  return time

# compile activity log data into a dictionary of time spent per activity code for each student
def compile_activity_log_data(activity_logs):
  data = {} # create an empty dictionary to store data

  # loop through each student and their log entries
  for student, log_entries in activity_logs.items():
    if student not in data:
      data[student] = {} # create a dictionary for each student if it doesn't exist

    # loop through each log entry for the student
    for log_entry in log_entries:
      # calculate the time spent on the activity and store in a variable
      time_spent = calculate_time_spent(log_entry.start_time, log_entry.end_time)

      if log_entry.activity_code not in data[student]:
        data[student][log_entry.activity_code] = 0 # set time spent to 0 if activity code doesn't already exist
      data[student][log_entry.activity_code] += time_spent # add time_spent to the activity code for the student

  # return the data dictionary
  return data

# create a report in grid format and save it as a text file
def create_report_three(data, file='PhaseThreeReport3.txt'):
  # create column order for the table: 1-9, A-D
  column_order = [hex(i)[2:].upper() for i in range(14)]

  # convert the data dictionary to a pandas dataframe
  df = pd.DataFrame.from_dict(data, orient='index').fillna(0).astype(int) # Resource #14

  # re-order columns using column_order
  df = df.reindex(columns=column_order, fill_value=0) # Resource #15

  # reset the index and rename the first column to 'Names'
  df.reset_index(inplace=True) # Resource #15
  df.rename(columns={'index': 'Names'}, inplace=True)

  # Save the DataFrame to a file in a grid format using the tabulate library
  with open(file, 'w') as f:
    f.write(
    "Report 3: Minutes Spent on each Activity by Each Team Member\n"
    "Class ID: CS 4500\n"
    "Team 7: Matthew Dobbs, John Garrett, Logan Bessinger, Connor Gilmore, Alewiya Duressa, and Aaron Graham\n"
    "Report 3 contains the amount by time spent (in minutes) on each activity by each team member.\n\n"
    )
    f.write(tabulate(df, headers='keys', tablefmt='grid', showindex=False)) # Resource #16)
    print(f"Report saved to {file}")
  return df

# function to create and display graph b using dataframe from report 3clclear
def create_graph_b(data: pd.DataFrame, title="Graph B", xlabel="Activity Codes", ylabel="Names"):
  # set the 'Names' column as the index
  data.set_index("Names", inplace=True)

  # create a new figure set dimensions
  plt.figure(figsize=(14,10))

  # create a heatmap with a grid and shades of grren filling the cells. 
  sns.heatmap(data, cmap="Greens", linewidths=0.5, cbar_kws={"label": "Minutes Spent"})
  
  # set title and labels font sizes
  plt.title(title, fontsize=16)
  plt.xlabel(xlabel, fontsize=12)
  plt.ylabel(ylabel, fontsize=12)

  # make both x and y axis labels horizontal without any rotations
  plt.xticks(rotation=0)
  plt.yticks(rotation=0)

  # display the plotted heatmap
  plt.show()

  return None