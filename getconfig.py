import os

#Returns a dictionary containing the parameters in a config file passed as reference. 
#Values and keys in the returned dictionary are of type string.
#Check README.md for additional information
def getconfig(config_file:str, assignment_op:str = "=", skip_empty_values:bool = False, verbose:bool = False):
  params={}
  line_sep=os.linesep #retrieves the line separator for this OS
  try:
    with open(config_file, 'r') as f:  #open config file with variables
      contents = f.readlines()

      line_num = 0
      for line in contents:
        line_num += 1

        if line.strip(line_sep).strip() == '':  #empty line, ignored
          print(f"line {line_num} is empty....ignoring")  #DEBUG
          continue
        #Check if the line contains the assignment operator
        if not line.__contains__(assignment_op):
          msg = f"{config_file}: line {line_num} --> \'{line.strip(line_sep)}\': \nMissing or incorrect assignment. Expecting <PARAM> {assignment_op} <VALUE>.\n1) Check you are using operator \'{assignment_op}\' for your definitions \n2) If parameter is not being used in your application, still put the assignment operator next to the parameter but do not type a value to its right \'<PARAM> {assignment_op} \'"
          raise ValueError(msg)
          
        #split the line in [parameter,value] pair
        slice = line.split(assignment_op)
        #Check the assignment operator is not repeating
        if len(slice) != 2:
          raise ValueError(f"Expecting <PARAM>{assignment_op}<VALUE>.\nExpecting exactly one assignment per line read")
        
        #Extract key and value, and remove the leading and trailing spaces, as well as new line separator
        dict_key = slice[0].strip(line_sep).strip()
        value = slice[1].strip(line_sep).strip()

        if value == '' and skip_empty_values:
          if verbose == True: #verbose
            print(f"{config_file}: line {line_num} --> Ignoring unassigned parameter'{dict_key}'")
          continue

        if verbose == True: #verbose
          print(f"Parameter: {dict_key} , Value: {value}")

        params[dict_key]=value

      if verbose == True: #verbose
        print(f'Parameters read:\n{params}')
  except FileNotFoundError:
    print(f"ERROR!!: File {config_file} not found, make sure that the path is correct.")
  return params
