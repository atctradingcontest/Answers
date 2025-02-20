n = int(input())

bullish = 0
bearish = 0
neutral = 0

for _ in range(n):
    data = input().split(',')
    open_price = float(data[1])
    close_price = float(data[4])

    if close_price > open_price:
        bullish += 1
    elif close_price < open_price:
        bearish += 1
    else:
        neutral += 1

print(bullish)
print(bearish)
print(neutral)
