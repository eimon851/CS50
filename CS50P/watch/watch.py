import re
import sys


def main():
    print(parse(input(f"HTML:\n")))


def parse(s):

    pattern = re.compile(r'src="https?://(?:www\.)?youtube\.com/embed/(\w+)"')
    matches = re.search(pattern, s)

    if matches:
        return f"\nhttps://youtu.be/{matches.group(1)}"
    else:
        return "None"

if __name__ == "__main__":
    main()


 # pattern = re.compile(r"https?(www\.)?youtube\.com/embed/(\w+)")
    # matches = re.findall(pattern, s)
