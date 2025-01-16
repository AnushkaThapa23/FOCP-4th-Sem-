'''The Unix nl command prints the lines of a text file with a line number at the start
of each line. (It can be useful when printing out programs for dry runs or white-box
testing). Write an implementation of this command. It should take the name of the
files as a command-line argument'''

import sys

if len(sys.argv) != 2:
    print("Usage: python nl.py <filename>")
else:
    try:
        with open(sys.argv[1], 'r') as file:
            for line_number, line in enumerate(file, start=1):
                print(f"{line_number}\t{line}", end='')
    except:
        print(f"Error: The file '{sys.argv[1]}' does not exist.")
