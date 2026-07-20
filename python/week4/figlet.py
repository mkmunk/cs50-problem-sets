from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

def main():
    if len(sys.argv) == 1:
        Fonts = figlet.getFonts()
        random_fonts = random.choice(Fonts)
        figlet.setFont(font=random_fonts)
        s = input("Input: ")
        print(f"Output: {figlet.renderText(s)}")
    elif len(sys.argv) == 3 and sys.argv[1] == "-f":
        Fonts = figlet.getFonts()
        if sys.argv[2] in Fonts:
            figlet.setFont(font=sys.argv[2])
            s = input("Input: ")
            print(f"Output: {figlet.renderText(s)}")
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")

main()  

