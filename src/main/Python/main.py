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
        await message.channel.send(f"{message.author.mention} is not allowed to say that here!")

    await bot.process_commands(message)

# Run the bot with token and log file handler
bot.run(token, log_handler=handler, log_level=logging.DEBUG)