from datetime import date

class Person:
    def __init__(self,name,country,date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth

    def get_age(self):
        today = date.today()
        year, month, day = map(int, self.date_of_birth.split("-"))
        bday = date(year,month,day)
        age = today.year - bday.year
        if (today.month, today.day) < (bday.month, bday.day):
            age = age - 1
        return age


person1 = Person("Ben James", "France", "2000-12-22")
print(person1.get_age())
