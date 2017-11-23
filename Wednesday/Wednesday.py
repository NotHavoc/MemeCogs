import discord
import requests
from discord.ext import commands

class Wednesday:
    """Cog for searching Hearthstone cards"""
        
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def card(self, name):
        """Searches for a regular Hearthstone card"""

        r = requests.get('https://omgvamp-hearthstone-v1.p.mashape.com/cards/{}'.format(name), headers={'X-Mashape-Key':'sly1A6Ur3tmshrDtRbWe4q738Afxp1cnkhajsnWqVf9HMJ7ZOJ'}) 
        
        await self.bot.say(r.json()[0]['img'])
        await self.bot.say(r.json()[0]['flavor'])

    @commands.command()
    async def gcard(self, name):
        """Searches for a gold Hearthstone card"""

        r = requests.get('https://omgvamp-hearthstone-v1.p.mashape.com/cards/{}'.format(name), headers={'X-Mashape-Key':'sly1A6Ur3tmshrDtRbWe4q738Afxp1cnkhajsnWqVf9HMJ7ZOJ'}) 
        
        await self.bot.say(r.json()[0]['imgGold'])
        await self.bot.say(r.json()[0]['flavor'])

def setup(bot):
    bot.add_cog(Hearthstone(bot))

"""
import discord
import datetime
import os
import asyncio
import re
from discord.ext import commands
from cogs.utils import checks
from cogs.utils.dataIO import dataIO
from cogs.utils.chat_formatting import box, pagify, escape_mass_mentions
from random import choice

class Wednesday:
    """Cog to notify the server when it is wednesday"""

    def __init__(self, bot):
        self.bot = bot
        self.tiggered = false

    @commands.command()
    async def card(self, name):
        """Searches for a regular Hearthstone card"""

        r = requests.get('https://omgvamp-hearthstone-v1.p.mashape.com/cards/{}'.format(name), headers={'X-Mashape-Key':'sly1A6Ur3tmshrDtRbWe4q738Afxp1cnkhajsnWqVf9HMJ7ZOJ'}) 
        
        await self.bot.say(r.json()[0]['img'])
        await self.bot.say(r.json()[0]['flavor'])    
        
    async def on_message(self, message):
        
        channel = message.channel
        author = message.author
        weekday = datetime.now().isoweekday()

        if message.server is None:
            return

        if author == self.bot.user:
            return

        if not self.bot.user_allowed(message):
            return

        if self.is_command(message):
            return

        if weekday != 4
            self.tiggered = false
            return

        if tiggered == true
            return
       
        await self.bot.say("It is Wednesday my dudes")

    def setup(bot):
        bot.add_cog(Wednesday(bot))

