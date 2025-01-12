# name = input("What's your name? ")

# # file = open("names.txt", "a")
# # file.write(f"{name}\n")
# # file.close()

# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")

names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")
