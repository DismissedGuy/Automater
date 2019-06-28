"""
A couple of objects to replace discord.py's (like Guild, Member, TextChannel, etc)
Intended to be used by the parser in order to restrict access to potentially sensitive methods.
"""


class SafeMember:
    pass


class SafeGuild:
    pass


class SafeTextChannel:
    pass
