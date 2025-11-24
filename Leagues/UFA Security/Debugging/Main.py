import discord
from discord.ext import commands
import asyncio
import os

intents = discord.Intents.default()
intents.typing = False
intents.message_content = True
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Connected as {bot.user}")
    await bot.tree.sync()

token = os.getenv("Token")
bot.run(token)