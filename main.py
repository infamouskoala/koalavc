import discord
from discord.ext import commands
import os
os.system("pip install pynacl")
from src.keep_alive.keep_alive import keep_alive
    
green = "\033[1;32m"
white = "\033[1;37m"
yellow = "\033[1;33m"  
purple = "\033[1;35m"  
os.system("cls || clear")

koala = commands.Bot(command_prefix="--DO--NOT--CHANGE--THIS--OR--ACCOUNT--BAN--", self_bot=True)
print(f"""{purple}                  _              ___ 
  /\ /\___   __ _| | __ _/\   /\/ __|
 / //_/ _ \ / _` | |/ _` \ \ / / /   
/ __ \ (_) | (_| | | (_| |\ V / /___ 
\/  \/\___/ \__,_|_|\__,_| \_/\____/ 
$$$ Win last to leave like nothing $$${white}
""")
pth = 'src\\stolen.txt'
file = open(pth,"w")
file.write("If this software was sold to you, I am sad to tell you that you have been robbed :( this is free on my github. Welp here are my socials and I am the real developer of this.\nhttps://youtube.com/infamouskoala\nhttps://github.com/infamouskoala")
file.close()
token = input("Enter User token: ")
channelID = int(input("Enter voice channel ID: "))
#mute_input = input("Mute [true/false]: ")
#mute = mute_input.upper()
#def_input = input("Deaf [true/false]:")
#deaf = def_input.upper()

@koala.event
async def on_message(message):
  if message.content == "hi":
      print(f"{purple}[MESSAGE]{white} You got a message from {message.author}")

@koala.event
async def on_ready():
    try:
        voice_channel = koala.get_channel(channelID)
        if voice_channel:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{green}[+]{white} Logged in as {koala.user}")
            await voice_channel.connect()
            print(f"{green}[+]{white} Joined the voice channel")
        else:
            print(f"{yellow}[!]{white} Voice channel not found")
    except Exception as e:
        print(f"{yellow}[!]{white} Error: {e}")

try:
  koala.run(token, bot=False)
except:
  print(f"{yellow}[!]{white} Couldn't run the bot, try validating the usertoken and the IDs and retry or contact support.")
