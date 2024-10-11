import os

def clear_console(): # Resource #2
  if os.name == 'nt': #If the OS is Windows 
    os.system('cls') # runs the 'cls' command to clear screen
  else: # for Linux or macOS
    os.system('clear') # runs the 'clear' command to clear screen

def readyToContinue():
  user_input = input("Please enter 'y' or 'Y' when ready to continue.\n")
  while user_input.lower() != 'y': # Prompt user for input until 'Y' or 'y' is entered
    print("Invalid entry.")
    user_input = input("Please enter 'y' or 'Y' when ready to continue.\n")
  print("Beginning file search.....") # Once valid input is entered, print statement and continue