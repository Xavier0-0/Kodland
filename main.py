import discord, random, bcrypt
from discord.ext import commands

intents = discord.Intents.default()

intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print('Bot Gotowy!')
    print(f'zalagowano jako {bot.user.name}')

@bot.command()
async def dodaj(ctx, a:int, b: int):
    await ctx.send(f'{a} + {b} = {a + b}')

@bot.command()
async def hello(ctx, count = 5):
    await ctx.send('Hello!' * count)

@bot.command()
async def password(ctx, length: int):
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    
    all_characters = lowercase + uppercase + numbers

    password = [random.choice(lowercase),
                random.choice(uppercase),
                random.choice(numbers)]
    
    while len(password) < length:
        next_char = random.choice(all_characters)
        if next_char not in password:
            password.append(next_char)
    
    random.shuffle(password)
    password = ''.join(password)

    hashed = bcrypt.haspw(password.encode(), bcrypt.gensalt())

    await ctx.send(f'Wygenerowne haslo: {password}, {hashed}')

@bot.command()
async def roll(ctx, dice: str):
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return
    result = ', '.join(str(random.randint(1, limit))for r in range(rolls))
    await ctx.send(result)

@bot.command()
async def addition(ctx, *numbers: int):
    await ctx.send(sum(numbers))

@bot.command()
async def repeat(ctx, times: int, content='repeating....'):
    for i in range(times):
        await ctx.send(content)
   


bot.run('MTI2NjQzMjk2NjI0NzE5MDUzOQ.GCf4tM.zv0DEFYFtLDvktmJZI-CIZFOog1A_JV_zXxt_Q')


