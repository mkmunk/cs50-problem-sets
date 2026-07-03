def main():
    n = input("File name: ").lower().strip()
    print (extensions(n))


def extensions(n):
    i = "image/"
    if n.endswith("gif"):
        return f"{i}gif"
    elif n.endswith("jpg"):
        return f"{i}jpeg"
    elif n.endswith("jpeg"):
        return f"{i}jpeg"
    elif n.endswith("png"):
        return f"{i}png"
    elif n.endswith("pdf"):
        return f"application/pdf"
    elif n.endswith("txt"):
        return f"text/plain"
    elif n.endswith("zip"):
        return f"application/zip"
    else:
        return f"application/octet-stream"

main()