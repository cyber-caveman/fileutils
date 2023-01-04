import sys

def compare_files(file1, file2, mode: str):
    # Open the files in read-only mode
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        # Read the lines from both files
        lines1 = f1.readlines()
        lines2 = f2.readlines()

        # Initialize a counter for the line number
        line_number = 1

        # Compare the lines in both files
        for line1, line2 in zip(lines1, lines2):
            # If the mode is 'diff', print lines that are different
            if mode == 'diff' and line1 != line2:
                print(f'Line {line_number}: {line1.strip()} != {line2.strip()}')
            # If the mode is 'same', print lines that are the same
            elif mode == 'same' and line1 == line2:
                print(f'Line {line_number}: {line1.strip()} == {line2.strip()}')
            # If the mode is 'merged', print the lines side by side
            elif mode == 'merged':
                # Highlight the difference between the two lines
                if line1 != line2:
                    print(f'Line {line_number}: {line1.strip():<{len(line1) + 1}}||{line2.strip():>{len(line2) + 1}}')
                else:
                    print(f'Line {line_number}: {line1.strip()}')
            line_number += 1

if __name__ == '__main__':
    # Check if the correct number of arguments were passed
    if len(sys.argv) != 4:
        print('Usage: python compare_files.py file1 file2 mode')
        print('Where mode is either "diff", "same", or "merged"')
        sys.exit(1)

    # Assign the arguments to variables
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    mode = sys.argv[3]

    # Check if the mode is valid
    if mode not in ['diff', 'same', 'merged']:
        print('Error: Invalid mode. Mode must be either "diff", "same", or "merged"')
        sys.exit(1)

    # Compare the files
    compare_files(file1, file2, mode)


