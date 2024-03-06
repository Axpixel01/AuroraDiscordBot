import os

import disnake

client = disnake.Client()

@client.event
async def on_ready():
    await client.change_presence(activity=disnake.Game(name="Joue à la version Bêta V1"))
    print("En Ligne")

client.run("")