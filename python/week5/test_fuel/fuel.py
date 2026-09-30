def main():
    while True:
        try:
            gas = input()
            gas_percentage = convert(gas)
            final_percentage = gauge(gas_percentage)
            print(final_percentage)
            break
        except(ValueError, ZeroDivisionError):
            print("one more time")


def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)
    if y == 0:
        raise ZeroDivisionError()
    elif x > y or y < 0 or x< 0:
        raise ValueError()
    z = x / y * 100
    return round(z)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()