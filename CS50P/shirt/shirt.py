# GOAL: overlay the shirt onto the muppet
# additional: may need to resize the shirt to best fit muppets

# import modules: sys, image,

import sys
import os
from PIL import Image,ImageOps


# conditions: 2 command line, corrent ending,

extensions = [".jpg", ".jpeg", ".png"]
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few command-lin arguments")

path1 = sys.argv[1]
path2 = sys.argv[2]

root1,ext1 = os.path.splitext(path1)
root2,ext2 = os.path.splitext(path2)

if ext1 not in extensions:
    sys.exit("Invalid Input")
elif ext2 not in extensions:
    sys.exit("Invalid Output")
elif ext1 != ext2:
    sys.exit("Input and output have different extensions")

if not os.path.isfile(sys.argv[1]):
    sys.exit("Input does not exist")

try:

    # open input to read

    before1 = Image.open(sys.argv[1])
    shirt = Image.open("shirt.png")

    # find the dimension of before 1

    width,height = shirt.size

    # resize the shirt image to muppet

    muppet = ImageOps.fit(before1,(width,height))

    # paste shirt on muppet

    muppet.paste(shirt,shirt)
    # save new modified before1 to after1

    muppet.save(sys.argv[2])


except FileNotFoundError:
    sys.exit("File not Found")



# open shirt as input, open muppet as output

# resize and crop input

# overlay the shirt

# save result



