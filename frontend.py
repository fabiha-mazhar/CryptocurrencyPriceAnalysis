import tkinter as tk
from tkinter import ttk, messagebox
import random

class CryptoPredictionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Crypto Price Predictions")
        self.root.geometry("1200x800")
        self.root.configure(bg='#2D1B69')
        
        # Configure styles
        self.setup_styles()
        
        # Create main frame
        self.main_frame = tk.Frame(root, bg='#2D1B69')
        self.main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Create header
        self.create_header()
        
        # Create instructions section
        self.create_instructions()
        
        # Create crypto cards
        self.create_crypto_cards()
        
        # Create footer
        self.create_footer()
    
    def setup_styles(self):
        """Setup custom styles for ttk widgets"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure combobox style
        style.configure('Custom.TCombobox',
                       fieldbackground='white',
                       background='white',
                       borderwidth=1,
                       relief='solid')
    
    def create_header(self):
        """Create the header section"""
        header_frame = tk.Frame(self.main_frame, bg='#2D1B69')
        header_frame.pack(fill='x', pady=(0, 30))
        
        title_label = tk.Label(header_frame, 
                              text="Crypto Price Predictions",
                              font=('Arial', 32, 'bold'),
                              fg='white',
                              bg='#2D1B69')
        title_label.pack()
        
        subtitle_label = tk.Label(header_frame,
                                 text="Advanced AI-powered cryptocurrency market forecasting",
                                 font=('Arial', 14),
                                 fg='#B8B8B8',
                                 bg='#2D1B69')
        subtitle_label.pack(pady=(5, 0))
    
    def create_instructions(self):
        """Create the instructions section"""
        # Instructions container with rounded rectangle effect
        instructions_frame = tk.Frame(self.main_frame, bg='#3D2B79', relief='solid', bd=1)
        instructions_frame.pack(fill='x', pady=(0, 30), padx=50)
        
        # Instructions header
        header_frame = tk.Frame(instructions_frame, bg='#3D2B79')
        header_frame.pack(fill='x', padx=20, pady=(15, 10))
        
        instructions_title = tk.Label(header_frame,
                                     text="📈 Instructions",
                                     font=('Arial', 16, 'bold'),
                                     fg='white',
                                     bg='#3D2B79')
        instructions_title.pack(anchor='w')
        
        subtitle = tk.Label(header_frame,
                           text="Get started with our crypto prediction platform",
                           font=('Arial', 12),
                           fg='#B8B8B8',
                           bg='#3D2B79')
        subtitle.pack(anchor='w', pady=(5, 0))
        
        # Two column layout
        content_frame = tk.Frame(instructions_frame, bg='#3D2B79')
        content_frame.pack(fill='x', padx=20, pady=(10, 20))
        
        # Left column - How to Use
        left_frame = tk.Frame(content_frame, bg='#3D2B79')
        left_frame.pack(side='left', fill='both', expand=True, padx=(0, 20))
        
        how_to_label = tk.Label(left_frame,
                               text="How to Use:",
                               font=('Arial', 12, 'bold'),
                               fg='white',
                               bg='#3D2B79')
        how_to_label.pack(anchor='w')
        
        how_to_items = [
            "• Select a cryptocurrency from the buttons below",
            "• View AI-generated price predictions and analysis",
            "• Access historical data and trend analysis",
            "• Make informed trading decisions"
        ]
        
        for item in how_to_items:
            item_label = tk.Label(left_frame,
                                 text=item,
                                 font=('Arial', 10),
                                 fg='#B8B8B8',
                                 bg='#3D2B79',
                                 justify='left')
            item_label.pack(anchor='w', pady=2)
        
        # Right column - Features
        right_frame = tk.Frame(content_frame, bg='#3D2B79')
        right_frame.pack(side='right', fill='both', expand=True)
        
        features_label = tk.Label(right_frame,
                                 text="Features:",
                                 font=('Arial', 12, 'bold'),
                                 fg='white',
                                 bg='#3D2B79')
        features_label.pack(anchor='w')
        
        features_items = [
            "• Real-time market data integration",
            "• Machine learning price forecasts",
            "• Technical analysis indicators",
            "• Risk assessment metrics"
        ]
        
        for item in features_items:
            item_label = tk.Label(right_frame,
                                 text=item,
                                 font=('Arial', 10),
                                 fg='#B8B8B8',
                                 bg='#3D2B79',
                                 justify='left')
            item_label.pack(anchor='w', pady=2)
    
    def create_crypto_cards(self):
        """Create the cryptocurrency cards"""
        cards_frame = tk.Frame(self.main_frame, bg='#2D1B69')
        cards_frame.pack(fill='x', pady=(0, 30))
        
        # Crypto data
        cryptos = [
            {"name": "Bitcoin", "symbol": "₿", "color": "#FFB366", "button_color": "#FF6B35"},
            {"name": "Dogecoin", "symbol": "Ð", "color": "#FFE066", "button_color": "#FFD700"},
            {"name": "Ethereum", "symbol": "$", "color": "#66B3FF", "button_color": "#4A90E2"},
            {"name": "Cardano", "symbol": "📈", "color": "#66FFB3", "button_color": "#00C851"}
        ]
        
        for i, crypto in enumerate(cryptos):
            self.create_crypto_card(cards_frame, crypto, i)
    
    def create_crypto_card(self, parent, crypto_data, index):
        """Create individual crypto card"""
        # Card frame
        card_frame = tk.Frame(parent, bg=crypto_data["color"], relief='solid', bd=1)
        card_frame.pack(side='left', fill='both', expand=True, padx=10, pady=10)
        
        # Symbol
        symbol_label = tk.Label(card_frame,
                               text=crypto_data["symbol"],
                               font=('Arial', 40, 'bold'),
                               fg='white',
                               bg=crypto_data["color"])
        symbol_label.pack(pady=(30, 10))
        
        # Name
        name_label = tk.Label(card_frame,
                             text=crypto_data["name"],
                             font=('Arial', 16, 'bold'),
                             fg='white',
                             bg=crypto_data["color"])
        name_label.pack(pady=(0, 20))
        
        # Prediction button with dropdown
        button_frame = tk.Frame(card_frame, bg=crypto_data["color"])
        button_frame.pack(pady=(0, 30))
        
        # Create dropdown frame (initially hidden)
        dropdown_frame = tk.Frame(button_frame, bg='white', relief='solid', bd=1)
        
        # Main prediction button
        prediction_button = tk.Button(button_frame,
                                     text=f"Show {crypto_data['name']} Prediction ▼",
                                     font=('Arial', 10, 'bold'),
                                     fg='white',
                                     bg=crypto_data["button_color"],
                                     relief='flat',
                                     padx=20,
                                     pady=8,
                                     command=lambda name=crypto_data['name'], frame=dropdown_frame, btn=None: self.toggle_dropdown(name, frame, prediction_button))
        prediction_button.pack()
        
        # Dropdown options
        monthly_btn = tk.Button(dropdown_frame,
                           text="Monthly Prediction",
                           font=('Arial', 9),
                           fg='black',
                           bg='white',
                           relief='flat',
                           padx=15,
                           pady=5,
                           command=lambda: self.select_prediction(crypto_data['name'], 'Monthly'))
        monthly_btn.pack(fill='x')
        
        yearly_btn = tk.Button(dropdown_frame,
                          text="Yearly Prediction",
                          font=('Arial', 9),
                          fg='black',
                          bg='white',
                          relief='flat',
                          padx=15,
                          pady=5,
                          command=lambda: self.select_prediction(crypto_data['name'], 'Yearly'))
        yearly_btn.pack(fill='x')
        
        # Store reference to dropdown for this card
        setattr(self, f'dropdown_{index}', dropdown_frame)

    
    def toggle_dropdown(self, crypto_name, dropdown_frame, button):
        """Toggle dropdown menu visibility"""
        # Hide all other dropdowns first
        for i in range(4):  # We have 4 crypto cards
            if hasattr(self, f'dropdown_{i}'):
                other_dropdown = getattr(self, f'dropdown_{i}')
                if other_dropdown != dropdown_frame:
                    other_dropdown.pack_forget()
        
        # Toggle current dropdown
        if dropdown_frame.winfo_viewable():
            dropdown_frame.pack_forget()
            button.config(text=button.cget('text').replace(' ▲', ' ▼'))
        else:
            dropdown_frame.pack(pady=(2, 0))
            button.config(text=button.cget('text').replace(' ▼', ' ▲'))

    def hide_dropdown(self):
        """Hide any open dropdown menus"""
        for i in range(4):
            if hasattr(self, f'dropdown_{i}'):
                getattr(self, f'dropdown_{i}').pack_forget()

    def select_prediction(self, crypto, prediction_type):
        self.hide_dropdown()

        # 🔽 Add all your crypto model/scaler/data paths here
        paths = {
            "Bitcoin": {
                "model": "models/Bitcoin.h5",
                "scaler": "scalers/Bitcoin_scaler.save",
                "data": "data/cleaned_Bitcoin.csv"
            },
            "Ethereum": {
                "model": "models/Ethereum.h5",
                "scaler": "scalers/Ethereum_scaler.save",
                "data": "data/cleaned_Ethereum.csv"
            },
            "Dogecoin": {
                "model": "models/Dogecoin.h5",
                "scaler": "scalers/Dogecoin_scaler.save",
                "data": "data/cleaned_Dogecoin.csv"
            },
            "Cardano": {
                "model": "models/Cardano.h5",
                "scaler": "scalers/Cardano_scaler.save",
                "data": "data/cleaned_Cradano.csv"
            }
        }

        if crypto not in paths:
            messagebox.showerror("Missing Model", f"No model available for {crypto}.")
            return

        days = 30 if prediction_type == "Monthly" else 365

        # Call your prediction function
        try:
            self.predict_future_prices(
                model_path=paths[crypto]["model"],
                scaler_path=paths[crypto]["scaler"],
                data_path=paths[crypto]["data"],
                days_to_predict=days
            )
        except Exception as exc:
            messagebox.showerror("Prediction Failed", f"Could not run prediction for {crypto}: {exc}")



    def show_prediction_options(self, crypto_name):
        """This method is no longer used but kept for compatibility"""
        pass
    
    def get_prediction(self, crypto_name, timeframe, popup):
        """Generate and show prediction based on selection"""
        # No need to destroy popup since we're not using popups anymore
        if popup:
            popup.destroy()
        
        # Generate mock prediction data
        current_price = random.uniform(100, 50000)
        if timeframe == "Monthly":
            change_percent = random.uniform(-15, 25)
            predicted_price = current_price * (1 + change_percent/100)
            period = "30 days"
        else:  # Yearly
            change_percent = random.uniform(-30, 100)
            predicted_price = current_price * (1 + change_percent/100)
            period = "365 days"
        
        # Show prediction result
        result_message = f"""
{crypto_name} Price Prediction ({timeframe})

