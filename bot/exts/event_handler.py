"""
Handles incoming websocket events, parses actions and executes actions in order to automate your server!
This is where the fancy stuff happens ;)
"""

import util
from discord.ext import commands
from util import safe_objects


class EventHandlerCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.actions = util.ConfigFile('macros/actions.json', config_type='json')
        self.events = util.ConfigFile('macros/events.json', config_type='json')

    @commands.Cog.listener()
    async def on_socket_response(self, msg):
        if msg.get('t') not in self.events.keys():
            return

        guild_id = msg.get('d').get('guild_id')
        print(guild_id)
        macros = await self.bot.db.get_guild_macros(guild_id)
        print(macros)

        for m in macros:
            event = getattr(safe_objects, self.events.get(m['event'].upper()))
            action = self.actions.get(m['action'])

            whitelist = {name: obj(**msg.get('d')) for (name, obj) in event.items()}

            parser = util.SafeInputParser(m['condition'], whitelist)
            if not parser.valid:
                continue
            do_apply = parser.parse()
            if not do_apply:
                continue

            try:
                parsed_args = {k: util.SafeInputParser(v, whitelist).parse()
                               for (k, v) in m['args'].items()}
            except Exception:
                # malformed action argument
                continue

            method = getattr(self.bot.http, action.get('method'))
            await method(**parsed_args)


def setup(bot):
    bot.add_cog(EventHandlerCog(bot))
