import discord
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from discord import TextChannel
import requests
import os
from deep_translator import (GoogleTranslator)
import time
import asyncio
from mutagen.mp3 import MP3
#sesin çalismasi icin "pip install PyNaCl" komutunu kullan

intents = discord.Intents.all()
client = commands.Bot(command_prefix=["!!"], intents=intents)

@client.event
async def on_ready():
    print("Hazir")
    

@client.command(name="name", description="description")
async def slash_command(int: discord.Interaction):    
    await int.response.send_message("command")


import asyncio # To get the exception

@client.command(name="s")
async def s(ctx): # waiting for message here
    await ctx.send(f"**{ctx.author}**, İstediğini yazmak için 15 saniye süren var")

    def check(m: discord.Message):  # m = discord.Message.
        return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id 
    try:
        msg = await client.wait_for('message', check = check, timeout = 15.0)
    except asyncio.TimeoutError: 
        await ctx.send(f"**{ctx.author}**, yazma süren bitti")
        return
    else:
        #await ctx.send(f"**{ctx.author}**, you responded with {msg.content}!")
        
        try:
            try:
                os.remove("ses.mp3")
            except:
                os.remove("ses.wav")
        except:
            ("silinecek ses yok")
        translate = msg.content  

        translate = str(translate)


        translated = GoogleTranslator(source='auto', target='ja').translate(text=translate)


        url = 'https://api.tts.quest/v1/voicevox/?text={}&speaker=20'.format(translated)#13-20

        # A get request to the API
        response = requests.get(url)

        res = response.json()
        #print(res)
        links = res.get("mp3DownloadUrl")
        time.sleep(1)
        try:
            try:
                mfile = res.get("mp3DownloadUrl")
                print(mfile)
                print(type(mfile))
                #urlretrieve(mfile, "ses.mp3")
                os.system(f'youtube-dl {mfile} -o "ses.mp3"')
                
            except:
                mfile = res.get("wavDownloadUrl")
                print(mfile)
                print(type(mfile))
                #urlretrieve(mfile, "ses.wav")
                os.system(f'youtube-dl {mfile} -o "ses.wav"')
        except:
            await ctx.send(f"**{ctx.author}**, Hata!!, Tekrar dene")  
    
    
    
    
    try:
        await ctx.guild.voice_client.disconnect()
    except:
        print("devam") 
    
    
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("Herhangi Bir ses kanalında değilsin!")
    else:
        voice = get(client.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()
            try:
                try:
                    voice.play(FFmpegPCMAudio("ses.mp3"))
                except:
                    voice.play(FFmpegPCMAudio("ses.wav"))
            except:
                    await ctx.send(f"**{ctx.author}**, Hata!!, Tekrar dene") 
        
        
        await ctx.send(f"**{ctx.author}**,\n Ses_dosyası:{links} ")

        try:
            try:
                audio = MP3("ses.mp3")
                print(audio.info.length)
            except:
                audio = MP3("ses.wav")
                print(audio.info.length)
        except:
            await ctx.send(f"**{ctx.author}**, Ses oynatma hatası!!, Tekrar dene")
        return

#client.run("ODMyNjU1MTY4NDQwMjM4MTMx.Gn5p7V.Db_hpVcSPKiz8I7AvQS6VXMZXoxnGa3g_lVLXM")

client.run("MTAxNDI5NDYxNjY2NjgwODQyMA.G_JOR-.yxEBRYIoRRfLShFyG6lp2Hs4W3qDGo3FxjzkPo")
