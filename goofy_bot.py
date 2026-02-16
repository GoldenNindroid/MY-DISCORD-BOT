from discord import *
from discord.ext import commands
import random


intents = Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="g!", intents=intents)
bot.remove_command("help")

@bot.event
async def on_ready():
    print(f"logged in as {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.send(f"wsp @{ctx.author.name}")

# Tells you how fast the bot is responding
@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")

@bot.command()
async def goober(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/1237217863501086750/1472739428165484747/lil_goofy_goober_guy-transparent.png?ex=6993aaf9&is=69925979&hm=52747b372e4c63225fc2c9abc08ca78d095860bcfaea48f8551f87f9890fde02&")

@bot.command()
async def help(ctx):
    await ctx.send("The Commands so far are:"
    "\ng!help" 
    "\ng!hello"
    "\ng!goober"
    "\ng!poem"
    "\ng!silksong"
    "\ng!awkward"
    "\ng!isthebotworking")

# Random poem
poem_list = ["Roses are red,\n Weapons against me won't prosper,\n With this Sacred Treasure I Summon, \nBig Raga, the Opp Stopper",
             "From childhood's hour I have not been, \nAs others were—I have not seen, \nAs others saw—I could not bring, \nMy passions from a common spring—, \nFrom the same source I have not taken, \nMy sorrow—I could not awaken,\nMy heart to joy at the same tone—,\nAnd all I lov'd—I lov'd alone—,\nThen—in my childhood—in the dawn,\nOf a most stormy life—was drawn,\nFrom ev'ry depth of good and il,\nThe mystery which binds me still—,\nFrom the torrent,\n or the fountai—,\nrom the red cliff of the mountain—,\nrom the sun that 'round me roll'd,\nIn its autumn tint of gold—,\nFrom the lightning in the sky,\nAs it pass'd me flying by—,\nFrom the thunder, \nand the storm—,\nAnd the cloud that took the form,\n(When the rest of Heaven was blue),\nOf a demon in my view—",
             "Throughout Heaven and Earth, I alone am the honored one",
             "As you are walking, down the street, this guy asks you,to hold his violin.\n ,It’s a Stradivarius.\n ,Soon as it fall,nto your hands,you start playing like crazy.\n ,The violin,almost plays itself,Your powerful hands,nearly break the instrument,but the music is gentle and sweet.\n ,You sweep your long... ",
             "Nature’s first green is gold,Her hardest hue to hold.\n Her early leaf’s a flower;But only so an hour.\n Then leaf subsides to leaf.\n  So Eden sank to grief,So dawn goes down to day.\n Nothing gold can stay.\n ",      
             """    Two roads diverged in a yellow wood,
                And sorry I could not travel both.
                I took the one less traveled by,
                And that has made all the difference."""
                """Once upon a midnight dreary,
                While I pondered, weak and weary,
                Over many a quaint and curious,
                Volume of forgotten lore.""",
                """     Do not go gentle into that good night,
                Rage, rage against the dying of the light.""",
                "No cost too great. No mind to think. No will to break. No voice to cry suffering..."]
@bot.command()
async def poem(ctx):
    await ctx.send(random.choice(poem_list))

@bot.command()
async def silksong(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/1237217863501086750/1472737515588026490/Screenshot_2025-10-26_203225.png?ex=6993a931&is=699257b1&hm=1732eee4d4d76c17d2c548d9357d05ce3b904cd8214994d2977dcdc91ebd19d6&")    

@bot.command()
async def awkward(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/1237217863501086750/1472739102225862942/Screenshot_2026-02-07_204436.png?ex=6993aaac&is=6992592c&hm=624ef3d73cb833bad0ead11004ae4cb3467de307e0dc1ef01e6ff83495fd2c2d&")

@bot.command()
async def isthebotworking(ctx):
    await ctx.send("yes")



bot.run("you aint seeing my token lil bro")