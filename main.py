import discord
import random
import os
import requests
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

@bot.group(hidden=True)
async def secret(ctx: commands.Context):
    """What is this "secret" you speak of?"""
    if ctx.invoked_subcommand is None:
        await ctx.send('There is no secret in this code yet', delete_after=5)

@bot.command()
async def tutor_file(ctx):
    await ctx.send('Untuk membaca file, kita menggunakan open - fungsi yang dibangun ke dalam Python. Fungsi ini memungkinkan kita untuk membuka file dalam beberapa mode:')
    await ctx.send('w - merekam data ke dalam file, tetapi tidak sebelum menghapus semua data yang tersimpan sebelumnya;')
    await ctx.send('r - membuka file dalam mode read-only;')
    await ctx.send ('a - merekam data di akhir file, tanpa menghapus apa pun;')
    await ctx.send('rb - membuka file non-teks untuk dibaca;')
    await ctx.send('wb - membuka file non-teks untuk perekaman.')


@bot.command()
async def random_meme(ctx):
    images = os.listdir('image')
    with open('image/'+random.choice(images), 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)


def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def get_duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

bot.run("Token Anda")
