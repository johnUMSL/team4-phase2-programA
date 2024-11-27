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
    correct_files = [file for file in os.listdir('.') if file.endswith('.csv')]

    if not correct_files:
        print("No valid CSV files in current directory.")
        return None

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

    if working_data:
        final_data = pd.concat(working_data, ignore_index=True)

        format = final_data.to_string(index=True, col_space=3, header=True)
        edges = "+" + "-" * (len(format.split("/n")[0]) - 2) + "|"

        format_table = edges + "\n" #creates the top border
        format_table += "| " + " | ".join(final_data.columns) + "\n"
        format_table += edges + "\n" #bottom of the header
        # adding in rows
        for index, row in final_data.iterrows():
            format_table += "| " + " | ".join(f"{value:<20}" for value in row) + "|\n"
            format_table += edges

        file = "report1.txt"
        with open(file, "w") as f:
            f.write(format_table)


        x = final_data['name'].tolist()
        y = final_data['time'].tolist()

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