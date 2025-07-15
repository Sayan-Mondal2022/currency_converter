import os
import logging
from dotenv import load_dotenv
import freecurrencyapi

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Get API Key from environment
API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise EnvironmentError("API_KEY not found in environment variables.")

# Initialize client
client = freecurrencyapi.Client(API_KEY)

def convert(source_currency: str, target_currency: str, amount: float) -> float:
    """
    Converts a given amount from source_currency to target_currency using the latest exchange rate.
    """
    try:
        response = client.latest(source_currency, [target_currency])
        rate = response['data'].get(target_currency)
        if rate is None:
            raise ValueError(f"No conversion rate found for {target_currency}")
        result = amount * rate
        return round(result, 2)
    except Exception as e:
        logger.error(f"Error during currency conversion: {e}")
        raise

def convert_on_date(date: str, source_currency: str, target_currency: str, amount: float) -> float:
    """
    Converts a given amount from source_currency to target_currency based on historical rate for a specific date.
    Date format: YYYY-MM-DD
    """
    try:
        response = client.historical(date, source_currency, [target_currency])
        rate = response['data'].get(date, {}).get(target_currency)
        if rate is None:
            raise ValueError(f"No historical rate found for {target_currency} on {date}")
        result = amount * rate
        return round(result, 2)
    except Exception as e:
        logger.error(f"Error during historical conversion: {e}")
        raise
