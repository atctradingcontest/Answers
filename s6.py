def compute_rsi(prices):
    if len(prices) < 2:
        return None
    gain = 0.0
    loss = 0.0
    for i in range(1, len(prices)):
        change = prices[i] - prices[i-1]
        if change > 0:
            gain += change
        else:
            loss += abs(change)
    if gain + loss == 0:
        return 50  
    return 100 * gain / (gain + loss)

n = int(input().strip())

dates = []
opens = []
highs = []
lows = []
closes = []

for _ in range(n):
    line = input().strip()
    date, open_, high_, low_, close_ = line.split(',')
    dates.append(date)
    opens.append(float(open_))
    highs.append(float(high_))
    lows.append(float(low_))
    closes.append(float(close_))

initial_capital = 10000.0
portfolio = initial_capital  # موجودی نقدی
shares = 0.0                # تعداد سهم‌های خریداری‌شده
buy_price = None            # قیمت خرید (برای استاپ‌لاس)

for i in range(n):
    current_close = closes[i]
    
    if i >= 19:
        sma = sum(closes[i-19:i+1]) / 20
        
        rsi = compute_rsi(closes[:i])
        

        if shares == 0:
            if rsi is not None and rsi < 30 and current_close > sma:
                shares = portfolio / current_close
                buy_price = current_close
                portfolio = 0.0

        else:

            if (rsi > 70 and current_close < sma) or (current_close < 0.95 * buy_price):
                portfolio = shares * current_close
                shares = 0.0
                buy_price = None

if shares > 0:
    portfolio = shares * closes[-1]
    shares = 0.0

print(f"{portfolio:.2f}")
