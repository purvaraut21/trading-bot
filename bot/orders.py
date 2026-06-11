# Import Binance client function
from bot.client import get_client

# import logger
from bot.logging_config import logger

# create binance client
client = get_client()

# Function to place MARKET order
def place_market_order(symbol,side,quantity):

    try:
        # Log request details
        logger.info(
            f"MARKET ORDER REQUEST -> Symbol: {symbol}, Side:{side}, Quantity:{quantity}"
        )

        # Send market order
        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

        # Log response
        logger.info(f"MARKET ORDER RESPONSE -> {response}")

        return response
    
    except Exception as e:

        logger.error(f"MARKET ORDER ERROR -> {e}")

        raise

# Function to place LIMIT order\
def place_limit_order(symbol,side,quantity,price):

    try:

        # Log request
        logger.info(
            f"LIMIT ORDER REQUEST-> Symbol: {symbol}, Side:{side}, Quantity:{quantity}, Price:{price}"
        )

        # Send limit order
        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

        # Log response
        logger.info(f"LIMIT ORDER RESPONSE -> {response}")
        
        return response
    

    except Exception as e:
        logger.error(f"LIMIT ORDER ERROR -> {e}")

        raise