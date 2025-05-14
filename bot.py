from binance.client import Client
import datetime
import logging

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.testnet = testnet
        self.client = Client(api_key, api_secret)

        if testnet:
            self.client.FUTURES_URL = 'https://testnet.binancefuture.com'

        # Logging setup
        log_filename = f"bot_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_filename),
                logging.StreamHandler()
            ]
        )

        logging.info("Initialized Binance client with testnet=%s", testnet)

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            params = {
                'symbol': symbol,
                'side': side.upper(),
                'type': order_type.upper(),
                'quantity': quantity
            }

            if order_type.upper() == 'LIMIT':
                params['price'] = price
                params['timeInForce'] = 'GTC'

            response = self.client.futures_create_order(**params)
            logging.info("Order placed: %s", response)
            return response
        except Exception as e:
            logging.error("Error placing order: %s", e)
            return None
