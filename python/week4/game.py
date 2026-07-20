import random


while True:
    try:
        n = int(input("Level: "))
        number = random.randint(1, n)
        if n < 1:
            raise ValueError()
        while True:
            try:
                guess = int(input("Guess: "))
                if guess < 1:
                    raise ValueError()
                if number > guess:
                    print("Too small!")
                elif number < guess:
                    print("Too large!")
                else:
                    print("Just right!")
                    break
            except ValueError:
                continue
    except ValueError:
        continue
    break

