import discord
import datetime
import os
import asyncio
import re
from discord.ext import commands

__author__ = "Havoc"

class GenericError(Exception):
    pass

class Wednesday:

    def __init__(self, bot):
        self.bot = bot
        self.tiggered = false

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

        if weekday != 3
            self.tiggered = false
            return

        if tiggered == true
            return

        await self.bot.say("It is Wednesday my dudes")

        

