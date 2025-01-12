import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")


try:
    if sys.argv[1].endswith(".csv"):
        with open(sys.argv[1], "r") as file:
            reader = csv.reader(file) # reader function
            #csv.DictReader(file) makes row be dictionary
            counter = 0
            for row in reader:
                if counter == 0:
                    break
            header = row
            counter = 1
            list = []
            for n_row in reader:
                if counter >= 1:
                    list.append(n_row)
                else:
                    counter = counter + 1

        # basically append from the .txt into a new table
        # then slice the table from table[1:] and tabulate that

        print(tabulate(list, header, tablefmt="grid"))

    else:
        sys.exit("Not a CSV file")
except FileNotFoundError:
    sys.exit("File does no exist")



