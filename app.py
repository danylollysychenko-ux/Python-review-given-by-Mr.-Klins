import json
from tabulate import tabulate

headers = ["Name", "Price", "Make", "Profit"]
data_collected = []
with open("products.json", "r") as f:
    data = json.load(f)

for i in range(len(data["products"])):
    product = data["products"][i]["item"]
    price = data["products"][i]["price"]
    make = data["products"][i]["make"]
    profit = price-make
    print(profit)
    data_collected.append([product, price, make, profit])

print(tabulate(data_collected, headers=headers, floatfmt=".2f"))