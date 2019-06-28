"""
All commands for the bot.
"""

import discord
from discord.ext import commands


class InfoCommandsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def setup(self, ctx):
        await ctx.send(f'You can set up your server by adding new macros here:\n'
                       f'{self.bot.config["form_url"]}?server_id={ctx.guild.id}')

    @commands.command()
    async def macros(self, ctx):
        macros = await self.bot.db.get_guild_macros(ctx.guild.id)

        if not macros:
            return await ctx.send(':warning: You don\'t have any macros! Use `.setup` to install some in your server.')

        embed = discord.Embed(title='Macros', color=discord.Color.from_rgb(150, 80, 0))
        for macro in macros:
            action_args = ', '.join([f'{k}={v}' for (k, v) in macro['args'].items()])

            embed.add_field(name=':heavy_minus_sign:', value=f"""
            :white_small_square: Event name:    {macro["event"]}
            :white_small_square: Condition:     {macro["condition"]}
            :white_small_square: Action:        {macro["action"]}
            :white_small_square: Action args:   {action_args}
            """)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(InfoCommandsCog(bot))