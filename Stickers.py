import discord
import requests
from bs4 import BeautifulSoup
import random

client = discord.Client()

@client.event
async def on_message(message):
    if str(message.content).startswith("/stick"):
        find = str(message.content).split("/stick ")[-1]
        print(find)
        url = "https://icons8.com/icon/set/"+find
        r = requests.get(url)
        if r.text.count("Nothing Found")>0:
            await client.send_message(message.channel,"Nothing found")
            await client.delete_message(message)
            return
        soup = BeautifulSoup(r.text,"html.parser")
        icon_list = soup.find('div', {'class': 'c-icon-list m-with-name'})
        if icon_list == None:
            await client.send_message(message.channel, "Nothing found")
            await client.delete_message(message)
            return
        icons = []
        for icon in icon_list:
            a = icon.find('img')
            if len(icons)<20 and a!=-1:
                icons.append(str(a.get('src')).replace('50','256'))
        print(icons)
        if icons == []:
            await client.send_message(message.channel, "Nothing found")
            await client.delete_message(message)
            return
        await client.send_message(message.channel,random.choice(icons)+"    from  "+message.author.name)
        await client.delete_message(message)
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
client.run("MzMyODA3OTA2MzE3NTY1OTUz.DEDhVA.Qp-VWzru13riCZV_3rUQHMt-xI8")
