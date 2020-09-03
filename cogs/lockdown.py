from discord.ext import commands
import traceback
import datetime
import discord
import logger

class Lockdown(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=["lock"])
    @commands.guild_only()
    @commands.has_guild_permissions(manage_channels=True)
    @commands.bot_has_guild_permissions(manage_channels=True)
    async def lockdown(self, ctx, channel: discord.TextChannel=None):
        channel = channel or ctx.channel

        if ctx.guild.default_role not in channel.overwrites:
            overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(send_messages=False)
            }
            await channel.edit(overwrites=overwrites)

            embed = discord.Embed(title=f"🔒  I have put `{channel.name}` on lockdown", description=f"Type `{ctx.prefix}lock` again to remove lockdown", colour=0x363940)
            await ctx.send(embed=embed)
        elif channel.overwrites[ctx.guild.default_role].send_messages == True or channel.overwrites[ctx.guild.default_role].send_messages == None:
            overwrites = channel.overwrites[ctx.guild.default_role]
            overwrites.send_messages = False
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrites)

            embed = discord.Embed(title=f"🔒  I have put `{channel.name}` on lockdown", description=f"Type `{ctx.prefix}lock` again to remove lockdown", colour=0x363940)
            await ctx.send(embed=embed)
        else:
            overwrites = channel.overwrites[ctx.guild.default_role]
            overwrites.send_messages = True

            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrites)
            embed = discord.Embed(title=f"🔓  I have removed `{channel.name}` from lockdown", description=f"Type `{ctx.prefix}lock` again to add lockdown", colour=0x363940)
            await ctx.send(embed=embed)

    
    

def setup(bot):
    try:    
        bot.add_cog(Lockdown(bot))
        print("Loaded lockdown.py")
    except Exception as e:
        print(f"Error loading lockdown.py: {e}")