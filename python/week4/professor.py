import random


def main():
    correct = 0
    level = get_level()
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        for attempt in range(3):
            try:
                answer = int(input((f"{x} + {y} = ")))
            except ValueError:
                print("EEE")
                continue
            if answer == x + y:
                correct += 1
                break
            else:
                print("EEE")
        else:
            print(f"{x} + {y} = {x+y}")


    print(f"Score: {correct}")
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level != 1 and level !=2 and level !=3:
                raise ValueError()
            else:
                return level 
        except ValueError:
            continue
def generate_integer(level):
        if level == 1:
            return random.randint(0, 9)
        elif level == 2:
            return random.randint(10, 99)
        elif level == 3:
            return random.randint(100, 999)
        else:
            raise ValueError()
        
if __name__ == "__main__":
    main()