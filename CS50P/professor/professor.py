import random


def main():
    level = get_level()
    correct = 0
    # randomly generate 10 math problems
    i = 10
    while i > 0:
        x = generate_integer(level)
        y = generate_integer(level)
        z = x + y
        # prompt user to solve each problem
        j = 3
        while j > 0:
            w = int(input(f"{x} + {y} = "))
            if w == z:
                correct = correct + 1
                break
            else:
                print("EEE")
                j = j - 1
        if j == 0:
            print(f"{x} + {y} = {z}")
        i = i - 1
    print(f"Score: {correct}")


def get_level():
    # Loop forever
    # Get user input [1-3]
    while True:
        try:
            level = int(input("Level: "))
            if level in range(1,4):
                return level
        except ValueError:
            pass

def generate_integer(level):
    # Based on lvl, generate integers
    # randrange(0,101) - gives 0-100
    if level == 1:
        return random.randrange(0,10)
    elif level == 2:
        return random.randrange(10,100)
    else:
        return random.randrange(100,1000)


if __name__ == "__main__":
    main()
