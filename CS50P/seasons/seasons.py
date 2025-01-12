from datetime import date
from inflect import engine
import sys

def main():
    birthday = input("Date of Birth: ")
    print(duration_in_words(birthday))

def duration_in_words(b):
    try:
        byear, bmonth, bday = map(int, b.split("-"))
        past_date = date(byear,bmonth,bday)


        today = date.today()

        day_duration = today - past_date

        minute_duration = day_duration.days * 24 * 60

        p = engine()

        words = p.number_to_words(minute_duration, andword="")

        return words.capitalize() + " minutes"
    except ValueError:
        sys.exit(1)

if __name__ == "__main__":
    main()


