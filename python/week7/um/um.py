import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    pattern = r"\bum\b"
    match = re.findall(pattern, s, re.IGNORECASE)
    number = len(match)

    return number

if __name__ == "__main__":
    main()
