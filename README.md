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

## Project Folder Structure

project_root/
├── src/
│ ├── config.py
│ ├── logger.py
│ ├── cli.py
│ ├── market_orders.py
│ ├── limit_orders.py
│ ├── stop_limit.py
│ ├── oco.py
│ ├── twap.py
│ ├── grid.py
│ └── utils/
│ └── validators.py
├── bot.log
├── requirements.txt
├── README.md
└── report.pdf

## How to Run the Bot

1. Install dependencies: Use pip install -r requirements.txt in your terminal.
2. Navigate to the src directory.
3. Run the CLI by executing the main script

```
bash
python cli.py
```

4. Follow the prompts to select order type, pair, side, price, etc.
5. All logs will be stored in bot.log.

### Author
##### Sagar Gurung
