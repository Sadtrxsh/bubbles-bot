import random
import discord
from discord.ext import commands, tasks

TOKEN = "TOKEN HERE"
bubbles_id = 1234567890 #PUT YOUR CHANNEL ID FOR BUBBLES HERE

bot = discord.ext.commands.Bot(command_prefix = "!")
@bot.event
async def on_ready():
    send_message.start()

@tasks.loop(seconds=100)
async def send_message():
    size = random.randint(6,14)
    await bot.get_channel(bubbles_id).send("\n".join(["||pop||" * size] * size))
bot.run(TOKEN)
