import discord
import asyncio
import os
import pandas as pd
import datetime
import pytz

TOKEN = os.getenv('DISCORD_BEARBOT_TOKEN')
CHANNEL_ID = 1061072760727666698

intents = discord.Intents.default()  # define the necessary intents
intents.messages = True  # to receive messages
intents.message_content = True

client = discord.Client(intents=intents)


async def fetch_messages(channel):
    async for message in channel.history(limit=3):  # Fetch the last three messages
        utc_time = message.created_at
        # Change to Korea time zone
        local_time = utc_time.replace(tzinfo=pytz.utc).astimezone(pytz.timezone("Asia/Seoul"))
        content = message.content
        if message.attachments:
            content += " [Attachments: " + ", ".join(attachment.url for attachment in message.attachments) + "]"
        if message.embeds:
            content += " [Embeds provided]"
        print(f"{local_time} - {message.author}: {content}")


@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        await fetch_messages(channel)
    else:
        print(f"Channel with ID {CHANNEL_ID} not found.")
    await client.close()

client.run(TOKEN)
