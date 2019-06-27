"""
An AST parser to parse user-friendly strings into booleans and other values to pass into filters and actions.
Features dot notation on whitelisted objects and restricts access to public methods for security reasons.
Max string length is 100 characters.
"""