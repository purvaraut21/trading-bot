# Validate BUY or SELL
def validate_side(side):
    if side.upper() not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")
    
# Validate MARKET or LIMIT
def validate_order_type(order_type):
    if order_type.upper() not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")

# Validate quantity
def validate_quantity(quantity):
    if float(quantity) <= 0:
        raise ValueError("Quantity must be greater than 0")