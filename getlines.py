import os

#Returns a list containing the lines of a file, stripping the leading and trailing whitespaces, as well as the os new line separator if indicated with "strip_blanks"
def getlines(source_file:str, strip_blanks:bool = False, verbose:bool = False):
  lines = []
  line_sep = os.linesep

  try:
    with open(source_file, 'r') as this_file:
      contents = this_file.readlines()

      if strip_blanks:
        #Iterate over the lines extracted and remove trailing and leading whitespaces
        #as well as the OS new line separator
        for line in contents:
          line = line.strip(line_sep).strip()
          if line == '':
            continue
          lines.append(line)
      else:
        lines = contents

    if verbose == True: #verbose
      print(f'Lines read:\n{lines}')
  except FileNotFoundError:
    print(f"ERROR!!: File {source_file} not found, make sure that the path is correct.")

  return lines