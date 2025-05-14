from bot import BasicBot
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")

bot = BasicBot(api_key, api_secret, testnet=True)

def main():
    print("=== Binance Futures Trading Bot ===")

    symbol = input("Enter trading symbol (e.g., BTCUSDT): ").strip().upper()
    if not symbol:
        print("Symbol cannot be empty.")
        return

    # Order side input
    side = input("Enter side (BUY or SELL): ").strip().upper()
    if side not in ["BUY", "SELL"]:
        print("Invalid side. Use BUY or SELL.")
        return

    # Order type input
    order_type = input("Enter order type (MARKET or LIMIT): ").strip().upper()
    if order_type not in ["MARKET", "LIMIT"]:
        print("Invalid order type. Use MARKET or LIMIT.")
        return

    # Quantity input
    try:
        quantity = float(input("Enter quantity: ").strip())
        if quantity <= 0:
            print("Quantity must be greater than 0.")
            return
    except ValueError:
        print("Invalid quantity. Must be a number.")
        return

    # Price input (only for LIMIT)
    price = None
    if order_type == "LIMIT":
        try:
            price = float(input("Enter limit price: ").strip())
            if price <= 0:
                print("Price must be greater than 0.")
                return
        except ValueError:
            print("Invalid price. Must be a number.")
            return

    print("\nPlacing order...\n")
    result = bot.place_order(symbol, side, order_type, quantity, price)

    if result:
        print("Order placed successfully!")
        print(result)
    else:
        print("Failed to place order. Check logs for details.")


if __name__ == "__main__":
    main()
