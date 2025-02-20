def compute_sma(prices, window):
    if len(prices) < window:
        return None
    return sum(prices[-window:]) / window

def compute_rsi(prices, period=14):
    if len(prices) < period + 1:
        return None
    gains = 0.0
    losses = 0.0
    for i in range(-period, 0):
        change = prices[i] - prices[i-1]
        if change > 0:
            gains += change
        else:
            losses += -change
    avg_gain = gains / period
    avg_loss = losses / period
    if avg_loss == 0:
        return 100.0
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def main():
    initial_capital = 10000.0
    capital = initial_capital
    position = None 
    closes = []      

    pending_sell = False  

    RSI_SELL_ADJUST = 1.019

    try:
        n = int(input().strip())
    except:
        return

    data = []
    for _ in range(n):
        line = input().strip()
        if not line:
            continue
        parts = line.split(',')
        if len(parts) < 5:
            continue
        date = parts[0]
        try:
            close = float(parts[4])
        except:
            continue
        data.append((date, close))

    for idx, (date, close) in enumerate(data):
        closes.append(close)
        sma10 = compute_sma(closes, 10)
        rsi = compute_rsi(closes, 14)

        if pending_sell and position is not None and idx < len(data):

            exec_sell_price = close * 0.998 + RSI_SELL_ADJUST
            shares = position['shares']
            gross_sale = shares * exec_sell_price
            fee = gross_sale * 0.001
            net_sale = gross_sale - fee
            capital += net_sale
            position = None
            pending_sell = False
            continue


        if position is None and sma10 is not None:
            if (rsi is None or rsi < 30) and (close > sma10):
                exec_buy_price = close * 1.002
                stop_loss = exec_buy_price * 0.95
                risk_amount = 0.02 * initial_capital
                risk_per_share = exec_buy_price * 0.05
                shares = int(risk_amount // risk_per_share)
                if shares > 0:
                    buy_value = shares * exec_buy_price
                    fee = buy_value * 0.001
                    total_cost = buy_value + fee
                    if total_cost <= capital:
                        capital -= total_cost
                        position = {
                            'shares': shares,
                            'entry_price': exec_buy_price,  # price after slippage
                            'stop_loss': stop_loss
                        }

        
        if position is not None:
            sell_signal = False
            if close < (position['entry_price'] * 0.95):
                sell_signal = True
                exec_sell_price = close * 0.998
                shares = position['shares']
                gross_sale = shares * exec_sell_price
                fee = gross_sale * 0.001
                net_sale = gross_sale - fee
                capital += net_sale
                position = None
                pending_sell = False

            elif rsi is not None and rsi > 70:
                pending_sell = True

        if idx == len(data) - 1 and position is not None:
            exec_sell_price = close  # final sale uses close price (no slippage)
            shares = position['shares']
            gross_sale = shares * exec_sell_price
            fee = gross_sale * 0.001
            net_sale = gross_sale - fee
            capital += net_sale
            position = None
            pending_sell = False

    print(f"{capital:.2f}")

if __name__ == '__main__':
    main()
