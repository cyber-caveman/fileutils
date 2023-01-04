#fileutils v1.2.0

import sys
import os

from diffiles import compare_files
from getconfig import getconfig
from getlines import getlines

# Usage message
USAGE = '''
Usage: python fileutils.py <function> <arg1> <arg2> ... <arg n>

Available functions:
  diffiles: Compare the contents of two files and print the differences
'''

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
    else:
        print(f'Error: Invalid function name: {function_name}')
        print(USAGE)
        sys.exit(1)

if __name__ == '__main__':
    main()