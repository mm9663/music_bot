import discord
import sys
import random
import asyncio
import glob
import copy

client = discord.Client()

def read_token():
    token = ''
    try:
        token_file = open('../key/token', 'r')
        token = token_file.read().replace('\n','')
    except:
        print('failed to find or read token file. check your token file')
    finally:
        return token

def read_active_channel_id():
    channel_id = -1
    try:
        channel_id_file = open('../key/channel_id', 'r')
        channel_id = int(channel_id_file.read())
    except:
        print('failed to find or read channel id file. check your channel id file')
    finally:
        return channel_id

def read_active_vc_id():
    channel_id = -1
    try:
        channel_id_file = open('../key/voice_id', 'r')
        channel_id = int(channel_id_file.read())
    except:
        print('failed to find or read channel id file. check your channel id file')
    finally:
        return channel_id

def make_playlist():
    ls = glob.glob("../playlist/*.mp[34]")
    return random.sample(ls,len(ls))

def nextsong(error):
    global pos
    pos += 1
    if pos >= len(playlist):
        pos = 0
    player = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(playlist[pos]), volume)
    voice.play(player,after=nextsong)
    return
# init
token = read_token()
active_channel_id = read_active_channel_id()
active_vc_id = read_active_vc_id()
playlist = make_playlist()


# bot を終了するコマンド
async def run_quit(message):
    await message.channel.send('botを終了しました。')
    sys.exit()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

voice = 0
volume = 0.015
pos = 0


@client.event
async def on_message(message):
    global voice
    global volume
    global pos
    global playlist
    print("nanika")
    if message.author == client.user:
        return
    if message.channel.id != active_channel_id:
        return

    # コマンドのパース
    print(message.content)
    cmd_list = list(filter(lambda x: len(x) > 0, message.content.split(' ')))
    if len(cmd_list) == 1:
        cmd = cmd_list[0]
        if cmd == '?join':
            voice = await client.get_channel(active_vc_id).connect()
        if cmd == '?jaana':
            voice.disconnect()
        if cmd == '?play':
            #player = discord.FFmpegPCMAudio(playlist[random.randint(0, len(playlist)-1)])
            pos = 0
            await message.channel.send(playlist)
            player = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(playlist[pos]), volume)
            voice.play(player,after=nextsong)
        if cmd == '?next':
            if voice.is_playing():
                voice.stop()
            nextsong(None)
        if cmd == '?shuffle':
            pos = -1
            playlist = random.sample(playlist,len(playlist))
            
            await message.channel.send(playlist)
            nextsong(None)
        if cmd == '?help':
            await message.channel.send("mada naiyo")
        if cmd == '?stop':
            voice.stop()
    
    if len(cmd_list) == 2:
        cmd = cmd_list[0]
        if cmd == '?volume':
            if cmd_list[1] == 'down':
                volume -= 0.001
            if cmd_list[1] == 'up':
                volume += 0.001
            if cmd_list[1] == 'ddown':
                volume -= 0.01
            if cmd_list[1] == 'uup':
                volume += 0.01

client.run(token)
