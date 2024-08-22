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
async def bestfriend(ctx):
    question ='Do you want to be my friend?'
    await ctx.send(question)

@bot.command()
async def yes(ctx):
    await ctx.send('Really?')
    await ctx.send('You want to be friends with a bot?')

@bot.command()
async def ya(ctx):
    await ctx.send('thank you for being my friend') 
   
@bot.command()
async def guess(ctx):
    await ctx.send('Guess a number between 1 and 10.')

@bot.command()
async def answer(ctx,n):
    if n == random.randint(1,13):
        await ctx.send('Good Job!')
    else:
        await ctx.send('Try Again!')

bot.run("Token Anda")
