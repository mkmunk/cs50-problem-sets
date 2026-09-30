import csv
import sys


def main():
    try:
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")
        else:
            with open(sys.argv[1], "r") as before, open(sys.argv[2], "w") as after:
                reader = csv.DictReader(before)
                writer = csv.DictWriter(after, fieldnames=["first", "last", "house"])
                writer.writeheader()

                for row in reader:
                    name = row["name"]
                    last, first = name.split(", ")
                    writer.writerow(
                        {
                            "first": first,
                            "last": last,
                            "house": row["house"]
                        }
                    )
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
    
        
main()
