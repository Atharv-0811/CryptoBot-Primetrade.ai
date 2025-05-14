import customtkinter as ctk
from bot import BasicBot
import os

api_key = os.getenv("API_KEY", "test_api_key")
api_secret = os.getenv("API_SECRET", "test_api_secret")

bot = BasicBot(api_key, api_secret, testnet=True)

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Crypto Bot - Primetrade")
app.geometry("400x500")

symbol_entry = ctk.CTkEntry(app, placeholder_text="Symbol (e.g., BTCUSDT)")
symbol_entry.pack(pady=10)

side_var = ctk.StringVar(value="BUY")
side_menu = ctk.CTkOptionMenu(app, values=["BUY", "SELL"], variable=side_var)
side_menu.pack(pady=10)

type_var = ctk.StringVar(value="MARKET")
type_menu = ctk.CTkOptionMenu(app, values=["MARKET", "LIMIT"], variable=type_var)
type_menu.pack(pady=10)

quantity_entry = ctk.CTkEntry(app, placeholder_text="Quantity")
quantity_entry.pack(pady=10)

price_entry = ctk.CTkEntry(app, placeholder_text="Price (for LIMIT orders)")
price_entry.pack(pady=10)

output_box = ctk.CTkTextbox(app, width=300, height=150)
output_box.pack(pady=10)

def place_order():
    symbol = symbol_entry.get().strip().upper()
    side = side_var.get()
    order_type = type_var.get()
    quantity = quantity_entry.get().strip()
    price = price_entry.get().strip()

    if not symbol or not quantity:
        output_box.insert("end", "Symbol and quantity are required.\n")
        return

    try:
        quantity = float(quantity)
    except ValueError:
        output_box.insert("end", "Quantity must be a number.\n")
        return

    if order_type == "LIMIT":
        try:
            price = float(price)
        except ValueError:
            output_box.insert("end", "Price must be a number for LIMIT order.\n")
            return
    else:
        price = None

    result = bot.place_order(symbol, side, order_type, quantity, price)

    if result:
        output_box.insert("end", f"Order placed:\n{result}\n\n")
    else:
        output_box.insert("end", "Failed to place order. See logs.\n")

# Place Order Button
order_btn = ctk.CTkButton(app, text="Place Order", command=place_order)
order_btn.pack(pady=20)

app.mainloop()
