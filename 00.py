import requests
from pprint import pprint
url = "https://api.bithumb.com/public/ticker/BTC_KRW"
response = requests.get(url).json()
answer = response["data"]["prev_closing_price"]
print(answer)