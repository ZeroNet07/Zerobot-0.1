import discord
from discord.ext import commands
import random

BOT_TOKEN = '!!BOT TOKEN!!'
CHANNEL_ID = !!CHANNEL ID!!

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    channel = bot.get_channel(CHANNEL_ID)
    #await channel.send("Hello! bot is ready! \U000270A")

@bot.command()
async def add(ctx, *arr):
    hasil = 0
    for i in arr:
        hasil += int(i)
    await ctx.send(f"Hasil = {hasil}")

@bot.command()
async def game(ctx):  #game function
    await ctx.send("Pilih Gunting ✌️ / Batu ✊ / Kertas 🖐️")

    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel and message.content.lower() in ["gunting", "batu", "kertas"]

    user_choice_msg = await bot.wait_for("message", check=check)
    user_choice = user_choice_msg.content.lower()

    gamegbk = ["gunting", "batu", "kertas"]
    bot_choice = random.choice(gamegbk)
    await ctx.send(f"Bot memilih: {bot_choice}")

    if user_choice == bot_choice:
        await ctx.send("Hasil: Seri")
    elif (user_choice == "gunting" and bot_choice == "kertas") or \
         (user_choice == "batu" and bot_choice == "gunting") or \
         (user_choice == "kertas" and bot_choice == "batu"):
        await ctx.send("Hasil: Kamu Menang!")
    else:
        await ctx.send("Hasil: Kamu Kalah!")

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author.mention}!')
    
@bot.command()
async def smile(ctx):
    emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    await ctx.send (random.choice(emodji))

@bot.command()
async def coin(ctx):
    flip = random.randint(0, 2)
    if flip == 0:
        await ctx.send ("HEADS")
    else:
        await ctx.send ("TAILS")

@bot.command()
async def mention_friends(ctx):
    friend_ids = [757436080026026107]  #user IDs

    mentions = ' '.join([f"<@{friend_id}>" for friend_id in friend_ids])

    await ctx.send(f"Hey {mentions}, let's hang out!")
    
bot.run(BOT_TOKEN)
