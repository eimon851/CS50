# take a csv file and turn it into a table
# import necessary modules: sys, tabulate

import sys
import csv
from tabulate import tabulate

# check if number of command line <> 2

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

# check if specified file name ends with .csv
# check if specified file exist

try:
    if sys.argv[1].endswith(".csv"):
        # open file and make an object
        with open(sys.argv[1], "r") as file:
            reader = csv.reader(file)
        # first row or header
            counter = 0
            for row in reader:
                if counter == 0:
                    break
            header = row

        # data rows, rows after header
            counter = 1
            list = []
            for n_row in reader:
                if counter >= 1:
                    list.append(n_row)
                else:
                    counter = counter + 1

        print(tabulate(list, header, tablefmt="grid"))

    else:
        sys.exit("Not a CSV file")
except FileNotFoundError:
    sys.exit("File does no exist")



