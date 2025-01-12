# import modules: sys, csv

import sys, csv

# check to see two command-line arguments

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

try:
    # check to see if its a csv file
    if sys.argv[1].endswith(".csv"):
    # open the both cmd arg
        with open(sys.argv[1], "r") as file, open(sys.argv[2], "w") as file2:
            reader = csv.DictReader(file)
            fieldnames=["first","last","house"]
            writer = csv.DictWriter(file2, fieldnames=fieldnames)
            writer.writeheader()
            # for loop to iterate over each line
            for row in reader:
                # split into first and last name, shave white space
                last, first = row['name'].split(',')
                first = first.lstrip()
                house = row["house"]

                # write and append to new empty csv

                writer.writerow({"first": first, "last": last, "house": house})

    else:
        sys.exit("Not a CSV file")

except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")







