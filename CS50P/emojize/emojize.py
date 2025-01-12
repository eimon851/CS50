# import module
import emoji

# prompt user

def main():
    word = input("Input: " )
    print("Output: " + emoj(word))

# check if emojize uses aliases
def emoj(em):
    return emoji.emojize(em, language='alias')

if __name__ == "__main__":
    main()



