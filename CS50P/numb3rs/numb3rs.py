# def main():
#     print(validate(input("IPv4 Address: ")))

# def validate(ip):
#     # split ip by comma
#     split_ip = ip.split(".")
#     # for loop to check if between 0-255
#     if len(split_ip) == 4:
#         counter = 0
#         for item in range(4):
#             try:
#                 # convert to int, and use range(256)
#                 if int(split_ip[item]) in range(256):
#                     counter = counter + 1
#                 else:
#                     return False
#             except ValueError:
#                 return False
#         if counter == 4:
#             return True
#         else:
#             return False
#     else:
#         return False


#     # check if counter is 4 has to be right
# if __name__ == "__main__":
#     main()

# Using R.e

import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    if matches := re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$",ip):
        for i in range(1,5):
                if int(matches.group(i)) not in range(256):
                    return False
                else:
                    continue
        return True
    else:
        return False

if __name__ == "__main__":
    main()


