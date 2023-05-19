tokens = []
#Dylan, Gabriel, Emily, Caitlyn

def parse(token_stream):
    global tokens
    tokens = token_stream
    tree=program()
    return tree
    print("Parse successful")


def match(expected_type):
    global tokens
    if tokens[0][1] == expected_type:
        t=tokens[0]
        tokens = tokens[1:]  # Consume this token
        return t
    else:
        raise SyntaxError("Parse error at " + str(tokens))


def program():
    if tokens[0][1] in ['id', 'read', 'write', '$$']:
        return ['program', stmt_list(), match('$$')]
    else:
        raise SyntaxError("Parse error at " + str(tokens))


def stmt_list():
    t = tokens[0][1]
    if t in ['id', 'read', 'write']:
        return ['stmt_list', stmt(), stmt_list()]
    elif t == '$$':
        return ['stmt_list', 'E']
    else:
        raise SyntaxError("Parse error at " + str(tokens))


def stmt():
    t = tokens[0][1]
    if t == 'id':
        return['stmt',match('id'),match(':='),expr()]
    elif t == 'read':
        return['stmt', match('read'), match('id')]
    elif t == 'write':
        return ['stmt', match('write'),expr()]
    else:
        raise SyntaxError("Parse error at " + str(tokens))


def expr():
    t = tokens[0][1]
    if t in ['id', '(', 'number']:
        return ['expr',term(),term_tail()]
    else:
        raise SyntaxError("Parse error at " + str(tokens))


def term_tail():
    t = tokens[0][1]
    if t in ['+', '-']:
        return['term_tail',add_op(),term(),term_tail()]
    elif t in [')', 'read', 'write', '$$']:
        return ['term_tail', 'E']
    else:
        raise SyntaxError("Parse error at " + str(tokens))


def term():
    t = tokens[0][1]
    if t in ['id', 'number', '(']:
        return['term', factor(),factor_tail()]
    else:
        raise SyntaxError("Parse error at " + str(tokens))


def factor_tail():
    t = tokens[0][1]
    if t in ['*', '/']:
        return ['factor_tail', mult_op(),factor(),factor_tail()]
    elif t in ['+', '-', ')', 'id', 'read', 'write', '$$']:
        return ['factor_tail','E']
    else:
        raise SyntaxError("Parse error at " + str(tokens))


def factor():
    t = tokens[0][1]
    if t == '(':
        return['factor',match('('), expr(),match(')')]
    elif t == 'id':
        return['factor',match('id')]
    elif t == 'number':
        return['factor',match('number')]
    else:
        raise SyntaxError("Parse error at " + str(tokens))


def add_op():
    t = tokens[0][1]
    if t == '+':
        return ['add_op', match('+')]
    elif t == '-':
        return ['add_op', match('-')]
    else:
        raise SyntaxError("Parse error at " + str(tokens))


def mult_op():
    t = tokens[0][1]
    if t == '*':
        return ['mult-op', match('*')]
    elif t == '/':
        return ['mult-op', match('/')]
    else:
        raise SyntaxError("Parse error at " + str(tokens))

