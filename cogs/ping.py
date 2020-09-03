from discord.ext import commands
import traceback
import datetime
import discord
import logger

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command(name='ping', description='Shows you my ping to discord\'s servers')
    async def pingcmd(self, ctx):

        latency = round(self.bot.latency * 1000)

        start = round(datetime.datetime.now(datetime.timezone.utc).timestamp() * 1000)

        embed2 = discord.Embed(title=f'Pinging..', colour=0x363940)
        msg = await ctx.send(embed=embed2)

        end = round(datetime.datetime.now(datetime.timezone.utc).timestamp() * 1000)
        elapsed = round(end - start)

        embed = discord.Embed(colour=0x363940)
        embed.set_author(name=f"Roundtime : {elapsed}ms\nHeartbeat : {latency}ms", icon_url=self.bot.user.avatar_url)

        await msg.edit(embed=embed)

def setup(bot):
    try:    
        bot.add_cog(Ping(bot))
        print("Loaded ping.py")
    except Exception as e:
        print(f"Error loading ping.py: {e}")