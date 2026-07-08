months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


while True:
    try:
        n = input("Date: ").strip().capitalize()
        if "/" in n:
            x, y, z = n.split("/")
            x = int(x)
            y = int(y)
            if x < 1 or x > 12 or y < 1 or y > 31 :
                raise ValueError()
            print(f"{z}-{x:02}-{y:02}")
            break
        else:
            if "," not in n:
                raise ValueError()
            a, b, c = n.replace(",", "").split(" ")
            if a in months:
                a = int(months.index(a) + 1)
            else:
                raise ValueError()
            b = int(b)
            if b < 1 or b > 31 :
                raise ValueError()
            print(f"{c}-{a:02}-{b:02}")
            break
    except ValueError:
        pass
