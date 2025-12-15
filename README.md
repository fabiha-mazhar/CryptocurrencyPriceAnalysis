# Cryptocurrency Price Analysis and Prediction

This project, developed for the Introduction to Data Science (IDS) Lab, focuses on analyzing and forecasting the volatile price movements of major cryptocurrencies.

## Project Overview

The core objective is to predict future cryptocurrency prices by leveraging historical data and advanced machine learning techniques, particularly for Bitcoin, Ethereum, Cardano, and Dogecoin.

| Feature | Description |
| :--- | :--- |
| **Primary Goal** | Predict future **Bitcoin** prices. |
| **Cryptocurrencies** | Bitcoin, Ethereum, Cardano, Dogecoin. |
| **Data Scope** | Historical daily price data from **2015 to 2021**. |
| **Key Model** | **Long Short-Term Memory (LSTM)** Neural Network. |
| **Output** | 30-day future price forecasts and visual analytical tools. |

## Methodology Highlights

The project follows a structured data science workflow, from collection to evaluation.

### 1. Data Processing
* **Source:** Kaggle dataset containing price and volume data (Open, High, Low, Close, Volume).
* **Preprocessing:** Included removing duplicates, handling missing values, and chronological sorting.
* **Normalization:** **Min-Max scaling** was applied to standardize numeric price features between 0 and 1, crucial for LSTM stability.
* **Data Splitting:** Data was split chronologically into **80% training** and **20% testing** sets.

### 2. LSTM Model Architecture

| Component | Description |
| :--- | :--- |
| **Layers** | 2 LSTM layers. |
| **Output Layer** | Single dense neuron for predicting next-day closing price. |
| **Loss Function** | Mean Squared Error (MSE). |
| **Optimizer** | Adam optimizer. |
| **Overfitting Prevention**| Dropout (20%) and Early Stopping. |

### 3. Evaluation and Forecasting
* **Metrics:** Measured performance using **Root Mean Squared Error (RMSE)** and **Mean Squared Error (MSE)** on the test data.
* **Result:** The low RMSE (e.g., Test RMSE $\approx 0.055$) indicates the model accurately captures the general closing price trend.
* **Forecast:** Predictions generated for the short-term (next 7-30 days) are designed to serve as trend indicators.

## Frontend Interface

The project includes a user-friendly GUI for selecting a cryptocurrency and viewing the predictions, analysis, and risk assessment.

---
***Disclaimer:*** *The predictions should be used as trend indicators and not as exact financial guidance due to the inherent volatility of the cryptocurrency market.*
