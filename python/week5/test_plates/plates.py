def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    found_number = False
    for _ in s:
        if _.isdigit() and found_number is False and _ == "0":
            return False
        if _.isdigit():
            found_number = True
        if _.isalpha() and found_number:
            return False
    for _ in s:
        if not _.isdigit() and not _.isalpha():
            return False

    if s[0:2].isalpha() and 2 <= len(s) <= 6:
        return True
    else:
        return False  

if __name__ =="__main__":
    main()

