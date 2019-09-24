import discord
from discord.ext import commands
import asyncio
import random
import requests
import openpyxl
from json import loads




client = discord.Client()

@client.event
async def on_ready():
    print(client.user.name)
    print("ready")
    game = discord.Game("업데이트 완료")
    await client.change_presence(status=discord.Status.online, activity=game)
    twitch = "dq12345"
    name = "알티갓"
    channel = client.get_channel(625633655477370890)
    a = 0
    while True:
        headers = {'Client-ID': 'd3w46tya3886tar4s31enx8f9ya91p'}
        response = requests.get("https://api.twitch.tv/helix/streams?user_login=" + twitch, headers=headers)
        try:
            if loads(response.text)['data'][0]['type'] == 'live' and a == 0:
                await channel.send("```" + name + " 님이 망하지않고 또다시 방송을 시작하였습니다." + "```")
                a = 1
        except:
            a = 0
        await asyncio.sleep(3)

    twitch2 = "mochapoo"
    name2 = "모카푸여왕님"
    channel = client.get_channel(625633655477370890)
    a = 0
    while True:
        headers = {'Client ID': 'v2n7lbn2edlcaylh0qzcjtrhwws025'}
        response = requests.get("https://api.twitch.tv/helix/streams?user_login=" + twitch2, headers=headers)
        try:
            if loads(response.text)['data'][0]['type'] == 'live' and a == 0:
                await channel.send("```" + name2 + " 이 방송을 시작하였습니다." + "```")
                a = 1
        except:
            a = 0
        await asyncio.sleep(3)

@client.event
async def on_message(message):
    global msg
    if message.content.startswith('!안녕'):
        await message.channel.send("```안녕하세요```")

    if message.content.startswith('!햄쑤'):
        await message.channel.send("```아마도 그는 감자라고 인식 되는것 같습니다.```")

    if message.content.startswith('!룰루'):
        await message.channel.send("```아마도 그는 꼰대라고 인식 되는것 같습니다.```")

    if message.content.startswith('!슈퍼키드'):
        await message.channel.send("```모카푸꺼```")

    if message.content.startswith('!모카푸'):
        await message.channel.send("```슈퍼키드꺼```")

    if message.content.startswith('!나잌키'):
        await message.channel.send("```아마도 그는 바보라고 인식 되는것 같습니다.```")

    if message.content.startswith('!볼란테'):
        await message.channel.send("```보~르란~떼르!```")

    if message.content.startswith('!명령어'):
        file = open("명령어.txt")
        await message.channel.send("```" + file.read() + "```")
        file.close()

    if message.content.startswith("!팀나누기"):
        team = message.content[6:]
        peopleteam = team.split(" / ")
        people = peopleteam[0]
        team = peopleteam[1]
        person = people.split(" ")
        teamname = team.split(" ")
        random.shuffle(teamname)
        for i in range(0, len(person)):
            await message.channel.send("```" + person[i] + "->" + teamname[i] + "```\n" )

    if message.content.startswith("!서버"):
        file = open("서버.txt")
        await message.channel.send("```" + file.read() + "```")
        file.close()

    if message.content.startswith("!데모"):
        file = open("데모.txt")
        await message.channel.send("```" + file.read() + "```")
        file.close()

    list = ['de_dust2', 'de_inferno', 'de_nuke', 'de_overpass', 'de_train', 'de_vertigo', 'de_mirage', 'de_cache']
    menu = random.choice(list)
    #   print(menu)
    if message.content.startswith("!map"):
        await message.channel.send("```" + menu + "```")

    if message.content.startswith("!골라"):
        choice = message.content.split(" ")
        choicenumber = random.randint(1, len(choice) - 1)
        choiceresult = choice[choicenumber]
        await message.channel.send("```" + choiceresult + "```")

client.run('NTc5NjgxMDI2Njc5MzczODI0.XYkjZA.cFiZwPYjyvleiom--aJU3RV-dzE')

