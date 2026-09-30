import sys


def main():
    try:
        if len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        elif len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        elif not sys.argv[1].endswith(".py"):
            sys.exit("Not a Python file")
        else:
            with open(sys.argv[1], "r") as f:
                contents = f.readlines()
                line = 0
                for row in contents:
                    if row.lstrip().startswith("#"):
                        line += 0
                    elif row.isspace():
                        line += 0
                    else:
                        line += 1
            print(line)
    except FileNotFoundError:
        sys.exit("File does not exist")
main()     