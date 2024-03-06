import disnake

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
>>>>>>> 3aec99283d11de8e7bc4b98d1cb310f3c39a0e33
