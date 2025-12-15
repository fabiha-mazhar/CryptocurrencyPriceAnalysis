import numpy as np
import pandas as pd
from keras.models import load_model
import joblib
from datetime import timedelta

def predict_yearly(model_path, scaler_path, data_path, days=365):
    model = load_model(model_path)
    scaler = joblib.load(scaler_path)
    df = pd.read_csv(data_path)

    df['Date'] = pd.to_datetime(df['Date'])

    last_60 = df['Close'].values[-60:].reshape(-1, 1)
    last_60_scaled = scaler.transform(last_60)
    sequence = np.reshape(last_60_scaled, (1, 60, 1))

    predictions = []

    for _ in range(days):
        predicted_price = model.predict(sequence)[0][0]
        predictions.append(predicted_price)
        sequence = np.append(sequence[:, 1:, :], [[[predicted_price]]], axis=1)

    predicted_prices = scaler.inverse_transform(np.array(predictions).reshape(-1, 1)).flatten()
    last_date = df['Date'].iloc[-1]
    future_dates = [last_date + timedelta(days=i) for i in range(1, days + 1)]

    return pd.DataFrame({'Date': future_dates, 'Predicted_Close': predicted_prices})
