import os

def getconfig(config_file, verbose:bool = False):
  params={}
  line_sep=os.linesep #retrieves the line separator for this OS
  file = open(config_file, 'r') #open config file with variables
  contents = file.readlines()
  file.close()

  line_num=1
  for line in contents:
    if not line.__contains__("="):
      print(f"{config_file}: line{line_num} --> \
        {line.strip(line_sep)}: not an assigned parameter. Expecting <PARAM>=<VALUE>")
      continue
    dict_key = line.split("=")[0].replace(" ", "")

    if verbose == True: #verbose
      print("Parameter:" + dict_key)

    value = line.split("=")[1].replace(" ", "").strip(line_sep)

    if verbose == True: #verbose
      print("Value: " + str(value))

    params[dict_key]=value
    line_num += 1

  if verbose == True: #verbose
    print(f'Parameters read:\n{params}') #DEBUG
  return params