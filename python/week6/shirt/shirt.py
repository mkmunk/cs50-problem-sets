import sys
import os
from PIL import Image, ImageOps


def main():
    try:
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")

        input_name, input_ext = os.path.splitext(sys.argv[1])
        input_ext = input_ext.lower()

        output_name, output_ext = os.path.splitext(sys.argv[2])
        output_ext = output_ext.lower()

        if input_ext not in (".jpg", ".jpeg", ".png"):
            sys.exit("Invalid input")
        elif output_ext not in (".jpg", ".jpeg", ".png"):
            sys.exit("Invalid input")
        elif not input_ext == output_ext:
            sys.exit("Input and output have different extensions")
        else:
            shirt_photo = Image.open("shirt.png")
            before_photo = Image.open(sys.argv[1])
            size = shirt_photo.size
            before_photo = ImageOps.fit(before_photo, size)
            before_photo.paste(shirt_photo, shirt_photo)
            before_photo.save(sys.argv[2])
            

    except FileNotFoundError:
        sys.exit("Input does not exist")


main()