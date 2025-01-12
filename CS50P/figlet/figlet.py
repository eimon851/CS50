import sys
import random
from pyfiglet import Figlet

# creating an instand of the Figlet class to borrow its
# properties

# if certain chck result in invalud usage, likely that will be in else statement

# if len(sys.argv) not in [1,3]:
#     #1 combine these two statements
#     print("Invalid usage")
#     sys.exit()
#     #1 sys.exit("Invalid usage")

# if sys.argv[2] not in fonts:
#     #1
#     print("Invalid usage")
#     sys.exit()

# if sys.argv[1] != '-f' and sys.argv[1] != '--font':
#     #1
#     print("Invalid usage")
#     sys.exit()

# words = input("Input: ")

# if len(sys.argv) == 1:
#     random_font = random.choice(fonts)
#     figlet.setFont(font=random_font)
#     print(figlet.renderText(words))
# elif len(sys.argv) == 3:
#     f = str(sys.argv[2])
#     figlet.setFont(font=f)
#     print(figlet.renderText(words))


figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    figlet.setFont(font=random.choice(fonts))
elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font') and sys.argv[2] in fonts:
    figlet.setFont(font=sys.argv[2])
else:
    sys.exit("Invalid usage")

text = input("Input: ")
print(figlet.renderText(text))


