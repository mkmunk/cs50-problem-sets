import requests
import sys


try:
    n = float(sys.argv[1])
except IndexError:
    sys.exit("Missing command-line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    text = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=72906fd711b0665d414ec7907b071e48321cf21bf9d9532da779d7e5814f66e4", )
    data = text.json()
    priceUsd = data["data"]["priceUsd"]
    price = n * float(priceUsd)

    print(f"${price:,.4f}")
except requests.RequestException:
    sys.exit()

