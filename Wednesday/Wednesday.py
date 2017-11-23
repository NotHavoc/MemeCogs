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

    async def on_message(self, message):
        """the bots entire functionallity"""
        """
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
        """
        await self.bot.say("It is Wednesday my dudes")

        

