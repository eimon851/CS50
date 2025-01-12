'''print("meow")
print("meow")
print("meow")

i = 3
while i != 0:
    print("meow")
    i = i - 1'''

# while loop

'''i = 0
while i < 3:
    print("meow")
    i = i + 1

# for loop iterates through a list of items

for i in [0,1,2]:
    print("meow")

for i in range(3):
    print("meow")

for _ in range(3):
    print("meow")'''

# print("meow\n" * 3, end="")

'''while True:
    n = int(input("What's n? "))
    if n < 0:
        continue
    else:
        break'''

# In Python, the scope of a
# variable is the region of the code
# where it can be accessed.
'''while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")'''

'''def main():
    meow(get_number())

def get_number():
    while True:
        n = int(input("What is n? "))
        if n > 1:
            return n


def meow(n):
    for _ in range(n):
        print("meow")

main()
'''

'''students = ["Hermoine", "Harry", "Ron"]

for i in range(len(students)):
    print(i+1,students[i])'''

'''students = {
    "Hermoine": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}
for student in students:
    print(student, students[student], sep= ", ")'''

'''def main():
    print_square(3)


def print_square(size):

    # For each row in square
    for i in range(size):

        # For each brick in row
        for j in range(size):

            #  Print brick
            print("#", end="")

        # Print blank line
        print()


main()
'''

def main():
    print_square(3)


def print_square(size):
    for i in range(size):
        print_row(size)


def print_row(width):
    print("#" * width)


main()
