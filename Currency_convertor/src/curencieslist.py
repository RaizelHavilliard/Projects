import requests

url = 'https://v6.exchangerate-api.com/v6/744e61f680700cd3dbfdd92f/latest/USD'
response = requests.get(url)
my_list = list(response.json()["conversion_rates"].keys())