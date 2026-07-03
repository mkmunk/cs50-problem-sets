name = input("Input: ")
for _ in name:
    if _ == "a" or _ == "e" or _ == "i" or _ == "o" or _ == "u":
        print("", end="")
    elif _ == "A" or _ == "E" or _ == "I" or _ == "O" or _ == "U":
        print("", end="")
    else:
        print( _ , end="")


""" 
利用for c in s:
        print(c , end="")
進行省略文字
舉例：
1. Twitter -> Twttr
2. What's your name -> Wht's yr nm?
3. CS50 -> CS50

$ python3 twttr.py
Iutput:
Ontput:



"""