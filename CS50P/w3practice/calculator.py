class Calculator:
    def add(self,a,b):
        return a + b
    def subtract(self,a,b):
        return a - b
    def multiply(self,a,b):
        return a * b
    def divide(self,a,b):
        if b == 0:
            return "Cannot divide by zero"
        else:
            return a + b

add1 = Calculator()
print(add1.add(a=5,b=5))
