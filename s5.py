import sys
from collections import deque

def calculate_sma(prices, window):
    if len(prices) < window:
        return sum(prices) / len(prices)
    return sum(list(prices)[-window:]) / window

def main():
    input_data = sys.stdin.read().strip().splitlines()
    if not input_data or len(input_data) < 2:
        print("10000.00")
        return

    n = int(input_data[0].strip())
    
    if n < 1 or len(input_data) < n + 1:
        print("10000.00")
        return

    cash = 10000.0  
    shares = 0.0      
    close_prices = [] 

    sma5_queue = deque(maxlen=5)   
    sma20_queue = deque(maxlen=20) 

    previous_sma5 = None
    previous_sma20 = None

    for i in range(1, n + 1):  
        parts = input_data[i].split(',')
        if len(parts) != 5:
            continue  

        try:
            close_price = float(parts[4])  
        except ValueError:
            continue  

        close_prices.append(close_price)
        sma5_queue.append(close_price)
        sma20_queue.append(close_price)

        current_sma5 = calculate_sma(sma5_queue, 5)
        current_sma20 = calculate_sma(sma20_queue, 20)

        if previous_sma5 is not None and previous_sma20 is not None:
            if shares == 0 and previous_sma5 <= previous_sma20 and current_sma5 > current_sma20:
                shares = cash / close_price      
                cash = 0.0

            elif shares > 0 and previous_sma5 >= previous_sma20 and current_sma5 < current_sma20:
                cash = shares * close_price  
                shares = 0.0

        previous_sma5 = current_sma5
        previous_sma20 = current_sma20

    if shares > 0:
        cash = shares * close_prices[-1]

    print(f"{cash:.2f}")

if __name__ == "__main__":
    main()