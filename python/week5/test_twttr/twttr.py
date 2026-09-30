def main():
    name = input().strip()
    print(shorten(name))

def shorten(word):
    result = ""
    for letter in word:
        if letter not in "aeiouAEIOU":
            result += letter
    return result

if __name__ == "__main__":
    main()