# Stock Portfolio Tracker

# Fixed stock prices
prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140
}

total = 0

print("Simple Stock Portfolio Tracker")
print("Available stocks: AAPL, TSLA, GOOG")
print("Type 'done' to finish")

while True:
    stock = input("Enter stock name: ").upper()

    if stock == "DONE":
        break

    if stock in prices:
        qty = int(input("Enter quantity: "))
        value = prices[stock] * qty
        total += value
        print("Added value:", value)
    else:
        print("Stock not found")

print("Total Investment:", total)

# Optional save to file
save = input("Save result to file? (yes/no): ").lower()

if save == "yes":
    file = open("portfolio.txt", "w")
    file.write("Total Investment: " + str(total))
    file.close()
    print("Saved in portfolio.txt")
