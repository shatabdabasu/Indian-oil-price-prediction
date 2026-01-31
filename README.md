# Indian Oil Price Prediction (Baseline Time-Series Model)

This project implements a baseline time-series regression model to estimate crude oil prices relevant to India (₹ per barrel) using global Brent crude prices and the USD–INR exchange rate.

The goal is to establish a simple and interpretable reference model that captures short-term price dependency.

---

## Objective

- Convert global Brent crude oil prices into Indian Rupees
- Model day-to-day oil price dependency using historical data
- Evaluate prediction accuracy using standard error metrics

---

## Data Sources

- **Brent Crude Futures (`BZ=F`)**
- **USD–INR Exchange Rate (`INR=X`)**

Data is sourced from Yahoo Finance using the `yfinance` library.

---

## Methodology

1. Download historical Brent crude and USD–INR data  
2. Convert oil prices to INR per barrel  
3. Create a lag feature using the previous day’s oil price  
4. Split data into training and testing sets without shuffling  
5. Train a Linear Regression model  
6. Evaluate performance using Mean Absolute Error (MAE)  
7. Visualize actual vs predicted prices

---

## Model Details

- **Algorithm:** Linear Regression  
- **Feature Used:** Previous day’s oil price (Lag-1)  
- **Target Variable:** Oil price in INR per barrel  

This model acts as a baseline for future time-series improvements.

---

## Evaluation

- **Metric:** Mean Absolute Error (MAE)  
- **Result:** MAE ≈ ₹200–250 per barrel  

### Interpretation

- The model captures overall price trends
- Accuracy decreases during sudden market shocks or high volatility
- Such limitations are expected for a simple linear baseline model

---

## Visualization

A time-series line plot is used to visually compare actual and predicted oil prices over time.

---

## Tech Stack

- **Language:** Python  
- **Libraries:**
  - `yfinance`
  - `pandas`
  - `scikit-learn`
  - `matplotlib`

---

## How to Run

```bash
pip install yfinance pandas scikit-learn matplotlib
python code.py
