def main():
    answer = input("Greeting: ").lower().strip()
    print(value(answer))

def value(greeting):
    if greeting.startswith("hello"):
        return int(0)
    elif greeting.startswith("h"):
        return int(20)
    else:
        return int(100)

if __name__ == "__main__":
    main()
