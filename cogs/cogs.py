from discord.ext import commands
import traceback
import datetime
import discord
import logger
import env
from PIL import Image
from claptcha import Claptcha
import random
import string
import asyncio
from discord import Spotify
import requests




class Cogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

    
    
    @commands.group(name='reload', hidden=True, invoke_without_command=True)
    @commands.is_owner()
    async def _reload(self, ctx, *, module=""):
      extensions = env.extensions
      embed2 = discord.Embed(title=f"Reloading Cog(s)..")
      m = await ctx.send(embed=embed2)
      if module=="":
        try:
            for ext in extensions:
              self.bot.reload_extension(ext)
        except commands.ExtensionError as e:
            embed2 = discord.Embed(title=f'{e.__class__.__name__}: {e}')
            await m.edit(embed=embed2)
        else:
            embed2 = discord.Embed(title=f"Reloaded all cogs")
            await m.edit(embed=embed2)
      else:
        try:
            self.bot.reload_extension(module)
        except commands.ExtensionError as e:
            embed2 = discord.Embed(title=f'{e.__class__.__name__}: {e}')
            await m.edit(embed=embed2)
        else:
            embed2 = discord.Embed(title=f"Cog reloaded")
            await m.edit(embed=embed2)


           


    
def setup(bot):
    try:    
        bot.add_cog(Cogs(bot))
        print("Loaded cogs.py")
    except Exception as e:
        print(f"Error loading cogs.py: {e}")