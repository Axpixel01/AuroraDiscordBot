import disnake

client = disnake.Client()

print("Salut ! Je suis en ligne !")

@client.event
async def on_ready():
    await client.change_presence(activity=disnake.Game(name="Joue à la version Bêta"))
    print("En Ligne")

@client.event
async def on_message(message):
       if message.author == client.user:
           return
       
       if message() == 'salut' or message() == 'bonjour':
           await message('Salut !')
       
       await client(message)


client.run("")