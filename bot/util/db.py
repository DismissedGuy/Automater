"""
A simple MySQL database class.
Features caching and common database operations.
"""

import json
import logging

import aiomysql

logging.getLogger('__main__')


class CachedMysqlDatabase:
    def __init__(self, *args, **kwargs):
        loop = kwargs.get('loop')
        self.conn = loop.run_until_complete(self.connect(*args, **kwargs))

    async def connect(self, *args, **kwargs):
        conn = await aiomysql.connect(*args, **kwargs)

        async with conn.cursor(aiomysql.DictCursor) as cur:
            logging.info('Loading macros from database...')

            await cur.execute('SELECT * FROM macros;')
            self._cache = await cur.fetchall()

        return conn

    async def get_guild_macros(self, guild_id):
        macros = [c for c in self._cache if c.get('serverid') == guild_id]

        return macros

    async def add_guild_macro(self, guild_id, event_name, condition, action, args):
        async with self.conn.cursor() as cur:
            query = """INSERT INTO macros
            (`serverid`, `event`, `condition`, `action`, `args`)
            VALUES (%s, %s, %s, %s, %s)"""
            await cur.execute(query, (guild_id, event_name, condition, action, str(args).replace('\'', '"')))
            await self.conn.commit()

            macro = {'id': cur.lastrowid, 'serverid': guild_id, 'event': event_name,
                     'condition': condition, 'action': action, 'args': args}
            self._cache.append(macro)
