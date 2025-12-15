from predict_yearly import predict_yearly
import matplotlib.pyplot as plt

result = predict_yearly(
    model_path='models/Ethereum.h5',
    scaler_path='scalers/Ethereum_scaler.save',
    data_path='data/cleaned_Ethereum.csv',
    days=365
)

result.to_csv('ethereum_yearly_prediction.csv', index=False)

plt.figure(figsize=(12, 6))
plt.plot(result['Date'], result['Predicted_Close'], label='Predicted Close Price', color='green')
plt.title('Ethereum Price Prediction - Next 1 Year')
plt.xlabel('Date')
plt.ylabel('Predicted Close Price (USD)')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
