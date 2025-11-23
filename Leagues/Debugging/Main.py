import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import logging

load_dotenv()
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

intents = discord.Intents.default()
intents.typing = False
intents.message_content = True
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    await bot.tree.sync()

# TODO:: Give this command functionality to fetch server info as an embed.
@bot.tree.command(name="serverinfo")
async def serverinfo(interaction: discord.Interaction):
    await interaction.response.send_message("This command is under development.")

@bot.tree.command(name="links")
async def links(interaction: discord.Interaction):
    await interaction.response.send_message("*Discord*: https://discord.gg/ufa-united-football-association-836277409245298708\n*Pitch*: Under Development\n*Others*: Coming soon")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send("Hello!")

    await bot.process_commands(message)

Token = os.getenv("Token")
bot.run(Token, log_handler=handler)
