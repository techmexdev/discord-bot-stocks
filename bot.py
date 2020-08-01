import requests
import os
import discord

finhub_api_key = os.environ["FINHUB_API_KEY"]
discord_secret_token = os.environ["DISCORD_SECRET_TOKEN"]

def get_stocks(symbol: str) -> str:
    print("symbol", symbol)
    r = requests.get(f'https://finnhub.io/api/v1/quote?symbol={symbol}&token={finhub_api_key}')
    body = r.json()
    if "error" in body:
        return body["error"]

    current_price = body["c"]
    return current_price


discord_client = discord.Client()

@discord_client.event
async def on_ready():
    print(f'Logged on as {discord_client.user}!')

@discord_client.event
async def on_message(message):

    if message.author == discord_client.user:
        return

    print(f'Message from {message.author}: {message.content}')
    msg_spl = message.content.split(" ")
    if len(msg_spl) != 2 or msg_spl[1] != "stocks":
        return

    symbol = msg_spl[0]
    current_price = get_stocks(symbol)
    msg = f'current price for {symbol}: {current_price}'
    await message.channel.send(msg)

discord_client.run(discord_secret_token)

