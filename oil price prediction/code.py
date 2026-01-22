# yfinance → talks to the internet and fetches historical market data
# pandas → lets us treat data like a table (rows = days, columns = facts)

import yfinance as yf
import pandas as pd


# Fetch data  Download crude oil prices and USD to INR exchange rate
brent = yf.download("BZ=F", start="2010-01-01")
brent_close = brent['Close'] # Get only the 'Close' prices
usd_inr = yf.download("INR=X", start="2010-01-01")['Close'] # USD to INR exchange rate
# Align and clean
data = pd.concat([brent_close, usd_inr], axis=1) # Combine both datasets side by side
data.columns = ['Brent_Close', 'USD_INR'] # Rename columns for clarity
data.dropna(inplace=True) # Remove any rows with missing data
# India-relevant oil price
data['Oil_INR'] = data['Brent_Close'] * data['USD_INR'] # Calculate oil price in INR
# Lag feature
data['Oil_INR_Lag1'] = data['Oil_INR'].shift(1) # Previous day's price
data.dropna(inplace=True) # Remove rows with NaN values after shifting
# causwe-effect setup
X = data[['Oil_INR_Lag1']] # cause
y = data['Oil_INR'] # effect

# Train-test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, shuffle=False
)


# Train a simple model to learn the relationship y = mx + c
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)

# TEST THE MODEL — DID IT LEARN ANYTHING?
y_pred = model.predict(X_test)

# evaluate — MEASURE HOW WRONG IT IS
from sklearn.metrics import mean_absolute_error

mae = mean_absolute_error(y_test, y_pred)
print("MAE:", mae) #MAE = 250 ,On average, the model’s prediction was ₹250 per barrel away from reality.

# Visual check
 # Numbers can lie quietly. Plots cannot.
import matplotlib.pyplot as plt

plt.plot(y_test.values, label="Actual")
plt.plot(y_pred, label="Predicted")
plt.legend()
plt.title("Actual vs Predicted Indian Crude Oil Price")
plt.show()
