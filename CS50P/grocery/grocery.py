list = []
while True:
    try:
        item = input()
        list.append(item)
    except EOFError:
        print("\n")
        break


# should initiators be in or out the loop?
dict = {}
for i in list:
    # if statement: check a item was already iterated over
    if i not in dict:
    # ask my self what data types am i concatenating

    # dict doesnt have an append method.
    # add new key-value pair using dict[key] = value
        dict[i] = list.count(i)

# to sort a dict, you sorted()
for key in sorted(dict):
    print(dict[key], key.upper())
