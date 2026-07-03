def main():
    number = input("Expression: ").split(" ")
    x, y, z = number
    x = int(x)
    z = int(z)

    if y == "+":
        print(f"{x + z:.1f}")
    elif y == "-":
        print(f"{x - z:.1f}")
    elif y == "*":
        print(f"{x * z:.1f}")
    else:
        print(f"{x / z:.1f}")

main()

"""def symbol(y):
    if y == "+":
        return x + z
    elif y == "-":
        return "-"
    elif y == "*":
        return "*"
    else:
        return "/"

"""