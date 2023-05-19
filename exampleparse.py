from pprint import pprint
from rede_parser import parse

tokens = [['read', 'read'],
      	['A', 'id'],
      	['read', 'read'],
      	['B', 'id'],
      	['sum', 'id'],
      	[':=', ':='],
      	['A', 'id'],
      	['+', '+'],
      	['B', 'id'],
      	['write', 'write'],
      	['sum', 'id'],
      	['write', 'write'],
      	['sum', 'id'],
      	['/', '/'],
      	['2', 'number'],
      	['$$', '$$']]

pprint(parse(tokens))