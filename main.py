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

acak = random.randint(1,20)
acak1 = random.randint(1,20)
@bot.command()
async def give(ctx):
    await ctx.send('I will give you star')
    await ctx.send('answer this question')
    await ctx.send(acak)
    await ctx.send("+")
    await ctx.send(acak1)


bot.run("Token Anda")
