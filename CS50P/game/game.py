import random

while True:
    try:
        level = int(input("Input: "))
        if level > 0:
            break
    except:
        pass

random_number = random.randint(1,level)

while True:
    try:
        guess = int(input("Guess: "))
        if guess < random_number:
            print("Too small!")
        elif guess > random_number:
            print("Too large!")
        else:
            print("Just right!")
            break
    except:
        pass














# TO-DO LIST

# import random

# def main

# print(level)
# print(guess)
# if statements that compare if level <>= guess
# print()

# def function_name
#     while loop
#     try
#         user prompt = level
#         if statement int > -1
#         return number
#         else
#         go back to user prompt = level
#     except valuerror
#         pass or break?

# import random


# while True:
#     try:
#         level = int(input("Level: "))
#         if level > 0:
#             level = random.randint(1,level)
#             break
#     except ValueError:
#         pass

# while True:
#     try:
#         guess = int(input("Guess: "))
#         if guess > 0:
#             break
#     except ValueError:
#         pass

# if level > guess:
#     print("Too small!")
# elif level < guess:
#     print("Too large!")
# else:
#     print("Just right!")


# Get Level
