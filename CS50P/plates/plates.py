
def main():
    plate = input("Plate: ") # HELLO
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
   if len(s) <= 2 or len(s) > 6:
       return False
   if not s[:2].isalpha():
       return False

   first_digit_found = False
   for i in s[2:]:
       if i.isdigit() and first_digit_found == False:
           if i == "0":
               return False
           else:
               first_digit_found = True
       if first_digit_found == True and not i.isdigit():
           if not i.isdigit():
            return False

   for letter in s:
       if not letter.isalnum():
           return False

   return True


main()
