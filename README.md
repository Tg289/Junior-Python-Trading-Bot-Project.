# Junior Python Trading Bot (Binance Futures Testnet)


This repository contains a **FULL PROJECT** implementation for the assignment: a simplified trading bot that interacts with Binance Futures Testnet (USDT-M).


**Highlights**
- Place MARKET and LIMIT orders (buy/sell) on Binance Futures Testnet.
- Additional order type: **TWAP** (bonus) and **Stop Market** (stop-style order for futures).
- Clean project structure (`src/`), CLI (`cli.py`), reusable logic (`basic_bot.py`, `order_types.py`).
- Logging of requests, responses and errors to `sample_logs/basic_bot.log`.
- Input validation, clear stdout output, and error handling.


---


## Setup


1. Create testnet account and generate API key + secret at: `https://testnet.binancefuture.com` (Futures Testnet).
2. Clone the repo and create a virtualenv:


```bash
python -m venv .venv
source .venv/bin/activate # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
