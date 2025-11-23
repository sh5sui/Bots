import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import logging
from discord import app_commands

load_dotenv()
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

intents = discord.Intents.default()
intents.typing = False
intents.message_content = True
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix="!", intents=intents)

freeagentchannel_id = 1387870667411558561
friendlieschannel_id = 1387782160697655409
contractschannel_id = 1387870804225687764

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
    await interaction.response.send_message("*Discord*: https://discord.gg/ufa-united-football-association-836277409245298708\n*Pitch*: https://www.roblox.com/games/137624913542642\n*Others*: Coming soon")

@bot.tree.command(name="freeagency")
@app_commands.describe(
    position="Your position",
    region="Your region"
)
async def freeagency(interaction: discord.Interaction, position: str, region: str):
    freeagentchannel = bot.get_channel(1387870667411558561)
    user_id = interaction.user.id
    await interaction.response.send_message("Free agency post sent!", ephemeral=True)
    await freeagentchannel.send(f"<@{user_id}> is a free agent! Position: {position}, Region: {region}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send("Hello!")

    await bot.process_commands(message)

Token = os.getenv("Token")
bot.run(Token, log_handler=handler)
