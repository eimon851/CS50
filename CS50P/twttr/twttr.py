text = input("Input: ")
vowels = ["A","E","I","O","U","a","e","i","o","u"]

for char in text: #Twitter
    if char in vowels: # 'e'
        text = text.replace(char, "")

print(text)
