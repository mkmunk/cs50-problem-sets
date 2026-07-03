def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    found_number = False
    for _ in s:
        if _.isdigit() and found_number is False and _ == "0":
            return False
        if _.isdigit():
            found_number = True
        if _.isalpha() and found_number:
            return False
    for _ in s:
        if not _.isdigit() and not _.isalpha():
            return False

    if s[0:2].isalpha() and 2 <= len(s) <= 6:
        return True
    else:
        return False  
          
main()

"""
“所有個人化車牌必須至少以兩個字母開頭。”
“…個性化車牌最多可包含 6 個字元（字母或數字），最少可包含 2 個字元。”
「車牌中間不能使用數字，數字必須放在末尾。例如，AAA222 是一個可以接受的個性化車牌；AAA22A 則不行。第一個數字不能是‘0’。”
“不允許使用句號、空格或任何標點符號。”
s = CS50[0:2]


如果遇到英文是對的
但遇到數字 且遇到數字0就會是錯的
"""
