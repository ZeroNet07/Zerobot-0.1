import discord
from discord.ext import commands
import random

BOT_TOKEN = 'BOT TOKEN'
CHANNEL_ID = 'CHANNEL ID'

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Hello! Study bot is ready!")
    channel = bot.get_channel(CHANNEL_ID)
    #await channel.send("Hello! bot is ready!")

@bot.command()
async def add(ctx, *arr):
    hasil = 0
    for i in arr:
        hasil += int(i)
    await ctx.send(f"Hasil = {hasil}")

@bot.command()
async def game(ctx):  # Adding a command decorator for the game function
    await ctx.send("Pilih Gunting / Batu / Kertas")

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

bot.run(BOT_TOKEN)
