import discord
import discord_token as t
import response as res

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    
@client.event
async def on_message(message):

    if message.content == "exit" or message.content == "e":

        await message.channel.send("Good Bye")
        await client.logout()
    
    elif message.content == "random":

        await message.channel.send( res.randomWeapon( message ) )

    elif message.content == "random all":

        await message.channel.send( res.randomWeapon_all( message ) )

    elif message.content == "random vc":

        await message.channel.send( res.randomWeapon_vc( message ) )

    elif   message.content == "試合順" or message.content == "order":

        await message.channel.send( res.gameOrder() )
            
    elif message.content == "help":

        await message.channel.send( res.help() )

    elif message.content.startswith("reg"):
        
        await message.channel.send( res.regPlayer( message ) )

    elif message.content == "show":
        
        await message.channel.send( res.showReg() )

    elif message.content == "makeTeam" or message.content == "チーム":
        
        await message.channel.send( res.makeTeam() )

    elif message.content == "makeTeam t":
        await message.channel.send( res.makeTeam_t() )
    
    elif message.content == "t":
        await message.channel.send( res.test( message ) )

    elif message.content == "hello":
        m = ( "チーム分けとかのボットです\n"
        "よつぎがbotを起動したときしか使えないですがよろしく\n"
        "以下、説明"
        + res.help() ) 
        await message.channel.send(m)
        
client.run( t.token )