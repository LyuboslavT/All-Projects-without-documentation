#import libs
import requests

#define function
def convert_currency(amount, from_currency, to_currency):
    api_key = '350664e980009b920e8fb3cd'
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}'

    response = requests.get(url)
    data = response.json()

    # initial logic
    if response.status_code != 200 or "conversion_rates" not in data:
        return "Error fetching exchange rate"

    exchange_rate = data["conversion_rates"].get(to_currency)

    if exchange_rate is None:
        return "Invalid currency code"
    rate = exchange_rate
    print(f'Exchange rate is {rate} for that type of currency')
    return amount * rate


# get user input
amount = float(input('Enter the amount to convert: '))
from_currency = input('Enter the currency to convert from: ')
to_currency = input('Enter the currency to convert to: ')

# convert currency
converted_amount = convert_currency(amount, from_currency, to_currency)

#print result with base logic
print(f'For {amount} {from_currency} you will get {converted_amount:.3f} {to_currency}' if isinstance(converted_amount, float) else converted_amount)