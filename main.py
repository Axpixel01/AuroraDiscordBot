import disnake
from main import bot

bot = disnake.Client()

@bot.event
async def on_ready():
    await bot.change_presence(activity=disnake.Game(name="Joue à la version **Bêta**"))
    print("En Ligne")

@bot.event
async def on_message(ctx):
    if ctx.author == ctx.author.bot:
        return
    
    if ctx.content.startswith("salut" or "bonjour"):
        await ctx.channel.send("Salut !")
    

bot.run("")