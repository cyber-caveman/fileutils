#fileutils v1.2.1

import sys
import os

from diffiles import compare_files
from getconfig import getconfig
from getlines import getlines

# Usage message
USAGE = '''
Usage: python fileutils.py <function> <arg1> <arg2> ... <arg n>

Available functions:
    diffiles: Compare the contents of two files, line by line, and print the differences
        params: file1, file2, mode
            Where mode is either "diff", "same", or "merged"
                diff: prints the lines that are different
                same: prints lines that match
                merged: prints all common and uncommon lines, uncommon lines printed side by side
    getconfig: Returns parameters in a config file passed as reference, formatted as dictionary
        params: config_file, assignment_op, skip_empty_values [False | True], verbose [False | True]
    getlines: Returns a list containing the lines of a file, stripping the leading and trailing whitespaces, as well as the os new line separator if indicated with "strip_blanks"
        params: source_file, strip_blanks [False | True], verbose [False | True]
'''

#Gets absolute path of file from a relative path
def get_file_abs_path(file_path: str):
    abs_path = file_path
    if not os.path.isabs(abs_path):     #Check if the user provided a relative path
        path = os.path.join(os.path.dirname(__file__), abs_path)    #build the absolute path
        abs_path = os.path.abspath(path)    #get the absolute path as a string
    return abs_path

def main():
    # Parse the command-line arguments
    args = sys.argv[1:]

    if not args:
        print('Error: No arguments provided')
        print(USAGE)
        sys.exit(1)

    # Get the function name and function arguments
    function_name = args[0]
    func_args = args[1:]

    # Import the function and call the appropriate function
    if function_name == 'diffiles':
        from diffiles import compare_files
        compare_files(*func_args)
    elif function_name == 'getconfig':
        try:
            if func_args[2] == 'False' or func_args[1] == 'false':
                func_args[2] = False
            elif func_args[2] == 'True' or func_args[1] == 'true':
                func_args[2] = True
            if func_args[3] == 'False' or func_args[1] == 'false':
                func_args[3] = False
            elif func_args[3] == 'True' or func_args[1] == 'true':
                func_args[3] = True
            params = getconfig(*func_args)
        except IndexError:
            params = getconfig(*func_args)

        print(params)
    elif function == 'getlines':
        try:
            if func_args[1] == 'False' or func_args[1] == 'false':
                func_args[1] = False
            elif func_args[1] == 'True' or func_args[1] == 'true':
                func_args[1] = True
            if func_args[2] == 'False' or func_args[1] == 'false':
                func_args[2] = False
            elif func_args[2] == 'True' or func_args[1] == 'true':
                func_args[2] = True
            lines = getlines(*func_args)
            print(lines)
        except IndexError:
            lines = getlines(*func_args)
            print(lines)
    else:
        print(f'Error: Invalid function name: {function_name}')
        print(USAGE)
        sys.exit(1)

if __name__ == '__main__':
    main()