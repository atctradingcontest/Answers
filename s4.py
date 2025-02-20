import sys

def calculate_pct_change(prev, curr):
    """Calculate percentage change between two numbers."""
    if prev is None:
        return "N/A"
    return round(((curr - prev) / prev) * 100, 2)

def calculate_sma(prices, index, window=5):
    """Calculate Simple Moving Average (SMA) for the last `window` elements."""
    if index < window - 1:
        return "N/A"
    return round(sum(prices[index - window + 1:index + 1]) / window, 2)

try:
    n = int(input().strip())
    if n <= 0:
        raise ValueError("Number of rows must be greater than 0.")
except ValueError:
    print("Invalid number of rows.")
    sys.exit(1)

data = []
close_prices = []

for _ in range(n):
    row = input().strip()
    values = row.split(',')
    if len(values) != 5:
        print("Invalid input format.")
        sys.exit(1)

    date, open_price, high, low, close = values

    try:
        open_price = float(open_price)
        high = float(high)
        low = float(low)
        close = float(close)
    except ValueError:
        print("Invalid numeric values in input.")
        sys.exit(1)

    data.append([date, open_price, high, low, close])
    close_prices.append(close)

prev_close = None

for i in range(n):
    date, open_price, high, low, close = data[i]

    daily_change = calculate_pct_change(prev_close, close)
    sma_5 = calculate_sma(close_prices, i, 5)

    print(f"{date},{open_price},{high},{low},{close},{sma_5},{daily_change}")

    prev_close = close  
