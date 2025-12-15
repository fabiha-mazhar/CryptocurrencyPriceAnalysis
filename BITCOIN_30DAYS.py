import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
import joblib

# === Load saved model and scaler ===
model = load_model("models/Bitcoin.h5")
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])  # Add this to remove warning

scaler = joblib.load("scalers/Bitcoin_scaler.save")

# === Load full dataset ===
df = pd.read_csv("data/cleaned_Bitcoin.csv")
data = df['Close'].values.reshape(-1, 1)

# === Scale and prepare last 60 days for prediction ===
data_scaled = scaler.transform(data)
last_60_days = data_scaled[-60:].reshape(1, 60, 1)

# === Predict 30 future days one-by-one ===
future_preds = []
input_seq = last_60_days.copy()

for _ in range(30):
    pred = model.predict(input_seq)[0][0]
    future_preds.append(pred)
    
    # Update input sequence by appending the new prediction and removing the oldest
    input_seq = np.append(input_seq[:, 1:, :], [[[pred]]], axis=1)

# === Inverse transform predictions ===
predicted_prices = scaler.inverse_transform(np.array(future_preds).reshape(-1, 1))

# === Plot results ===
plt.figure(figsize=(10, 4))
plt.plot(predicted_prices, label='Next 30 Days Prediction')
plt.title("Bitcoin Price Prediction (Next 30 Days)")
plt.xlabel("Days")
plt.ylabel("Price")
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()

# === Optional: print values ===
print("Bitcoin Next 30 Days Prediction:")
print(predicted_prices.flatten())
