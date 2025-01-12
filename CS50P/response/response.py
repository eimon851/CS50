import validators

# input a str asking for email

str = input("What's your email address? ")

# valid email using validators
if validators.email(str) == True:
    print("Valid")
else:
    print("Invalid")

# print Valid or Invalid



