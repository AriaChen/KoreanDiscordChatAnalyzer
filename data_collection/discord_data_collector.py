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
    messages = []

    async for message in channel.history(limit=100000):
        if not message.content:  # Skip empty messages
            continue

        # Convert UTC to Korea time zone
        local_time = message.created_at.replace(tzinfo=pytz.utc).astimezone(pytz.timezone("Asia/Seoul"))
        formatted_time = local_time.strftime("%Y-%m-%d %H:%M:%S")

        messages.append([formatted_time, str(message.author), message.content])

    # Create a DataFrame and save to CSV
    df = pd.DataFrame(messages, columns=['Timestamp', 'Author', 'Content'])
    df.to_csv('../data/chat_data.csv', index=False, encoding='utf-8-sig')


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
