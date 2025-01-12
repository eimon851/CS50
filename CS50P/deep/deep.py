phrase = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()

if phrase == "42":
    print("Yes")
elif phrase == "forty-two":
    print("Yes")
elif phrase == "forty two":
    print("Yes")
else:
    print("No")

