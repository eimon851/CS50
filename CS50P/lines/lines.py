# import necessary modules (sys, os)

import sys

# check if number of command-line arg is = 2
    #(the script name, file name)
# else, exit the program

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

# check if file name ends with .py
# else, exit the program
# check if the file exist
# else, exit the program
# open the file and read it line by line

try:
    if sys.argv[1].endswith(".py"):
        file = open(sys.argv[1], "r")

            # For each line, check if it's a comment of blank line
        count = 0
        for line in file:
            if line.lstrip().startswith("#") or len(line.strip()) == 0:
                continue
            else:

                    # if not, increment a counter
                count = count + 1

            # finally, print the counter
        print(count)
    else:
        sys.exit("Not a Python file")

except FileNotFoundError:
    sys.exit("File does no exist")













