# use function setup: def main, check_cmd_line_args

import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2: # elif > if
    sys.exit("Too many command-line arguments")

try:
    if sys.argv[1].endswith(".py"): # this line can be put into def check function
        # alternative: if ".py" not in sys.arg[1]

        file = open(sys.argv[1], "r")
        # lines = file.readlines()
        # print(lines) => a list of each line as strings even \n
        count = 0
        for line in file:
            # it seems like a good idea to create functions to check conditions
            if line.lstrip().startswith("#") or len(line.strip()) == 0:
                # so in new function id do
                # line.lstrip().startswith("#"):
                # return True
                # line.isspace() 
                continue
            else:
                count = count + 1
        print(count)

    else: # this line can be put into def check function
        sys.exit("Not a Python file")

except FileNotFoundError:
    sys.exit("File does no exist")













