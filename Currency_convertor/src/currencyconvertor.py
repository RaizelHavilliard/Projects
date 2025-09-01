import requests
from cachetools import TTLCache

cache = TTLCache(maxsize=100, ttl=5*60*60)

@cached(cache)
def get_exchange_rate(base_currency, target_currency):
    url = f"https://v6.exchangerate-api.com/v6/744e61f680700cd3dbfdd92f/latest/{base_currency}"
    response = requests.get(url)
    return response.json()['conversion_rates'][target_currency]


def convert_currency(amount, exchange_rate):
    return amount * exchange_rate 


amount = 100
base_currency = 'USD'
target_currency = 'CAD'
exchange_rate = get_exchange_rate(base_currency, target_currency)


if __name__ == '__main__':
    base_currency = input('enter bas currency: ')
    target_currency = input('enter target currency: ')
    amount = float(input('Enter amount: '))
    exchange_rate = get_exchange_rate(base_currency, target_currency)
    converted_amount = convert_currency(exchange_rate, amount)
    print(f'{amount} {base_currency} is {converted_amount} of {target_currency}')