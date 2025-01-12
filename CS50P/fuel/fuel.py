# .split(" ") returns a list with two strings
    # you can handle exception right after the integers are identified
while True:
    # use while loop to re-prompt user
    # if the input function is out the loop, user only inputs once
    fraction = input("Fraction: ").split("/")
    try:
        num = int(fraction[0])
        den = int(fraction[1])
        fuel_percentage = round(num/den * 100)
        if fuel_percentage > 100:
            continue
    # you can have except lines right after each other
    except ValueError:
        pass
    except ZeroDivisionError:
        pass
    else:
         break

if 0 <= fuel_percentage <= 1:
    print("E")
# elif statement allows you to check multiple expression for true
# and executes a block of code as soon as one of he condision is true
elif 99 <= fuel_percentage <= 100:
    print("F")
else:
    print(f"{fuel_percentage}%")







