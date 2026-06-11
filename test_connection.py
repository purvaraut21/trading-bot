from bot.client import get_client

client = get_client()

try:
    print("Testing Futures Account...")

    account = client.futures_account()

    print("SUCCESS")
    print(account)

except Exception as e:
    print("ERROR")
    print(e)