import re
import sys

def main():
    print(convert(input("Hours: ")))


def convert(s):
    # Define the function convert that takes a string as input
    # Check if the input string matches the expected formats (you can use regular expressions for this). If not, raise a ValueError.

    matches = re.search(r'(\d{1,2}):?(\d{1,2})? (AM|PM) to (\d{1,2}):?(\d{1,2})? (AM|PM)',s)

    if not matches:
        raise ValueError

    # Split the input string into hours, minutes, and AM/PM parts.

    h1, h2 = int(matches.group(1)), int(matches.group(4))

    m1, m2 = matches.group(2), matches.group(5)
    if m1 is None:
        m1 = 0
    else:
        m1 = int(matches.group(2))

    if m2 is None:
        m2 = 0
    else:
        m2 = int(matches.group(5))

    t1, t2 = matches.group(3), matches.group(6)

    # Boundary Testing

    if not (1 <= h1 <= 12) or not (0 <= m1 < 60):
        raise ValueError
    if not (1 <= h2 <= 12) or not (0 <= m2 < 60):
        raise ValueError

    # If the time is in PM, add 12 to the hours (unless the hour is 12).

    if t1 == 'PM' and h1 != 12:
        h1 = h1 + 12
    elif t2 == 'PM' and h2 != 12:
        h2 = h2 + 12


    # If the time is in AM and the hour is 12, change the hour to 0.
    if t1 == 'AM' and h1 == 12:
        h1 = 0
    elif t2 == 'AM' and h2 == 12:
        h2 = 0


    # Return the time in 24-hour format.

    return f'{h1:02}:{m1:02} to {h2:02}:{m2:02}'

if __name__ == "__main__":
    main()

# 12 AM to 12 PM
# 12:00 AM to 12:00 PM
