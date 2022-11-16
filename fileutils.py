#fileutils v1.0.1
import os

def getconfig(config_file, verbose:bool = False):
  #Returns a dictionary containing the parameters in a config file passed as reference. 
  #Values and keys in the returned dictionary are of type string.

  params={}
  line_sep=os.linesep #retrieves the line separator for this OS
  try:
    with open(config_file, 'r') as file:  #open config file with variables
      contents = file.readlines()
      file.close()

      line_num=1
      for line in contents:
        if not line.__contains__("="):
          print(f"{config_file}: line {line_num} --> \
            {line.strip(line_sep)}: Parameter not assigned, or empty line. Expecting <PARAM>=<VALUE>.\
              Ignoring, reading next line...")
          continue
        dict_key = line.split("=")[0].replace(" ", "")

        value = line.split("=")[1].replace(" ", "").strip(line_sep)

        if verbose == True: #verbose
          print(f"Parameter: {dict_key} , Value: {value}")

        params[dict_key]=value
        line_num += 1

      if verbose == True: #verbose
        print(f'Parameters read:\n{params}') #DEBUG
  except FileNotFoundError:
    print(f"ERROR!!: File {config_file} not found, make sure that the path is correct.")
  return params