def main():
    n = input("Greeting: ").lower().strip()
    print(answer(n))

def answer(n):
    if n.startswith("hello"):
        return f"$0"
    elif n.startswith("h"):
        return f"$20"
    else:
        return f"$100"


main()
