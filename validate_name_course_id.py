import os

def unique_name_check(valid_files):
  # create an empty dictionary for name and corresponding file
  names_in_files = {}
  
  for file in valid_files:
    with open(file, mode='r') as f:
      data_points_name = f.readline().split(',') # read the first line of the file and add each string to a list
      name = f"{data_points_name[1]} {data_points_name[0]}" # format strings into a Firstname Lastname format

      if name in names_in_files: # check if name is already in dictionary
        duplicate_name_file = names_in_files[name] # get the file where the duplicate name was found
        raise Exception(f"The name {name} is not unique. {name} is found in {file} and {duplicate_name_file}.")
      
      names_in_files[name] = file # add unique name to the dictionary, mapping to the file it is in
  
  print("\nAll of the names in the valid activity logs are unique.\n")
  return names_in_files

def class_id_check(valid_files):
  # create empty strings for first_file and first_class_id
  first_file = ''
  first_class_id = ''

  for file in valid_files:
    with open(file, mode='r') as f:
      f.readline() # read the first line of the file and skip it
      class_id = f.readline().split(',')[0] # read the second line of the file and assign the first string to a variable

      if first_file == '': # If first file is an empty string - will only be true on first iteration
        first_file = file # assign current file to first_file
        first_class_id = class_id # assign current class_id to first_class_id
      
      elif class_id != first_class_id: # comparison will only run after first iteration
        raise Exception(f"The class ids are not identical. {first_file} has a class id of {first_class_id} and {file} has a class id of {class_id}.")

  print("All of the class ids in the valid activity logs are the same.")
  return None
