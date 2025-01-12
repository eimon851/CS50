camelCase = input("camelCase: ")
print("snake_name: ", end="")
for char in camelCase:
    if char.isupper() == False:
        print(char, end="")
    else:
        print("_" + char.lower(), end="")
print()

'''def main():
    camelCase = input("camelCase: ")
    print("snake_case: " + convert_camel_case(camelCase))

def convert_camel_case(camelCase):
    result = ""
    for char in camelCase:
        if char.isupper() == False:
            result += char
        else:
            result += "_" + char.lower()
    return result

main()'''

