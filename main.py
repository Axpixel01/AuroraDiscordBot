import disnake

bot = disnake.Client()

@bot.event
async def on_ready():
    await bot.change_presence(activity=disnake.Game(name="Joue à la version Bêta"))
    print("En Ligne")



@bot.event
async def on_message(ctx):
    if ctx.author == ctx.author.bot:
        return
    
    if ctx.content.startswith("salut" or "bonjour"):
        await ctx.channel.send("Salut !")
    
@bot.event
async def on_message(ctx):
    if ctx.author == ctx.author.bot:
        return
    
    import random

    nombre = random.randint(1, 100)
    
    if ctx.content.startswith("?roll"):
        await ctx.channel.send(nombre)
 
bot.run("")