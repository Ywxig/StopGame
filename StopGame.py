import requests
from bs4 import BeautifulSoup
import discord
import datetime
from discord.ext import commands
import random

def game1():
    URL = 'https://stopgame.ru/games/Android'
    HEDERS = {
            'User-Agent' : "YOUR USER AGENT"
        }

    response = requests.get(URL, HEDERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('div', class_ = 'item game-summary game-summary-horiz')
    comps = []
    v_l = []

    for item in items:
        comps.append({'link': item.find('a', class_ = '').get('href')})
    for comp in comps:
        v_l.append(comp['link'])
        #l = 'https://rt.pornhub.com' + comp['link']
    #print(v_l)

    j = len(v_l)
    r = random.randint(0, j)
    
    return 'https://stopgame.ru' + v_l[r]
    print('https://stopgame.ru' + v_l[r])

time = ['07:00:00', '09:00:00', '11:00:00',  '13:00:00',  '15:00:00',  '17:00:00', '20:00:00']

bot = commands.Bot(command_prefix='/')

@bot.command()
async def start(ctx):
    await ctx.send(game1())
    while True:
        data = datetime.datetime.today()
        globaltime = data.strftime("%H:%M:%S")
        if globaltime in time:
            await ctx.send(game1())
            await ctx.send('https://www.youtube.com/c/StopGameRuGames')

bot.run('ODg5NTQ5MjgzMjk1MTEzMjk2.YUi3VA.2kQyBoOvPhLjhCRAp_Zm5aXQ7wc')
