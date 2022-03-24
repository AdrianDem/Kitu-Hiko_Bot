import discord
from discord.ext import commands
from config import settings
bot = commands.Bot (command_prefix = settings ['prefix']);

client = discord.Client()
@bot.command()
async def helping(ctx):
    await ctx.send(f'!embrace, !info, !cookies, поцелуи: !kisscheek - поцелуй в шеку, !kiss - поцелуй губы')

@bot.command()
async def info(ctx):
    await ctx.send(f'{ctx.author.mention} автор бота Adrian_Demoner')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)

@bot.command()
async def embrace(ctx, member: discord.Member = None):

    if member == None:
        return

    await ctx.channel.send(f"{ctx.author.mention} обнял {member.mention}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)

@bot.command()
async def cookies(ctx, member: discord.Member = None):

    if member == None:
        return

    await ctx.channel.send(f"{ctx.author.mention} выдал печенье {member.mention}")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)

@bot.command()
async def kisscheek(ctx, member: discord.Member = None):

    if member == None:
        return

    await ctx.channel.send(f"{ctx.author.mention} поцеловал в шеку {member.mention}")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)

@bot.command()
async def kiss(ctx, member: discord.Member = None):

    if member == None:
        return

    await ctx.channel.send(f"{ctx.author.mention} поцеловал {member.mention}")

    #command на отправку гифок, картинок, и поиск манг
    #вызов команды из под JS
    #Код для создания постов о начале стримов и выхода видео


bot.run(settings['token'])
