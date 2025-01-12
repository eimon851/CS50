# defining class named Jar
class Jar:
    # constructor method - called when new instance is created
    def __init__(self, capacity=12):
        if capacity < 0: # if negative capacity is pass, VE
            raise ValueError
        else:
            self._capacity = capacity # sets capacity
            self.cookies = 0 # initialize # of cookie = 0

    # special method that returns a string version of the object
    def __str__(self):
        if 0 < self.cookies <= self.capacity:
            return "🍪" * self.cookies
        else:
            return ""
    # deposit is a method
    def deposit(self, n):
        self.cookies += n
        if self.cookies > self.capacity:
            raise ValueError

    def withdraw(self, n):
        self.cookies -= n
        if self.cookies < 0 :
            raise ValueError

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.cookies

# creating an instance of the class
jar = Jar()
jar.deposit(1)
jar.withdraw(1)
print(jar.size)






