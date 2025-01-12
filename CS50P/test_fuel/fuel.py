def main():
    fraction = input("Fraction: ")
    fuel_percentage = convert(fraction)
    print(gauge(fuel_percentage))


def convert(fraction):
    while True:
        try:
            seperate = fraction.split("/")
            num = int(seperate[0])
            den = int(seperate[1])
            f = num/den
            if f <= 1:
                p = round(f * 100)
                return p
            else:
                fraction = input("Fraction: ")
                pass
        # you can have except lines right after each other
        except (ValueError,ZeroDivisionError):
            raise



def gauge(fuel_percentage):
    if 0 <= fuel_percentage <= 1:
        return "E"
    elif 99 <= fuel_percentage <= 100:
        return "F"
    else:
        return f"{fuel_percentage}%"



if __name__ == "__main__":
    main()














