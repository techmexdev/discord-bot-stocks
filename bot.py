import requests
import os
import discord

finhub_api_key = os.environ["FINHUB_API_KEY"]
symbol = os.environ["SYMBOL"]

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        symbol = message["content"]
        current_price = get_stocks(symbol)
        return f'current price for {symbol}: {current_price}'

client = MyClient()
client.run(finhub_api_key)

def get_stocks(symbol: str) -> str:
    r = requests.get(f'https://finnhub.io/api/v1/quote?symbol={symbol}&token={finhub_api_key}')
    body = r.json()
    if "error" in body:
        return body["error"]

    current_price = body["c"]
    return current_price

current_price = get_stocks(symbol)
print(f'current price: {current_price}')

