import logging
import discord
import asyncio
from discord.ext import commands

bot = commands.Bot(command_prefix="?")
bot.remove_command('help')
logging.basicConfig(level=logging.INFO)

startup_ext = ['commands.music']


@bot.async_event
def main():
    yield from bot.login('MjQyNzEyNTY2NzUxNTU5Njgx.Cv-6kw.Ro6FBHxgCpl5SRQGkFkwZZu9jRc')
    yield from bot.connect()


@bot.async_event
def on_ready():
    yield from bot.change_presence(game=discord.Game(name='shit miguel likes'))
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print('-' * 10)

    for ext in startup_ext:
        try:
            bot.load_extension(ext)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(ext, exc))


loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main())
except:
    loop.run_until_complete(bot.logout())
finally:
    loop.close()
