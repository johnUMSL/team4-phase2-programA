# Resources used in Program
# 1. https://stackoverflow.com/questions/500864/case-insensitive-regular-expression-without-re-compile - ignore case flag for regex (re) library
# 2. https://stackoverflow.com/questions/48959098/how-to-create-a-new-text-file-using-python

from constants import SUMMARY
from helpers import readyToContinue, clear_console
from csv_functions import find_csv_files, create_validity_file, validate_csv_files

def main():
  clear_console() # clear the console
  print(SUMMARY) # print the SUMMARY from constants.py
  readyToContinue() # wait for user to procedd by entering input

  files_matching_pattern = find_csv_files() 
  create_validity_file(files_matching_pattern)
  validate_csv_files(files_matching_pattern)

  

# entry point
if __name__=='__main__':
  main()