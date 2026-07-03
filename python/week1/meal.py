def main():
    time = input("What time is it? ")
    result = convert(time)
    if 7 <= result <= 8:
        print("breakfast time")
    elif 12 <= result <= 13:
        print("lunch time")
    elif 18 <= result <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    time = int(hours) + float(minutes) / 60
    return time

if __name__ == "__main__":
    main()