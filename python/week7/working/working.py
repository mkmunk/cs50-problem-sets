import re
import sys

def main():
    print(convert(input("Hours: ")))



def convert(s):
    pattern = r"(\d{1,2})(:\d{2})? (AM|PM) to (\d{1,2})(:\d{2})? (AM|PM)"
    match = re.search(pattern, s)
    if not match:
        raise ValueError

    hour_1 = match.group(1)
    minute_1 = match.group(2)
    period_1 = match.group(3)
    hour_2 = match.group(4)
    minute_2 = match.group(5)
    period_2 = match.group(6)

    new_hour_1, new_minute_1 = to_24_hour(hour_1, minute_1, period_1)
    new_hour_2, new_minute_2 = to_24_hour(hour_2, minute_2, period_2)

    return f"{new_hour_1:02}:{new_minute_1:02} to {new_hour_2:02}:{new_minute_2:02}"
    

def to_24_hour(hour, minute, period):
    hour = int(hour)
    if minute is None:
        minute = 0
    else:
        minute = minute[1:]
        minute = int(minute)
                
    if hour < 1 or hour > 12:
        raise ValueError
    elif minute > 59:
        raise ValueError

    if period == "AM":
        if hour == 12:
            hour = 0
        else:
            hour = hour

    elif period == "PM":
        if hour == 12:
            hour = hour
        else:
            hour += 12

    return hour, minute

    
if __name__ == "__main__":
    main()