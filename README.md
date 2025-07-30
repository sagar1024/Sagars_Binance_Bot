# Sagar's Binance Futures Order Bot

## Introduction
This is a command-line interface (CLI) trading bot built for the Binance USDT-M Futures Testnet. The bot allows users to place multiple types of orders including Market, Limit, and advanced strategies like Stop-Limit, OCO, TWAP, and Grid trading. The goal is to provide a modular, extensible, and well-logged system to simulate automated trading logic using the Binance Futures API.

## Key Features

1. CLI-based interface for order placement
2. Market and Limit order execution (mandatory core functionality)
3. Advanced order strategies:
4. Stop-Limit orders
5. One-Cancels-the-Other (OCO) orders
6. TWAP (Time-Weighted Average Price)
7. Grid Trading Strategy

Input validation for symbols, sides, prices, and quantities

Structured logging for all actions including API responses and errors

Organized project structure for easy extension and debugging

Tech Stack

Python

Binance USDT-M Futures Testnet API (REST)

requests and hmac for secure API communication

argparse and input() for CLI interaction

logging module for maintaining log files

API Setup Instructions

Sign up for a Binance Futures Testnet account.

Generate API Key and Secret Key from the API management section.

Store your credentials in a .env file or inject them as environment variables:

BINANCE_API_KEY

BINANCE_SECRET_KEY

Use only the Binance Futures Testnet base URL for all endpoints:

https://testnet.binancefuture.com

Project Folder Structure
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

How to Run the Bot

Install dependencies:

Use pip install -r requirements.txt in your terminal.

Navigate to the src directory.

Run the CLI by executing the main script (cli.py).

Follow the prompts to select order type, pair, side, price, etc.

All logs will be stored in bot.log.

Author
Sagar G.
Passionate about algorithmic trading and backend systems.

