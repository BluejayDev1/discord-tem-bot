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
