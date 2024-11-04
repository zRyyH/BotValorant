import discord
from discord.ext import commands
import threading
import time
import asyncio


intents = discord.Intents.default()
intents.message_content = True  # Enable message content intent

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Bot está pronto. Logado como {bot.user.name}')


async def send_to_channel(message):
    channel = bot.get_channel(1283810201027346485)
    print(channel)

    if channel:
        await channel.send(message)


def loop():
    bot.run("MTI4Mzc3NjY1OTMxNjgwMTYyNw.G-b2VF.EzvYDLZ1kUcMRQtnUxICQ0KsP2RinhCulGhdgk")
    while True:
        time.sleep(1)


threading.Thread(target=loop, daemon=True).start()


def notify(message = '@everyone Elo liberado!'):
    asyncio.run_coroutine_threadsafe(send_to_channel(message=message), bot.loop)
