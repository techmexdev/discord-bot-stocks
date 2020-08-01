import os
import requests

def get_stocks(symbol: str) -> str:
    finhub_api_key = os.environ["FINHUB_API_KEY"]

    r = requests.get(f'https://finnhub.io/api/v1/quote?symbol={symbol}&token={finhub_api_key}')
    body = r.json()
    if "error" in body:
        return body["error"]

    current_price = body["c"]
    return current_price
