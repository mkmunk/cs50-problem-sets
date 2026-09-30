import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"
    match = re.search(pattern, ip)
    if not match:
        return False

    one, two, three, four = ip.split(".")
    if one[0] == "0" and len(one) > 1:
        return False
    elif two[0] == "0" and len(two) > 1:
        return False
    elif three[0] == "0" and len(three) > 1:
        return False
    elif four[0] == "0" and len(four) > 1:
        return False
    one, two, three, four = map(int, [one, two, three, four])
    if one > 255 or two > 255 or three > 255 or four > 255:
        return False
    return True  

if __name__ == "__main__":
    main()