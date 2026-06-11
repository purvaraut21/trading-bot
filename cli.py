import argparse

from bot.orders import(
    place_market_order,
    place_limit_order
)

from bot.validators import(
    validate_side,
    validate_order_type,
    validate_quantity
)

# Create argument parser
parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", required=True)

# Price is optional because MARKET orders don't need it
parser.add_argument("--price")

args = parser.parse_args()

try:
    # validate inputs
    validate_side(args.side)
    validate_order_type(args.type)
    validate_quantity(args.quantity)

    print("\n=== ORDER REQUEST ===")
    print("Symbol :", args.symbol)
    print("Side :", args.side)
    print("Type :", args.type)
    print("QTY :", args.quantity)

    if args.type.upper() == "MARKET":
        response = place_market_order(
            args.symbol,
            args.side,
            args.quantity
        )
    else:
        if not args.price:
           raise ValueError(
               "Price is required for LIMIT order"
           )
        response = place_limit_order(
            args.symbol,
            args.side,
            args.quantity,
            args.price
        ) 

        print("\n=== ORDER RESPONSE ===")
        print("Order ID : ", response.get("orderId"))
        print("Status : ", response.get("status"))
        print("Executed Qty : ", response.get("executedQty"))

        print("\nSUCCESS")

except Exception as e:

    print("\nFAILED")
    print(e)