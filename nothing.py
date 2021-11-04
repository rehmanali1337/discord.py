import discord


user = discord.Client()


@user.event
async def on_ready():
    print('Ready now')
    await user.scrape_members(str(user.guilds[0]), str(user.guilds[0].channels[0]))

token = "OTAyMjYzNDA4OTgyOTA4OTM4.YXb4YQ.k1ZeWccBtD7JPi8lpxrpB5e-bWg"
user.run(token, bot=False)
