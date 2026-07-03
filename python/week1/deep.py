def main():
    number = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()
    if number == "42":
        return print("Yes")
    elif number == "forty-two":
        return print("Yes")
    elif number == "forty two":
        return print("Yes")
    else:
        return print("No")

main()