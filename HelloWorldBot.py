import discord
from db import engine, ServerAuths
from sqlalchemy.orm import Session

intents = discord.Intents(messages=True, message_content=True, guilds=True)
client = discord.Client(intents=intents)

"""This is the event that is triggered to check the weather the bot is ready to test or not"""


@client.event
async def on_ready():
    print("test ready")


"""This is the on_message event which is made to fullfil the requirement of interaction with bot when called upon"""


@client.event
async def on_message(message):
    if message.content.startswith("$hellobot"):
        await message.channel.send(f"hello world")


# @client.event
# async def on_member_join(member):
#     HWmessage = f"Hello world, {member.guild}"
#     await member.send(HWmessage)

"""this is the on_guild_join event which is triggered when the bot join a server 
this also contains the database session which is used to collect the token id and the name of the
server joined by the bot which is the commited into the database """


@client.event
async def on_guild_join(guild):
    Info = ServerAuths(id=guild.id, ServerName=guild.name)
    print(type(guild.id))
    print(f"Hello world, {guild.name}, server ID: {guild.id}")
    with Session(engine) as session:
        session.add(Info)
        session.commit()


client.run("MTE4NDY0NjU0MDM1OTM4OTMwOA.GTwP9A.UEq1pKvc56TL8K3JgG_DpCQjvgG-p1V2QLtGXA")