Current Price: ${current_price:,.2f}
Predicted Price ({period}): ${predicted_price:,.2f}
Expected Change: {change_percent:+.2f}%

Confidence Level: {random.randint(75, 95)}%
Risk Level: {"Low" if abs(change_percent) < 20 else "Medium" if abs(change_percent) < 40 else "High"}

*This is a simulated prediction for demonstration purposes
    """
    
        messagebox.showinfo(f"{crypto_name} Prediction", result_message)

    @staticmethod
    def predict_future_prices(model_path, scaler_path, data_path, days_to_predict):
        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt
        from tensorflow.keras.models import load_model
        import joblib

        # Load model and scaler
        model = load_model(model_path)
        scaler = joblib.load(scaler_path)

        # Load data
        df = pd.read_csv(data_path)
        data = df['Close'].values.reshape(-1, 1)

        # Scale data and get last 60 days
        data_scaled = scaler.transform(data)
        input_seq = data_scaled[-60:].reshape(1, 60, 1)

        # Predict future days
        future_preds = []
        for _ in range(days_to_predict):
            pred = model.predict(input_seq)[0][0]
            future_preds.append(pred)
            input_seq = np.append(input_seq[:, 1:, :], [[[pred]]], axis=1)

        # Inverse transform to actual prices
        predicted_prices = scaler.inverse_transform(np.array(future_preds).reshape(-1, 1))

        # Plot predictions
        plt.figure(figsize=(10, 4))
        plt.plot(predicted_prices, label=f"{days_to_predict}-Day Prediction")
        plt.title("Bitcoin Price Prediction")
        plt.xlabel("Days Ahead")
        plt.ylabel("Price (USD)")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

        return predicted_prices

    
    def create_footer(self):
        """Create the footer section"""
        footer_label = tk.Label(self.main_frame,
                               text="Powered by advanced AI algorithms and real-time market data",
                               font=('Arial', 10),
                               fg='#B8B8B8',
                               bg='#2D1B69')
        footer_label.pack(side='bottom', pady=20)

def main():
    root = tk.Tk()
    app = CryptoPredictionApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
