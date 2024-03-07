import os
import discord

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

# { "guilds", "members", "messages", "reactions", "guild_messages", "message_content", "guild_reactions"}
intents = discord.Intents(guilds=True, members=True, messages=True, reactions=True, guild_messages=True, message_content=True, guild_reactions=True)
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)