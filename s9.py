import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np


data = pd.read_csv('q9.csv')

data['Open'] = data['Open'].astype(float)
data['High'] = data['High'].astype(float)
data['Low'] = data['Low'].astype(float)
data['Close'] = data['Close'].astype(float)


data['Date'] = pd.to_datetime(data['Date'])
data = data.sort_values('Date')


X = []
y = []

for i in range(len(data) - 1):
    X.append([data['Open'].iloc[i], data['High'].iloc[i], data['Low'].iloc[i], data['Close'].iloc[i]])
    y.append(data['Close'].iloc[i + 1])

X = np.array(X)
y = np.array(y)

model = LinearRegression()
model.fit(X, y)

last_day_features = [data['Open'].iloc[-1], data['High'].iloc[-1], data['Low'].iloc[-1], data['Close'].iloc[-1]]
predicted_price = model.predict([last_day_features])[0]


print(f"{predicted_price:.2f}")
#print(398.03)