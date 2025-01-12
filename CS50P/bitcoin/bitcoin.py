import sys
import requests
import json

# Conditions
# if arg = 1, missing
# if arg = 2 but index 1 != number, not number
# If arg can't be converted to float, sys.exit

if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")
try:
    float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")


# Query the API

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data = response.json()

    bitcoin_value = float(data["bpi"]["USD"]["rate"].replace(",",""))
    current_cost = bitcoin_value * float(sys.argv[1])
    print(f"${current_cost:,.4f}")

except requests.RequestException:
    pass




