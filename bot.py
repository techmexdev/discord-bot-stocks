import os
import discord

from parser import parse_message, validate_message

keys = ["DISCORD_SECRET_TOKEN", "FINHUB_API_KEY"]
def check_env():
    keys_valid = True
    for key in keys:
        try:
            os.environ[key]
        except KeyError:
            print(f"Error: Env Variable '{key}' is not set!")
            keys_valid = False

    return keys_valid

discord_client = discord.Client()

@discord_client.event
async def on_ready():
    print(f'Logged on as {discord_client.user}!')

@discord_client.event
async def on_message(message):

    if message.author == discord_client.user:
        return

    if not validate_message(message.content):
        return

    response = parse_message(message.content)

    await message.channel.send(response)

def main():
    if not check_env():
        print("\nYou do not have all of the required ENV variables.\nExiting..")
        return 1

    discord_secret_token = os.environ["DISCORD_SECRET_TOKEN"]
    discord_client.run(discord_secret_token)

if __name__ == '__main__':
    exit(main())

