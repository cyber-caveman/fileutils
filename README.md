# fileutils.py

   Module to facilitate interacting with files, for example, config files for Python scripts.     

def getconfig(config_file:str, assignment_op:str = "=", skip_empty_values:bool = False, verbose:bool = False)
    Returns a dictionary containing the parameters and values in a config file. Values and keys in the dictionary are of type string.

    Params:
        config_file: Path of the config file to be read
        assignment_op: Assignment operator used in the config file. Default is '='
        skip_empty_values: Indicate if empty parameters should be collected and returned
        verbose: Enable chatty output

def getlines(source_file:str, strip_blanks:bool = False, verbose:bool = False)
    Return lines in a file.

    Params:
        source_file: Path of the file to be read
        strip_blanks: Strip leading and trailing white spaces and OS line separator
        verbose: Enable chatty output

