import os
from dotenv import load_dotenv 
import freecurrencyapi

load_dotenv()

API_KEY = os.getenv("API_KEY")
client = freecurrencyapi.Client(API_KEY)

def convert(source_currency: str, target_currency: str, amount: float) -> float:
    data = client.latest(source_currency, [target_currency])
    target_amt = data['data'][target_currency]

    result = amount * target_amt
    return round(result, 2)

def convertInterval(date: str, source_currency: str, target_currency: str, amount: float) -> float:
    data = client.historical(date, source_currency, [target_currency])
    target_amt = data['data'][date][target_currency]

    result = amount * target_amt
    return round(result, 2)
