final_states = [1,2,3,4,6,8,9]

transitions = [{'+': 3, '-': 3, '*': 3, '/': 9, '(': 3, ')': 3, ':': 7, '.' :5},#0
               {},#1
               {'.': 6},#2
               {},#3
               {},#4
               {},#5
               {},#6
               {'=':8},#7
               {},#8
               {'*': 10,'/':11},#9
               {'*':13},#10
               {'\n' : 0, ' ': 11, '\t': 11},#11
               {},#12
               {'/': 0, '*':13},#13
               {}]

for d in '0123456789':
    transitions[0][d] = 2
    transitions[1][d] = 4
    transitions[2][d] = 2
    transitions[4][d] = 4
    transitions[5][d] = 6
    transitions[6][d] = 6
    transitions[10][d]=10
    transitions[11][d]=11
    transitions[13][d]=10

for l in 'abcdefghijklmnopqrstuvwxyz':
    transitions[0][l]=1
    transitions[1][l]=4
    transitions[4][l]=4
    transitions[10][l] = 10
    transitions[11][l] = 11
    transitions[13][l]= 10

for c in ' \t\n':
    transitions[0][c] = 0
    transitions[13][c]=10
    transitions[10][c]=10

for h in ' -+=:()/':
    transitions[10][h]=10
    transitions[11][h]=11
for h in ' -+=:()':
    transitions[13][h]=10

def scan(program):
    tokens = []
    current_token = ''
    state = 0
    for c in program + '\n':
        if c in transitions[state]:
            current_token += c
            state = transitions[state][c]
        elif state in final_states:
            tokens += [current_token]
            current_token = c
            state = transitions[0][c]
        else:
            print('ERROR: ' + current_token + c)
            return tokens
        if state == 0:
            current_token = ''
    if state in final_states:
        tokens += [current_token]
    # else:
    #     print('ERROR: '+ current_token+c + ' invalid token spanned to end of program')
    return tokens



with open('test1.numbers') as f:
    print(scan(f.read()))