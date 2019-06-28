"""
Backend that will handle the form's OAUTH2 flow.
TODO: oauth flow, data verification. in heavy development
"""

from aiohttp import web
from discord.ext import commands

routes = web.RouteTableDef()


class BackendServer(commands.Cog):
    def __init__(self, bot, *args, **kwargs):
        self.bot = bot
        self.app = web.Application(*args, **kwargs)

    @routes.post('/submit')
    async def submit(self, request):
        data = request.post()
        await self.bot.db.add_guild_macro(data['server_id'], data['event'],
                                          data['condition'], data['action'],
                                          data['args'])

        return web.Response(text='Success!')


def setup(bot):
    cog = BackendServer(bot)
    bot.add_cog(cog)

    # NEEDS EVENT LOOP FIXING!
    # cog.app.add_routes(routes)
    # web.run_app(cog.app, host='0.0.0.0', port=4343)
