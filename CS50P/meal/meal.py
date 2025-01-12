def main():
    clock = input("What time is it? " )
    xy = convert(clock)

    if 7.00 <= xy <= 8.00:
        print("breakfast time")
    elif 12.00 <= xy <= 13.00:
        print("lunch time")
    elif 18.00 <= xy <= 19.00:
        print("dinner time")
    else:
        print()


def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes) / 60
    return float(hours + minutes)


if __name__ == "__main__":
    main()


















