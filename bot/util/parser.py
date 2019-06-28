"""
An AST parser to parse user-friendly strings into booleans and other values to pass into filters and actions.
Features dot notation on whitelisted objects and restricts access to public methods for security reasons.
"""

import ast
import operator

from util.safe_objects import *

MAX_STR_LEN = 100
ALLOWED_OBJECTS = {
    'author': SafeMember,
    'guild': SafeGuild,
    'channel': SafeTextChannel
}
BIN_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv
}


class UnsupportedNodeException(Exception):
    pass


class ForbiddenObjectException(Exception):
    pass


class ForbiddenHandlingException(Exception):
    pass


class SafeInputParser:
    def __init__(self, string):
        self.string = string

        if len(string) > MAX_STR_LEN:
            raise ValueError(f'String length cannot exceed {MAX_STR_LEN} characters.')

    @property
    def valid(self):
        try:
            self.parse()
            return True
        except:
            return False

    def parse(self):
        node = ast.parse(self.string, mode='eval')
        return self.eval(node.body)

    def eval(self, node):
        if isinstance(node, ast.Expression):
            return self.eval(node.body)
        elif isinstance(node, ast.Str):
            return node.s
        elif isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.BinOp):
            return BIN_OPS[type(node.op)](self.eval(node.left), self.eval(node.right))
        elif isinstance(node, ast.Name):
            if not isinstance(node.ctx, ast.Load):
                raise ForbiddenHandlingException('Only loading variables is allowed.')
            elif not self.is_whitelisted(node.id):
                raise ForbiddenObjectException(f'{node.id} is not whitelisted.')

            return ALLOWED_OBJECTS.get(node.id)()
        elif isinstance(node, ast.Attribute):
            if not isinstance(node.ctx, ast.Load):
                raise ForbiddenHandlingException('Only loading variables is allowed.')
            return getattr(self.eval(node.value), node.attr)
        else:
            raise UnsupportedNodeException(f'Unsupported node: {node}')

    def is_whitelisted(self, value):
        return value in ALLOWED_OBJECTS.keys()
