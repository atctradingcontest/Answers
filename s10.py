import sys
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv(file_path)

df['Date'] = pd.to_datetime(df['Date'])
df['Open'] = df['Open'].astype(float)
df['High'] = df['High'].astype(float)
df['Low'] = df['Low'].astype(float)
df['Close'] = df['Close'].astype(float)

df['SMA3'] = df['Close'].rolling(window=3).mean()
df['SMA5'] = df['Close'].rolling(window=5).mean()

delta = df['Close'].diff()
gain = (delta.where(delta > 0, 0)).rolling(window=3).mean()
loss = (-delta.where(delta < 0, 0)).rolling(window=3).mean()
rs = gain / loss
df['RSI'] = 100 - (100 / (1 + rs))

df = df.dropna()

X = df[['Open', 'High', 'Low', 'Close', 'SMA3', 'SMA5', 'RSI']]
y = df['Close'].shift(-1).dropna()
X = X.iloc[:-1]

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

last_row = X.iloc[-1].values.reshape(1, -1)
predicted_close = model.predict(last_row)

print(f"{predicted_close[0]:.2f}")

# print(299.20)
