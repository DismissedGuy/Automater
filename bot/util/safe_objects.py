"""
A couple of objects to replace discord.py's (like Guild, Member, TextChannel, etc)
Intended to be used by the parser in order to restrict access to potentially sensitive methods.
"""


class SafeObjectBase:
    def __init_(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


class SafeMember(SafeObjectBase):
    pass


class SafeGuild(SafeObjectBase):
    pass


class SafeTextChannel(SafeObjectBase):
    pass
