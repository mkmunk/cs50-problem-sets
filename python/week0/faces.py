def convert():
    faces = input("").replace(":)" , "🙂").replace(":(" , "🙁").replace("XD" , "😆")
    return faces

def main():
    print(convert())

main()                                                 