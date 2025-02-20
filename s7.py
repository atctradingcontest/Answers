import numpy as np

def compute_daily_returns(prices):

    return (prices[1:] - prices[:-1]) / prices[:-1]

def correlation(x, y):

    return np.corrcoef(x, y)[0, 1]

def greedy_selection(returns, mean_returns):

    selected = []
    sorted_indices = np.argsort(-mean_returns)
    for asset in sorted_indices:
        if not selected:
            selected.append(asset)
        else:
            include = True
            for s in selected:
                corr = correlation(returns[:, s], returns[:, asset])
                if abs(corr) >= 0.5:
                    include = False
                    break
            if include:
                selected.append(asset)
    return selected

def simulate_buy_and_hold(selected, prices, initial_capital=10000):

    if not selected:
        return 0, round(initial_capital, 2)
    
    initial_prices = prices[0, selected]
    final_prices = prices[-1, selected]
    
    num_assets = len(selected)
    capital_per_asset = initial_capital / num_assets
    shares = capital_per_asset / initial_prices
    final_value = (shares * final_prices).sum()
    
    return num_assets, round(final_value, 2)

def main():
    n = int(input().strip())
    price_rows = []
    
    for _ in range(n):
        row = input().strip().split(',')
        price_rows.append([float(x) for x in row[1:]])
    
    prices = np.array(price_rows)
    
    returns = compute_daily_returns(prices)
    mean_returns = returns.mean(axis=0)
    
    selected_assets = greedy_selection(returns, mean_returns)
    
    num_selected, final_value = simulate_buy_and_hold(selected_assets, prices)
    
    print(num_selected)
    print(final_value)

if __name__ == "__main__":
    main()