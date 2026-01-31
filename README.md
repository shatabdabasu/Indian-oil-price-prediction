# Indian-oil-price-prediction
This project builds a baseline time-series model to estimate crude oil prices relevant to India using Brent crude prices and USD–INR exchange rates.

Oil Price Prediction (India-Relevant)
This project builds a baseline time-series model to estimate crude oil prices relevant to India using Brent crude prices and USD–INR exchange rates.

Approach
Fetch historical Brent crude and USD–INR data using yfinance
Convert oil prices to INR per barrel
Create a lag-based feature to model time dependence
Train a baseline Linear Regression model
Evaluate using Mean Absolute Error (MAE) and visual comparison
Result
MAE ≈ ₹112 per barrel
Model captures trend but fails during sudden market shocks (expected for a baseline)
How to Run
python code.py
