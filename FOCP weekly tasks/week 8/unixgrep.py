'''The Unix grep command searches a file and outputs the lines in the file that
contain a certain pattern. Write an implementation of this. It will take two
command-line arguments: the first is the string to look for, and the second is the
file name. The output should be the lines in the file that contain the string.'''

import sys

if len(sys.argv) != 3:
    print("Usage: python grep.py <pattern> <filename>")
else:
    pattern = sys.argv[1]
    filename = sys.argv[2]
    
    try:
        with open(filename, 'r') as file:
            for line in file:
                if pattern in line:
                    print(line, end='')
    except:
        print(f"Error: The file '{filename}' could not be opened.")
