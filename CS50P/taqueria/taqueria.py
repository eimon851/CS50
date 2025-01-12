dict = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0
while True:
    # repetitive acts: try ... input
    try:
        item = input("Items: ").lower()
    except EOFError:
        print()
        break
    # dict has keys, so when used with for loop it iterates over keys
    for i in dict:
            if i.lower() == item:
                total += dict[i]
                print(f"Total: ${total:.2f}")
                # by adding break the for loop can go again after it find item
                break

