# fileutils.py

Library to facilitate interacting with files.   
It is also an executable script that can be invoked from CLI with arguments.

Usage: 
    python fileutils.py <function> <arg1> <arg2> ... <arg n>

    Available functions:
    diffiles: Compare the contents of two files and print the differences. See compare_files(file1, file2, mode: str) below.

Library modules:
    fileutils.py: Executable script. Main script.
    diffiles.py: Executable script. 
    getconfig.py: Returns a dictionary containing the parameters in a config file passed as reference. 
    getlines.py: Return lines in a file.

Library functions:
    getconfig(config_file:str, assignment_op:str = "=", skip_empty_values:bool = False, verbose:bool = False)
        Returns a dictionary containing the parameters and values in a config file. Values and keys in the dictionary are of type string.

        Params:
            config_file: Path of the config file to be read
            assignment_op: Assignment operator used in the config file. Default is '='
            skip_empty_values: Indicate if empty parameters should be collected and returned
            verbose: Enable chatty output

    getlines(source_file:str, strip_blanks:bool = False, verbose:bool = False)
        Return lines in a file.

        Params:
            source_file: Path of the file to be read
            strip_blanks: Strip leading and trailing white spaces and OS line separator
            verbose: Enable chatty output

    compare_files(file1, file2, mode: str):
        Compares the contents of two files and prints the differences.

        Params:
            file1 and file2 are the names of the files to compare
            'mode' is a string indicating the comparison mode:
                'diff': print lines that are different
                'same': print lines that are the same
                'merged': print the lines side by side, highlighting the differences

        Example: python diffiles.py file1.txt file2.txt diff
            This command will compare the contents of file1.txt and file2.txt, and print the lines that are different.