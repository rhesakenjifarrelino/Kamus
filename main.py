import discord
import os
import random
import requests
from datetime import datetime
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='=', intents=intents)

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
        await ctx.send('Try again')


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

@bot.command()
async def get_tokusatsu(ctx):
    images = os.listdir('tokusatsu')
    with open('tokusatsu/'+random.choice(images), 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)    
 

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('get_duck')
async def get_duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def maps(ctx):
    await ctx.send('Visit this website: https://www.google.com/maps')

@bot.command()
async def youtube(ctx):
    await ctx.send('Visit this website: https://www.youtube.com/')

@bot.command()
async def github(ctx):
    await ctx.send('Visit this website: https://github.com/')    

@bot.command()
async def bot_developer(ctx):
    await ctx.send('The bot maker is on github: https://github.com/rhesakenjifarrelino')

# Daftar tautan gambar
gambar_links = [
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQwshA3o6OlS7f2N0c_6MGgRCmBhkfBC_j-Wg&s',
    'https://live.staticflickr.com/8127/8701179380_7806eab378.jpg',
    'https://i.pinimg.com/236x/94/4e/3e/944e3ea9b769564d1a282115a37d8a8d.jpg'
]

@bot.command()
async def gambar_lucu(ctx):
    # Memilih tautan gambar secara acak
    link = random.choice(gambar_links)
    await ctx.send(f'Here is a random image: {link}')


pantun_list = [
    "Buah mangga buah kedondong,Dibawa anak ke pasar minggu.Selamat pagi wahai Tuan,Semoga hari ini menyenangkan bagimu.",
    "Jalan-jalan ke kota Blitar,Beli oleh-oleh berupa sukun.Selamat pagi wahai sahabat,Semoga harimu penuh dengan senyuman.",
    "Burung merpati terbang tinggi,Hinggap di dahan pohon jati.Selamat pagi wahai kawan,Semoga harimu penuh arti."
]

@bot.command()
async def pantun(ctx):
    pantun = random.choice(pantun_list)
    await ctx.send(pantun)    

@bot.command()
async def calculator(ctx, *, expression: str):
    try:
        result = eval(expression)
        await ctx.send(f'Hasil: {result}')
    except Exception as e:
        await ctx.send('Ekspresi tidak valid!')


@bot.command()
async def rps(ctx, choice: str):
    choices = ['rock', 'paper', 'scissors']
    bot_choice = random.choice(choices)
    await ctx.send(f'Bot memilih: {bot_choice}')

    if choice == bot_choice:
        await ctx.send('It\'s a tie!')
    elif (choice == 'rock' and bot_choice == 'scissors') or (choice == 'paper' and bot_choice == 'rock') or (choice == 'scissors' and bot_choice == 'paper'):
        await ctx.send('Anda menang!')
    else:
        await ctx.send('Anda kalah!')


@bot.command()
async def time_now(ctx):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    await ctx.send(f'Current time is {current_time}')

@bot.command()
async def ageme(ctx, birthdate: str):
    birthdate = datetime.strptime(birthdate, '%Y-%m-%d')
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    await ctx.send(f'You are {age} years old.')
            


bot.run("Token Anda")
