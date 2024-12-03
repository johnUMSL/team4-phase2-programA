# lead programmer: Aaron Graham
# Phase 3 Report 1 Total the minutes worked in each .csv file and save a .txt file with the name of each employee and their total minutes worked
import os
import pandas as pd
import numpy as np
import plotext as plt
from helpers import readyToContinue



# importing plotext information from https://github.com/piccolomo/plotext/blob/master/readme/bar.md
# information used for writing files from https://stackoverflow.com/questions/29223246/how-do-i-save-data-in-a-text-file-python



def report1():
    # checking the validity of the files
    correct_files = [file for file in os.listdir('.') if file.endswith('.csv')]

    if not correct_files:
        print("No valid CSV files in current directory.")
        return None
    # initializing working_data
    working_data = []

    for correct_file in correct_files:
        try:
            df = pd.read_csv(correct_file, header = None)

            if df.shape[1] >= 6:
                name = str(df.iloc[0, 0] + ", " + df.iloc[0, 1])

                try:
                    t1 = pd.to_datetime(df.iloc[:, 1], format='%H:%M', errors='coerce')
                    t2 = pd.to_datetime(df.iloc[:, 2], format='%H:%M', errors='coerce')
                except Exception as e:
                    print(f"Time conversion error in {correct_file}: {e}")
                    continue

                valid = ~pd.isna(t1) & ~pd.isna(t2)
                t1 = t1[valid]
                t2 = t2[valid]

                final_time = ((t2 - t1).dt.total_seconds() / 60).sum()

                working_data.append(pd.DataFrame({'name': [name], 'time': [final_time]}))
            else:
                print(f"name and time columns not found in {correct_file}")

        except Exception as e:
            print(f"Error reading files {correct_file}: {e}")
# createing the table that is then written into a .txt file
    if working_data:
        final_data = pd.concat(working_data, ignore_index=False)

        format = final_data.to_string(index=True, col_space=5, header=True)
        edges = "+" + "-" * (len(format.split("/n")[0]) - 2) + "|"

        format_table = edges + "\n" #creates the top border
        format_table += "| " + " | ".join(final_data.columns) + "\n"
        format_table += edges + "\n" #bottom of the header
        # adding in rows
        for index, row in final_data.iterrows():
            format_table += "| " + " | ".join(f"{str(value):<5}" for value in row) + "|\n"
            format_table += edges + "\n"

        file = "Phase3Report1.txt"
        with open(file, "w") as f:
            f.write("Report 1: Total Minutes in each report for each individual log \n")
            f.write("Class ID: CS4500\n")
            f.write("Team 7: Matthew Dobbs, John Garrett, Logan Bessinger, Connor Gilmore, Alewiya Duressa, and Aaron Graham.\n")
            f.write("The following is a report containing the total minutes worked for each individual.\n")
            f.write("People Included in the report: \n\n")
            f.write(format_table)
# message telling the user the name of the report file
        print(f"The report was saved to {file}")
# using plotext to create a bar graph in terminal for the information that was extracted from the .csv files
# changing the name of the x and y axis of the graph to be acurate to what they need to be.
        x = final_data['name'].tolist()
        y = final_data['time'].tolist()
# setting the names and colors for the information
        plt.bar(x, y, label = "Graph A", color = "red")
        plt.title("Graph A")
        plt.xlabel("Name")
        plt.ylabel("Minutes Worked")
        plt.show()
        print(final_data)

        return final_data
    else:
        print("No valid data extracted")
        return None

readyToContinue()