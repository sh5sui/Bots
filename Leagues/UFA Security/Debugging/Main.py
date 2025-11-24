import discord
from discord.ext import commands
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

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

@bot.tree.command(name="ban")
async def ban(interaction: discord.Interaction, member: discord.Member = None, reason: str = "No Reason"):
    if not interaction.user.guild_permissions.ban_members:
        await interaction.response.send_message("You don't have permission to run this command.", ephemeral=True)
        return
    
    if member == interaction.user:
        await interaction.response.send_message("You cannot ban yourself.", ephemeral=True)
        return
    
    if member.top_role >= interaction.user.top_role and interaction.user != interaction.guild.owner:
        await interaction.response.send_message("You cannot ban someone with a higher role than you.", ephemeral=True)
        return
    
    logschannel = bot.get_channel = 123
    await member.ban(reason=reason)
    await interaction.response.send_message(f"{member} Was banned for {reason}")
    await logschannel.send(f"Ban command was executed by {interaction.user} on {member}")

@bot.tree.command(name="kick")
async def kick(interaction: discord.Interaction, member: discord.Member = None, reason: str = "No Reason"):
    if not interaction.user.guild_permissions.kick_members:
        await interaction.response.send_message("You don't have permission to run this command.", ephemeral=True)
        return
    
    if member == interaction.user:
        await interaction.response.send_message("You cannot kick yourself.", ephemeral=True)
        return
    
    if member.top_role >= interaction.user.top_role and interaction.user != interaction.guild.owner:
        await interaction.response.send_message("You cannot kick someone with a higher role than you.", ephemeral=True)

        logschannel = bot.get_channel = 123
        await member.kick(reason=reason)
        await interaction.response.send_message(f"{member} Was kicked for {reason}")
        await logschannel.send(f"Kick command was executed by {interaction.user} on {member}")

Token = os.getenv("Token")
bot.run(Token)