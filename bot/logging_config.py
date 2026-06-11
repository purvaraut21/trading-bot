# import logging module
import logging

# configure logging settings
logging.basicConfig(
    filename="trading_bot.log", # Log file name
    level= logging.INFO, # Store INFO and above
    format="%(asctime)s - %(levelname)s - %(message)s"
)
# Create logger object
logger = logging.getLogger(__name__)

