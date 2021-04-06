import random
import discord
from discord.ext import commands, tasks

bot = discord.ext.commands.Bot(command_prefix = "!")
@bot.event
async def on_ready():
    send_message.start()

@tasks.loop(seconds=100)
async def send_message():
    size = random.randint(6,14)
    await bot.get_channel(828838318006468649).send("\n".join(["||pop||" * size] * size))
bot.run('bot token here')
