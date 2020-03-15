import os
from dotenv import load_dotenv
import random
import discord
from discord.ext import commands

def read_file(filename):
    f = open(filename, "r", encoding="utf-8")
    lines = f.readlines()
    return lines

ships = read_file("ships.txt")
characters = read_file("characters.txt")
tropes = read_file("tropes.txt")
greetings = ["Howdy partner 🤠.", "Hey sexy thang.", "Heyo!", "So you say that you're struggling with some inspiration...",
                "Boy have I got some inspo for you.", "What's kickin', little chicken?", "Sup, homeslice?"]

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
bot = commands.Bot(command_prefix='!')

@bot.command(name='99')
async def on_message(message):
    brooklyn_99_quotes = [
    'The English language cannot fully capture the depth and complexity of my thoughts, so I\'m incorporating emojis into my speech to better express myself. Winky face.',
    'I\'m the human form of the 💯 emoji.',
    'A place where everybody knows your name is hell. You\'re describing hell.',
    'If I die, turn my tweets into a book.',
    'Great, I\'d like your $8-est bottle of wine, please.',
    'Captain Wuntch. Good to see you. But if you\'re here, who\'s guarding Hades?',
    'I\'m playing Kwazy Cupcakes, I\'m hydrated as hell, and I\'m listening to Sheryl Crow. I\'ve got my own party going on.',
    'Captain, turn your greatest weakness into your greatest strength. Like Paris Hilton RE: her sex tape.',
    'Jake, piece of advice: just give up. It\'s the Boyle way. It\s why our family crest is a white flag.',
    'All men are at least 30% attracted to me. My mother cried the day I was born, because she knew she would never be better than me. At any given moment, I\'m thinking about one thing: Richard Dreyfuss hunkered over eating dog food. I feel like I\'m the Paris of people.',
    'Title of your sex tape.',
    'Oh, I\'ve caused a problem. I tihink I am getting a text message. Bloop. Ah, there it is.',
    'Coat! Coat! Jacket! Coat! Is this a police precinct or a Turkish bazaar?',
    'The doctor said all my bleeding was internal. That\'s where the blood is supposed to be!',
    'Noice. SMORT.',
    'All right, fine. If you guys won\'t help me, I guess I\'ll just get myself off. Context. Context was important on that one.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
        'Your butt is the bomb.',
        'Sarge, with all due respect, I am gonna completely ignore everything you just said.',
    ]

    response = random.choice(brooklyn_99_quotes)
    await message.send(response)

@bot.command(name="all")
async def on_message(ctx):
    greeting = random.choice(greetings)
    ship = random.choice(ships)
    character = random.choice(characters)
    trope = random.choice(tropes)

    response = str(greeting)+" Here's a ship: "+str(ship).strip("\n")+", and a character: "+str(character).strip("\n")+", and last but not least, a trope: "+str(trope)
    await ctx.send(response)

@bot.command(name="ship")
async def on_message(ctx):
    greeting = random.choice(greetings)
    ship = random.choice(ships)
    response = str(greeting)+" Here's a ship for ya: "+str(ship)
    await ctx.send(response)

@bot.command(name="character")
async def on_message(ctx):
    greeting = random.choice(greetings)
    character = random.choice(characters)
    response = str(greeting)+" Here's a character for ya: "+str(character)
    await ctx.send(response)

@bot.command(name="trope")
async def on_message(ctx):
    greeting = random.choice(greetings)
    trope = random.choice(tropes)
    response = str(greeting)+" Here's a trope for you: "+str(trope)
    await ctx.send(response)

@bot.command(name="ship-trope")
async def on_message(ctx):
    greeting = random.choice(greetings)
    ship = random.choice(ships)
    trope = random.choice(tropes)
    response = str(greeting)+" Here's a ship: "+str(ship).strip("\n")+", and a trope: "+str(trope)
    await ctx.send(response)

@bot.command(name="character-trope")
async def on_message(ctx):
    greeting = random.choice(greetings)
    character = random.choice(characters)
    trope = random.choice(tropes)
    response = str(greeting)+" Here's a character: "+str(character).strip("\n")+", and a trope: "+str(trope)
    await ctx.send(response)

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="HP Writer Bot", description="For when you're lacking inspiration.")

    embed.add_field(name="Author", value="shreyofsunshine")

    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

    embed.add_field(name="Invite", value="[Invite link]https://discordapp.com/api/oauth2/authorize?client_id=688834532136583178&permissions=337984&scope=bot")

    await ctx.send(embed=embed)

@bot.command(name="crackship")
async def info(ctx):
    character_one = random.choice(characters)
    character_two = random.choice(characters)
    while (character_two == character_one):
        character_two = random.choice(characters)

    response = str(greeting)+" Let's see what you can do with these two: "+str(character_one).strip("\n")+" and "+str(character_two)
    await ctx.send(response)

bot.remove_command('help')
@bot.command()
async def help(ctx):
    embed = discord.Embed(title="HP Writer Bot", description="Ships and tropes!")
    embed.add_field(name="!99", value="Responds with random quote from B99")
    embed.add_field(name="!help", value="Gives this message.")
    embed.add_field(name="!all", value="Gives you a random ship, character, and trope.")
    embed.add_field(name="!ship", value="Gives you a random ship")
    embed.add_field(name="!character", value="Gives you a random character")
    embed.add_field(name="!trope", value="Gives you a random trope")
    embed.add_field(name="!ship-trope", value="Gives you a random ship and trope")
    embed.add_field(name="!character-trope", value="Gives you a random character and trope")
    embed.add_field(name="!crackship", value="Gives you two random characters to use in a crackship. Use at your own caution")
    await ctx.send(embed=embed)

bot.run(TOKEN)
