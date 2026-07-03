amount = 50
while  amount >= 0:
    print("Amount Due:", amount)
    coin = int(input("Insert Coin: "))
    if coin == 25:
        if amount < 25:
            print("Change Owed:", coin - amount)
            break
        amount -= 25
        if amount == 0:
           print("Change Owed:", amount)
           break
    elif coin == 10:
        if amount < 10:
            print("Change Owed:", coin - amount)
            break
        amount -= 10
        if amount == 0:
           print("Change Owed:", amount)
           break
    elif coin == 5: 
        amount -= 5
        if amount == 0:
           print("Change Owed:", amount)
           break
        

# Change Owed: 0 

# 假設一台機器以 50 美分的價格出售可口可樂（可樂），並且只接受以下面額的硬幣：25 美分、10 美分和 5 美分。
# 在一個名為 `.ts` 的檔案中coke.py，實作一個程序，提示使用者一次投入一枚硬幣，並每次都告知使用者應得金額。
# 當用戶至少投入 50 美分後，輸出用戶應找零的美分數。假設使用者只能輸入整數，並忽略任何非指定面額的整數。

"""

--- Amount 預設數字為:50
--- 一開始直接顯示
    Amount Due: 50
    Insert Coin: 
--- 50如何重複只減去25、10、5這幾個數字

def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")

main()
"""