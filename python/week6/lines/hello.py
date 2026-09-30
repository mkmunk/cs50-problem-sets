
# Ask user for their name
name = input("What's your name? ").strip().title()

# Split user's name into first and last name
first, last = name.split(" ")

# Say hello to user
print(f"Hello, {first}")

# Ask user for their habit 

def main():
    name = input("What's your name? ")
    hello(name)

def hello(to):
    print("Hello,", to)

main()