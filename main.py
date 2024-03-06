import disnake

bot = disnake.Client()

@bot.event
async def on_ready():
    await bot.change_presence(activity=disnake.Game(name="Joue à la version **Bêta**"))
    print("En Ligne")

@bot.event
async def on_message(ctx):


    if ctx.content.startswith("salut"):
        await ctx.send("Salut !")
    
bot.run("MTIxNDkxODc2NzUzNzE2MDIxMg.GvL6JG.1g8-5ff7UaCi79mzfWCayUHM5t_aP9OmoTyhP4")