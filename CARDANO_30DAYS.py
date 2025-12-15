import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
import joblib
# --- Cardano ---
model = load_model("Cardano.h5")
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])
scaler = joblib.load("Cardano_scaler.save")
df = pd.read_csv("cleaned_Cradano.csv")
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
plt.plot(predicted_prices, label='Cardano Next 30 Days', color='green')
plt.title("Cardano Price Prediction")
plt.xlabel("Days")
plt.ylabel("Price (USD)")
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()
