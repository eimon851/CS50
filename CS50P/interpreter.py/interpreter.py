'''
expression = input(("Expressions: " ))
x, y, z = expression.split(" ")

if y == "+":
    print(float(int(x) + int(z)))
elif y == "-":
    print(float(int(x) - int(z)))
elif y == "*":
    print(float(int(x) * int(z)))
elif y == "/":
    print(float(int(x) / int(z)))
else:
    print(0) */

'''

def perform_operation(x, y, z):
    if y == "+":
        print(float(int(x) + int(z)))
    elif y == "-":
        print(float(int(x) - int(z)))
    elif y == "*":
        print(float(int(x) * int(z)))
    elif y == "/":
        print(float(int(x) / int(z)))

# define main function
def main():
    expression = input(("Expressions: " ))
    try:
        # split char into variables
        x, y, z = expression.split(" ")
        # call work function 
        perform_operation(x, y, z)
    except ValueError:
        print("Invalid input. Please enter in the format: number operator number.")

main()
