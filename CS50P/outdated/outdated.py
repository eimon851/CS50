list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


 # the :02 formatting works on int not string


while True:
    date = input("Date: ")
    try:
        if "/" in date:
            month,day,year = date.split("/")
            month = int(month)
            day = int(day)
            year = int(year)
            if month <= 12 and day <= 31:
                year_mm_dd = f"{year}-{month:02}-{day:02}"
                print(year_mm_dd)
                break
        elif " " and "," in date:
            new_date = date.replace(",","")
            month, day, year = new_date.split(" ")
            month = int(list.index(month)+1)
            day = int(day)
            year = int(year)
            if month <= 12 and day <= 31:
                year_mm_dd = f"{year}-{month:02}-{day:02}"
                print(year_mm_dd)
                break
        else:
            raise ValueError
    except ValueError:
        pass



