import discord

client = discord.Client()
#-------------대답---------------
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
#-----------메세지 대답------------------
@client.event
async def on_message(message):
    if message.content.startswith("둘기야"):
        await message.channel.send("구~☆")
    if message.content.startswith("비둘기야"):
        await message.channel.send("구~구~")
    if message.content.startswith("그렇지 둘기야?"):
        await message.channel.send("구!")
    if message.content.startswith("치킨"):
        await message.channel.send("구?! ㅜㅜ")

access_token=os.environ["BOT_TOKEN"]
client.run(access_token)
