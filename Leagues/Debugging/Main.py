import discord
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

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

@client.tree.command(name="serverinfo")
async def serverinfo(interaction: discord.Interaction):
    await interaction.response.send_message("This command is under development.")

Token = os.getenv("Token", log_Handler=handler)
client.run(Token)