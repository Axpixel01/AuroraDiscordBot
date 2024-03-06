import disnake

bot = disnake.Client()

@bot.event
async def on_ready():
    await bot.change_presence(activity=disnake.Game(name="Joue à la version **Bêta**"))
    print("En Ligne")

from pypresence import Presence
import time

client_id = "1214918767537160212"
RPC = Presence(client_id)
RPC.connect()

RPC.update(
    state="Bienvenue sur le tuto de GCA",
    large_image="python",
    buttons=[{"label": "Discord GCA", "url": "https://discord.gg/gca"}],
    details="J'ai désormais un profil personnaliser",
)

while True:
    time.sleep(15)

@bot.event
async def on_message(ctx):
    if ctx.author == ctx.author.bot:
        return
    
    if ctx.content.startswith("salut" or "bonjour"):
        await ctx.channel.send("Salut !")

bot.run("")