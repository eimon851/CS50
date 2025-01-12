def main():
    text = input("Input: ")
    print(shorten(text))


def shorten(word):
    vowels = ["A","E","I","O","U","a","e","i","o","u"]

    for char in word: #Twitter
        if char in vowels: # 'e'
            word = word.replace(char, "")

    return word


if __name__ == "__main__":
    main()


