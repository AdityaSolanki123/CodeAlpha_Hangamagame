# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 135
}

portfolio = {}
total_investment = 0

print("===== Stock Portfolio Tracker =====")

n = int(input("Enter the number of stocks you want to add: "))

for i in range(n):
    stock = input("\nEnter Stock Symbol (AAPL, TSLA, GOOGL, MSFT, AMZN): ").upper()

    if stock in stock_prices:
        quantity = int(input("Enter Quantity: "))
        portfolio[stock] = quantity
    else:
        print("Stock not available!")

print("\n===== Portfolio Summary =====")

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity
    total_investment += investment

    print(f"{stock} : {quantity} shares × ${price} = ${investment}")

print("\nTotal Investment Value = $", total_investment)

# Save to file
with open("portfolio_summary.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    file.write("=========================\n")

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        investment = price * quantity
        file.write(f"{stock} : {quantity} × ${price} = ${investment}\n")

    file.write(f"\nTotal Investment = ${total_investment}")

print("\nPortfolio saved successfully in portfolio_summary.txt")