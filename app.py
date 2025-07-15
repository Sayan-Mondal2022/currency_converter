from flask import Flask, request, jsonify
import random
import convert

app = Flask(__name__)

# Predefined response parts
PREFIXES = [
    "Sure thing!", "Got it!", "Absolutely!", "Here you go!",
    "No problem!", "Let me crunch the numbers...", "Quick math coming up!",
    "Done!", "Here’s the conversion:", "Alright!"
]

SUFFIXES = [
    "Hope that helps!", "Need another conversion?",
    "Anything else you want to convert?", "Let me know if you need a historical rate too!",
    "Want to compare with another currency?", "I’ve got more exchange tricks if you need them!",
    "Feel free to throw in another currency!", "Always happy to help you!",
    "Math magic at your service!"
]

@app.route("/", methods=["POST"])
def index():
    prefix = random.choice(PREFIXES)
    suffix = random.choice(SUFFIXES)

    data = request.get_json()
    parameters = data['queryResult']['parameters']

    # Historical conversion
    if "date-period" in parameters:
        return handle_historical_conversion(parameters)

    # Regular conversion with amount
    if parameters.get('unit-currency'):
        return handle_amount_conversion(parameters, prefix, suffix)

    # Conversion without amount (defaults to 1)
    return handle_default_conversion(parameters, prefix, suffix)

def handle_historical_conversion(parameters):
    input_currency = parameters.get('unit-currency')
    currency_names = parameters.get('currency-name')

    if input_currency:
        if isinstance(input_currency, list) and len(input_currency) == 1:
            input_currency = input_currency[0]
        source_currency = input_currency['currency']
        amount = input_currency['amount']
        target_currency = currency_names[0]
    else:
        # If unit-currency not provided, try to infer from currency-name
        input_currency = currency_names
        if len(input_currency) == 1:
            source_currency = target_currency = input_currency[0]
        else:
            source_currency, target_currency = input_currency[:2]
        amount = 1

    # Fix potential future dates
    start_date = parameters["date-period"]["startDate"][:10]
    if int(start_date[:4]) >= 2026:
        start_date = "2025" + start_date[4:]

    final_amount = convert.convertInterval(start_date, source_currency, target_currency, amount)
    response_text = f"{amount} {source_currency} on {start_date[:4]} was {final_amount} {target_currency}"

    return jsonify({'fulfillmentText': response_text})


# Working when both the Base currency and Source Currency when the Base amount is given.
def handle_amount_conversion(parameters, prefix, suffix):
    input_currency = parameters['unit-currency']

    if isinstance(input_currency, list) and len(input_currency) == 1:
        input_currency = input_currency[0]

    source_currency = input_currency['currency']
    amount = input_currency['amount']
    target_currency = parameters['currency-name'][0]

    final_amount = convert.convert(source_currency, target_currency, amount)

    response_text = (
        f"{prefix}\n\n"
        f"{amount} {source_currency} will be {final_amount} {target_currency}.\n\n"
        f"{suffix}"
    )
    print(response_text)
    return jsonify({'fulfillmentText': response_text})


# Used when we are finding just the rates.
def handle_default_conversion(parameters, prefix, suffix):
    currencies = parameters["currency-name"]
    source_currency, target_currency = currencies[:2]
    amount = 1

    final_amount = convert.convert(source_currency, target_currency, amount)

    response_text = (
        f"{prefix}\n\n"
        f"1 {source_currency} will be {final_amount} {target_currency}.\n\n"
        f"{suffix}"
    )
    return jsonify({'fulfillmentText': response_text})


if __name__ == "__main__":
    app.run(debug=True)