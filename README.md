# Simplified Crypto Trading Bot – Binance Futures Testnet

A simplified crypto trading bot built in Python for Binance Futures Testnet. Supports market & limit orders via CLI and GUI, with logging, validation, and error handling. Bonus: lightweight UI built with CustomTkinter.

## 🔧 Core Features
**Order Execution**
- **Market/Limit Orders**
- **Testnet Integration**
- **Order Validation**

**Reliability**  
- **Error Handling**: API exception capture with retry logic
- **Activity Logging**: JSON-formatted logs with timestamps
- **Balance Checks**: Auto-reject orders exceeding testnet balance

## 🛠️ Technologies
### Core dependencies
- python-binance==1.0.28 # Binance API wrapper 
- customtkinter==5.2.0 # Modern UI components 
- python-dotenv==1.0.0 # Environment management