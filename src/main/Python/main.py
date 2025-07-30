# Discord Bot One (Discord Tem Bot)
#
# Created by Bluejay Dev on 07/27/2025
# Simple Discord Bot (Arisu Bot Ver.)
# Package: DiscordBotOne.src.main.Python; Class: main.py

import logging
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load the .env file and token
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

# Create the file handler for logging
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

# Set up the intents for the bot
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# Set up the command prefix
bot = commands.Bot(command_prefix='!', intents=intents)

# Role variables
gdd_role = "GDD Gamer"

# -------- Set up event handlers --------

# Status: Ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('Panpakapan~! (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧')

# Handler: New member joins (Send DM)
@bot.event
async def on_member_join(member):
    await member.send(f'Welcome to the server, {member.name}! A new member has joined Arisu\'s Party!')

# Handler: handle excluded words or certain phrases
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Profanity and racial slur filter set (Will be updated)
    banned_words = {"nigger", "nigga", "rape", "raped", "beaner"}

    if any(banned_word in message.content.lower() for banned_word in banned_words):
        await message.delete()
        await message.channel.send(f'{message.author.mention} is not allowed to say that here!')

    await bot.process_commands(message)

# -------- Bot Commands --------

# !hello command
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello, {ctx.author.mention} sensei!')

#---- Role Management ----

# Role assignment (!assign)
@bot.command()
async def assign(ctx):
    role = discord.utils.get(ctx.guild.roles, name=gdd_role)
    if role:
        await ctx.author.add_roles(role)
        await ctx.send(f"**{ctx.author.mention} has joined the party! Now they're a {gdd_role}!"
                       + "\nPanpakapan~! (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧**")
    else:
        await ctx.send("**It looks like the party's full or maybe it's the wrong one..."
                       + f"Arisu is so sorry {ctx.author.mention}!!!\n┗( T﹏T )┛**")

#Role removal (!remove)
@bot.command()
async def remove(ctx):
    role = discord.utils.get(ctx.guild.roles, name=gdd_role)
    if role:
        await ctx.author.remove_roles(role)
        await ctx.send(f"**{ctx.author.mention} has left the party! They're no longer a {gdd_role}!"
                       + "\n(┬┬﹏┬┬)**")
    else:
        ctx.send("**Arisu doesn't think you have that role. Maybe it isn't real? (⊙_⊙)？**")

# Has a certain role? (!secret)
@bot.command()
@commands.has_role(gdd_role)
async def secret(ctx):
    await ctx.send(f"**{ctx.author.mention} is an epic gamer sensei! (★‿★)**")

@secret.error
async def secret_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send(f"**Wah! {ctx.author.mention} does not have that permission! (⊙-⊙;)"
                       + "\nSensei needs to get stronger before they can take on that role! (•ˋ _ ˊ•)**")
# ---- End Role Management ----

# Sends a dm with a specified message
@bot.command()
async def dm(ctx, *, msg):
    await ctx.author.send(f"{msg}")

# Replies
@bot.command()
async def reply(ctx):
    await ctx.reply(f"**Panpakapan~! (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧**")

# Polling
@bot.command()
async def poll(ctx, *, question):
    embed = discord.Embed(title="Poll", description=question, color=0x33BCEF)
    poll_message = await ctx.send(embed=embed)
    await poll_message.add_reaction("✅")
    await poll_message.add_reaction("❌")

# Run the bot with token and log file handler
bot.run(token, log_handler=handler, log_level=logging.DEBUG)