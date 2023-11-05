import discord
import credits
from discord.ext import commands
import random
import asyncio
import os
import requests

print(os.listdir('images'))

token = credits.token
client = discord.Client()



bot = commands.Bot(command_prefix='!')

@bot.command(name='animals')
async def animals():
    print()



@bot.event
async def on_ready():
    print("Я запущен!")
 
@bot.command()
async def mem(ctx):
    with open('images/mem1.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture) 
    
@bot.command(name='help')
async def help(ctx):
    await ctx.send("Команды бота: \n!start\n!dice\n!truthoraction\n!he\n!choose\nСоздатель бота: Illuminati Inc.")

@bot.command(name = "start")
async def start(ctx):
    await ctx.send("Привет, пользователь!")

@bot.command(name="dice")
async def dice(ctx):
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']
 

@bot.command('duck')
async def duck(ctx):
    '''По команде duck вызывает функцию get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command(name = "truthoraction")
async def truthoraction(ctx):
   x = random.randint(1, 2)
   if x == 1:
        await ctx.send("Правда")
   elif x == 2:
        await ctx.send("Действие")

@bot.event
async def on_message(message):
    if message.content == "Привет":
        await message.channel.send("Рад тебя видеть!")    
    if message.content == "Пока":
        await message.channel.send("Досвидания, рад был тебя видеть!") 
        
@bot.command(name="he")
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
    
@bot.command(name="choose")
async def choose(ctx, *choices: str):
    await ctx.send(random.choice(choices))   
  
with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
            
            