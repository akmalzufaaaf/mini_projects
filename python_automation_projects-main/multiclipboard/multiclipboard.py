# allow user to copy multiple unit
import sys
import clipboard 
import json

# define a function called save
def save_data(filepath, data):
  with open(filepath, "w") as f:
    json.dump(data, f)
   
# define load function
def load_data(filepath):    # this function will load a data/file in dictionary form
  try:
    with open(filepath, "r") as f:
      data = json.load(f)
      return data
  except:
    return {}
  
# make a workflow when the program start
if len(sys.argv) == 2:
  command = sys.argv[1]
  data = load_data(SAVED_DATA)
  
  if command == "save":
    key = input("type your key: ")
    data[key] = clipboard.paste()
    save_data(SAVED_DATA, data)
    print("Data succesfully saved!")
  elif command == "load":
    key = input("enter a key: ")
    if key in data:
      clipboard.copy(data[key])
      print("Item Copied")
    else:
      print("Key does not exist")
   elif command == "list":
    print(data)
  
