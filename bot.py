import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)  # BOT PREFIX

#mute
@bot.event
async def on_ready():
    print(f'Бот {bot.user.name} запущен! | Developed By SnezOK419')

@bot.command()
async def mute(ctx, member: discord.Member):
    await member.add_roles(discord.utils.get(ctx.guild.roles, name='Muted'))
    await ctx.send(f'{member.mention} был замучен')

@bot.command()
async def unmute(ctx, member: discord.Member):
    await member.remove_roles(discord.utils.get(ctx.guild.roles, name='Muted'))
    await ctx.send(f'{member.mention} был размучен')

#ban
@bot.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} был забанен')

@bot.command()
async def unban(ctx, member: discord.Member):
    await member.unban()
    await ctx.send(f'{member.mention} был разбанен')

#warn
@bot.command()
async def warn(ctx, member: discord.Member, *, reason="Не указана"):
    embed = discord.Embed(title="Предупреждение", color=0xFF0000)
    embed.add_field(name="Участник", value=member.mention)
    embed.add_field(name="Модератор", value=ctx.author.mention)
    embed.add_field(name="Причина", value=reason)
    
    await ctx.send(embed=embed)
    
    log_channel = discord.utils.get(ctx.guild.text_channels, name="предупреждения")
    if log_channel:
        await log_channel.send(embed=embed)
    else:
        await ctx.send("Канал для логов предупреждений не найден")

#ping
@bot.command()
async def ping(ctx):
    latency = bot.latency * 1000
    await ctx.send(f'Мой текущий пинг составляет {latency:.2f} мс')

#run(впишите свой токен)
bot.run('TOKEN')