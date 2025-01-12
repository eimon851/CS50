# while loop that keeps asking for name input
# until ctrl d which raises an EOF Errr
# print adieu ... n1,n2,3
# drop the names after each print?

import inflect

p = inflect.engine()
names = []

while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        break

thelist = p.join((names))

print(f"Adieu, adieu, to {thelist}")
