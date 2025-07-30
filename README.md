# Sagar's Binance Futures Bot

## Introduction
This is a command-line interface (CLI) trading bot built for the Binance USDT-M Futures Testnet. The bot allows users to place multiple types of orders including Market, Limit, and advanced strategies like Stop-Limit, OCO, TWAP, and Grid trading. The goal is to provide a modular, extensible, and well-logged system to simulate automated trading logic using the Binance Futures API.

## Key Features

1. CLI-based interface for order placement
2. Market and Limit order execution (core functionality)
3. Advanced order strategies: Stop-Limit, OCO, TWAP and Grid
4. Input validation for symbols, sides, prices, and quantities
5. Structured logging for all actions including API responses and errors
6. Organized project structure for easy extension and debugging

## Tech Stack

1. Python 3
2. Binance USDT-M Futures Testnet API (REST)
3. requests and hmac for secure API communication
4. argparse and input() for CLI interaction
5. logging module for maintaining log files

## API Setup Instructions

1. Sign up for a Binance Futures Testnet account.
2. Generate API Key and Secret Key from the API management section.
3. Store your credentials in a .env file or inject them as environment variables: API_KEY, SECRET_KEY
4. Use only the Binance Futures Testnet base URL for all endpoints: https://testnet.binancefuture.com

## How to Run the Bot

1. Clone the repository:

bash
```
git init
git clone https://github.com/sagar1024/Sagars_Binance_Bot.git
```

2. Navigate to the project directory:

bash
```
cd Sagars_Binance_Bot
```

3. Install dependencies:

Run this to install all required Python packages.

bash
```
pip install -r requirements.txt
```

4. Navigate to the src directory:

bash
```
cd src
python cli.py
```

5. Follow the on-screen prompts to select the order type, trading pair, side, price, quantity, and other details.
6. All logs will be recorded in the bot.log file located in the root project directory.

### Author
##### Sagar Gurung
