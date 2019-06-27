import logging
import os

import util
from discord.ext import commands

logging.basicConfig(level=logging.INFO)


class AutomaterBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        self.config = util.ConfigFile('config.yml', config_type='yaml')

        prefix = kwargs.get('command_prefix', self.config['prefix'])

        super().__init__(*args, **kwargs, command_prefix=prefix)

        self.loop.run_until_complete(self.load_extensions())

    async def on_ready(self):
        print('---------- Automater v1.0 ----------')
        print(f'Guilds:        {len(self.guilds)}')
        print(f'Loaded Users:  {len(self.users)}')
        print('------------------------------------')

    @property
    def all_extensions(self):
        for f in os.listdir('exts'):
            if f.startswith('_'):
                continue
            yield 'exts.' + f.rstrip('.py')

    async def load_extensions(self):
        extensions = list(self.all_extensions)

        self.load_extension('jishaku')  # debugging for owner
        for ext in extensions:
            try:
                self.load_extension(ext)
            except commands.NoEntryPointError:
                logging.warning(f'Ignoring extension {ext}: no setup.')


if __name__ == '__main__':
    bot = AutomaterBot()
    bot.run(bot.config['token'])
