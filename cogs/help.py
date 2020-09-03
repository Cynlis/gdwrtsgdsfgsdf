from discord.ext import commands
import traceback
import datetime
import discord
import logger

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def help(self, ctx, *, command=""):
      if command == "":
        embed = discord.Embed(title=f'Help Command', description=f"`Lockdown` bot is a useful bot you can use anywhere, commands are below!", colour=0x363940)
        embed.add_field(name='**Lockdown**', value=f"Locks down the channel the command was used inside.", inline=False)
        embed.add_field(name='**Ping**', value=f"Gets the bots latency.", inline=False)
        embed.set_thumbnail(url=self.bot.user.avatar_url)

        await ctx.send(embed=embed)
        return
      if command == "lockdown" or command == "Lockdown" or command == "lock" or command == "Lock":
        embed = discord.Embed(title=f'', description=f"", colour=0x363940)
        embed.add_field(name='**Lockdown**', value=f"Locks down the channel the command was used inside.", inline=False)
        embed.add_field(name='Aliases:', value=f"`lock`", inline=False)

        await ctx.send(embed=embed)
        return
      if command == "Ping" or command == "ping":
        embed = discord.Embed(title=f'', description=f"", colour=0x363940)
        embed.add_field(name='**Ping**', value=f"Gets the bots latency.", inline=False)
        embed.add_field(name='Aliases:', value=f"NONE", inline=False)


        await ctx.send(embed=embed)
        return
      else:  
        embed = discord.Embed(title=f'Help Command', description=f"`Lockdown` bot is a useful bot you can use anywhere, commands are below!", colour=0x363940)
        embed.add_field(name='**Lockdown**', value=f"Locks down the channel the command was used inside.", inline=False)
        embed.add_field(name='**Ping**', value=f"Gets the bots latency.", inline=False)
        embed.set_thumbnail(url=self.bot.user.avatar_url)

        await ctx.send(embed=embed)
        return



    
    

def setup(bot):
    try:    
        bot.add_cog(Help(bot))
        print("Loaded help.py")
    except Exception as e:
        print(f"Error loading help.py: {e}")