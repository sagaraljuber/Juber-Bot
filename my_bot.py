import discord
from discord.ext import commands

#Client ( our bot)
client = commands.Bot(command_prefix='--')

@client.command(name='version')
async def version(context):

    myEmbed = discord.Embed(title="Current Version", description="The bot is in Version 1.0", color=0x00ff00)
    myEmbed.add_field(name='Version Code:', value="v1.0.0", inline=False)
    myEmbed.add_field(name="Date Released:", value="August 18,2021", inline=False)
    myEmbed.set_footer(text="This is a sample footer")
    myEmbed.set_author(name="Juber Sagaral")

    await context.message.channel.send(embed=myEmbed)

#stuff
@client.event
async def on_ready():

    
    general_channel = client.get_channel(876072838463897603)
    await general_channel.send('Hello, World!')

@client.event
async def on_message(message):
    
    if message.content == 'what is the version':
         general_channel = client.get_channel(876072838463897603)
         
         myEmbed = discord.Embed(title="Current Version", description="The bot is in Version 1.0", color=0x00ff00)
         myEmbed.add_field(name='Version Code:', value="v1.0.0", inline=False)
         myEmbed.add_field(name="Date Released:", value="August 18,2021", inline=False)
         myEmbed.set_footer(text="This is a sample footer")
         myEmbed.set_author(name="Juber Sagaral")

         


         await general_channel.send(embed=myEmbed)

    await client.process_commands(message)


#Run the client on the suerver
client.run('ODc2MDczMTQxNDk4MTc1NDk4.YRewsQ.WI30ik612Rv3cnwaFMjFVe_KLuk')


 