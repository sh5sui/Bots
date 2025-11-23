import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import logging
from discord import app_commands
from discord import guild

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
    
    guild = interaction.guild
    user_id = interaction.user.id

    embed = discord.Embed(title="Sever Information", color=discord.Color.purple())
    embed.set_thumbnail(url=guild.icon.url)
    embed.add_field(name="Requested By", value=f"<@{user_id}>")
    embed.add_field(name="Server Name", value=guild.name)
    embed.add_field(name="Server ID", value=guild.id)
    embed.add_field(name="Members", value=guild.member_count)
    embed.add_field(name="Owner", value=guild.owner)
    embed.add_field(name="Creation Date", value=guild.created_at)

    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="links")
async def links(interaction: discord.Interaction):
    await interaction.response.send_message("*Discord*: https://discord.gg/ufa-united-football-association-836277409245298708\n*Pitch*: https://www.roblox.com/games/137624913542642\n*Others*: Coming soon")

# TODO:: Make this an embed
@bot.tree.command(name="freeagency")
@app_commands.describe(
    position="Your position",
    region="Your region"
)
async def freeagency(interaction: discord.Interaction, position: str, region: str):
    freeagentchannel = bot.get_channel(1387870667411558561)
    if freeagentchannel is None:
        await interaction.response.send_message("Free agency channel could not be found.", ephemeral=True)
        return
    
    user_id = interaction.user.id

    await interaction.response.send_message("Free agency post sent!", ephemeral=True)

    embed = discord.Embed(title="Free Agent", color=discord.Color.blue())
    embed.add_field(name="User", value=f"<@{user_id}>")
    embed.add_field(name="Position", value=position)
    embed.add_field(name="Region", value=region)

    await freeagentchannel.send(embed=embed)

Token = os.getenv("Token")
bot.run(Token, log_handler=handler)
