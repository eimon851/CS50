import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):

# Initialize a count
    count = 0

# Find all um throught text
    matches = re.findall(r'\bum\b', s, re.IGNORECASE)

# find the len of the list

    length = len(matches)

# return length

    return length

if __name__ == "__main__":
    main()
