from binance.client import Client
from dotenv import load_dotenv
import os

# Load variables from .env file
load_dotenv()

# Read API credentials
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")

# Create and return Binance Futures Testnet client
def get_client():

    # Create Binance client object
    client = Client(
        api_key,
        api_secret
    )

    # Set Futures Testnet endpoint
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    return client