import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def guess(ctx):
    await ctx.send('Guess the number between 1 to 7')

@bot.command()
async def answer(ctx, n = random.randint(1,7)):
    if n == random.randint(1,7):
        await ctx.send('Congrats, You guessed the right number!')
    else:
        await ctx.send('Skill Issue')

bot.run("Token Anda")
