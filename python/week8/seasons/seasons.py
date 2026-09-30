from datetime import date
import sys
import inflect

def main():
    before_day = calculate_minutes(input("Day of Birth: "))
    print(before_day)
    
def calculate_minutes(before_day):
    try:
        before_day = date.fromisoformat(before_day)
        today = date.today()
        days = today - before_day
        days = days.days
        minutes = days * 60 * 24
        p = inflect.engine()
        words = p.number_to_words(minutes, andword="").capitalize()
        return f"{words} minutes"
    except ValueError:
        sys.exit("Invalid date")    

if __name__ == "__main__":
    main()