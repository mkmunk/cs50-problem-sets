import csv
import sys
import tabulate


def main():
    try:
        if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        elif not sys.argv[1].endswith(".csv"):
            sys.exit("Not a CSV file")
        else:
            with open(sys.argv[1], "r") as f:
                contents = csv.DictReader(f)
                rows = list(contents)
                print(tabulate.tabulate(rows, headers="keys", tablefmt = "grid")) 
    except FileNotFoundError:
        sys.exit("File does not exist")
main()

