# --- Ethereum ---

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
import joblib
model = load_model("Ethereum.h5")
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])
scaler = joblib.load("Ethereum_scaler.save")
df = pd.read_csv("cleaned_Ethereum.csv")
data = df['Close'].values.reshape(-1, 1)
data_scaled = scaler.transform(data)
last_60_days = data_scaled[-60:].reshape(1, 60, 1)

preds = []
seq = last_60_days.copy()
for _ in range(30):
    pred = model.predict(seq)[0][0]
    preds.append(pred)
    seq = np.append(seq[:, 1:, :], [[[pred]]], axis=1)

predicted_prices = scaler.inverse_transform(np.array(preds).reshape(-1, 1))

plt.figure(figsize=(10, 4))
plt.plot(predicted_prices, label='Ethereum Next 30 Days', color='purple')
plt.title("Ethereum Price Prediction")
plt.xlabel("Days")
plt.ylabel("Price (USD)")
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()
