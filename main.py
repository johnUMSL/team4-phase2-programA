# Resources used in Program
# 1. https://stackoverflow.com/questions/500864/case-insensitive-regular-expression-without-re-compile - ignore case flag for regex (re) library
# 2. https://stackoverflow.com/questions/48959098/how-to-create-a-new-text-file-using-python
# 3. https://www.geeksforgeeks.org/how-to-read-specific-lines-from-a-file-in-python/
# 4. https://docs.python.org/3/library/functions.html#enumerate
# 5. https://stackoverflow.com/questions/2489669/how-do-python-functions-handle-the-types-of-parameters-that-you-pass-in
# 7. https://strftime.org/
# 8. https://discuss.python.org/t/best-way-to-validate-an-entered-date/49406/3

from constants import SUMMARY
from helpers import *
from csv_functions import *

def main():
  clear_console() # clear the console
  print(SUMMARY) # print the SUMMARY from constants.py
  readyToContinue() # wait for user to procedd by entering input

  files_matching_pattern = find_csv_files() 
  create_validity_file(files_matching_pattern)
  
  errors = validate_csv_files(files_matching_pattern)
  write_errors_to_file(errors)

  

# entry point
if __name__=='__main__':
  main()