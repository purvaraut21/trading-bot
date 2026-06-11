# Binance Futures Testnet Trading Bot

## Overview

This project is a Python-based trading bot that places MARKET and LIMIT orders on Binance Futures Testnet using the Binance API.

## Features

* BUY and SELL orders
* MARKET and LIMIT order support
* Command-line input using argparse
* Input validation
* Logging and error handling

## Setup

1. Create a virtual environment

```bash
python -m venv venv
```

2. Activate the environment

```bash
venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Create a `.env` file

```env
API_KEY=your_api_key
API_SECRET=your_api_secret
```

## Run Examples

MARKET Order:

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

LIMIT Order:

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 50000
```

## Log File

All API requests, responses, and errors are stored in:

```text
trading_bot.log
```

## Author

Purva Raut

GitHub Repository:
https://github.com/purvaraut21/trading-bot
