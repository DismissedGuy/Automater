"""
All commands for the bot.
"""

from discord.ext import commands


class InfoCommandsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def setup(self, ctx):
        await ctx.send('<enter form URL here>')


def setup(bot):
    bot.add_cog(InfoCommandsCog(bot))