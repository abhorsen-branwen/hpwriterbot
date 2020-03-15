import os
from dotenv import load_dotenv
import random
import discord
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
bot = commands.Bot(command_prefix='!')

# @bot.event
# async def on_ready():
#     guild = discord.utils.get(bot.guilds, name=GUILD)
#     print(
#         f'{bot.user} has connected to the following guild:\n'
#         f'{guild.name}(id: {guild.id})'
#     )
#
#     members = '\n - '.join([member.name for member in guild.members])
#     print(f'Guild Members:\n - {members}')

@bot.command(name='99', help='Responds with a random quote from Brooklyn 99')
async def on_message(message):
    brooklyn_99_quotes = [
    'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
        'Your butt is the bomb.'
    ]

    response = random.choice(brooklyn_99_quotes)
    await message.send(response)

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="HP Writer Bot", description="For when you're lacking inspiration.")

    embed.add_field(name="Author", value="shreyofsunshine")

    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

    embed.add_field(name="Invite", value="[Invite link]https://discordapp.com/api/oauth2/authorize?client_id=688834532136583178&permissions=337984&scope=bot")

    await ctx.send(embed=embed)


bot.remove_command('help')
@bot.command()
async def help(ctx):
    embed = discord.Embed(title="HP Writer Bot", description="Ships and tropes!")
    embed.add_field(name="!99", value="Responds with random quote from B99")
    embed.add_field(name="!help", value="Gives this message.")

    await ctx.send(embed=embed)

# @client.event
# async def on_error(event, *args, **kwargs):
#     with open('err.log', 'a') as f:
#         if event == 'on_message':
#             f.write(f'Unhandled message: {args[0]}\n')
#         else:
#             raise


bot.run(TOKEN)
