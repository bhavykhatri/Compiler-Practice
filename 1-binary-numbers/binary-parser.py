#goal to write semantics anal
import ply.yacc as yacc

#importing lexer information
from lexer import tokens


class Node:
    def __init__(self, name='', children=[]):
        self.name = name
        if children:
            self.children = children
        else:
            self.children = []
    def __str__(self):
        x = f'[{self.name}'
        for c in self.children:
            if(isinstance(c, Node)):
                x += str(c)
            else:
                x += str(c)
        x += ']'
        return x


#grammar rules are defined inside the function_definition
#and should start with p_
#you also have to write semantic rules

#always write readme file so that you know how to run it
#aim:
# 1. Write a dot script for visualization
# 2. Write different programs for different grammars and visulaize them.

#writing a dot script


def p_statement_left_left(p):
    '''statement : left DOT left'''

    p[0] = Node('statement', p[1:])
    p[0].value = p[1].value + p[3].value/p[3].f

    #print(p[2], type(p[2]))
    # print('''expression : expression ADD term''')
    # file.write("\"" + str(p[2]) + "\" -> " + str(p[1]) + ";\n")
    # file.write("\"" + str(p[2]) + "\" -> " + str(p[3]) + ";\n")
    # print("-------------------")

def p_statement_left(p):
    '''statement : left'''

    p[0] = Node('expression', p[1:])
    p[0].value = p[1].value
    # print('''expression : term''')
    # print("-------------------")

def p_left_left_binary(p):
    '''left : left binary'''

    p[0] = Node('term', p[1:])
    p[0].value = 2*p[1].value  + p[2].value
    p[0].f = p[1].f*2
    # print('''term : term MUL factor''')
    # file.write("\"" + str(p[2]) + "\" -> " + str(p[1]) + ";\n")
    # file.write("\"" + str(p[2]) + "\" -> " + str(p[3]) + ";\n")
    # print("-------------------")

def p_left_binary(p):
    '''left : binary'''

    p[0] = Node('binary', p[1:])
    p[0].value = p[1].value
    p[0].f = 2
    # print('''term : factor''')
    # print("-------------------")

def p_binary(p):
    '''binary : ZERO
    | ONE '''

    p[0] = Node('binary', p[1:])
    p[0].value = float(p[1])
    # print('''factor : LPAREN expression RPAREN''')
    # print("-------------------")


#error rules for syntax errors
def p_error(p):
    print("syntax error in input!")

# number nodes to remove duplicates
count = 1
def number_nodes(node):
    global count
    node.num = count
    count += 1
    for c in node.children:
        if isinstance(c, Node):
            number_nodes(c)
    c_list = []
    for x in node.children:
        if isinstance(x, Node):
            c_list += [x]
        else:
            c_list += [(x, count)]
            count += 1
    node.children = c_list

# create dot script from node information
def create_dot_script(node):
    def make_nodes(node):
        y = str(node.num) + f' [label="{node.name}"]\n'
        for c in node.children:
            if isinstance(c, Node):
                y += f'{node.num} -- {c.num}\n'
                y += make_nodes(c)
            else:
                if '"' not in c[0]:
                    y += str(c[1]) + f' [label="{c[0]}"]\n'
                else:
                    y += str(c[1]) + f' [label={c[0]}]\n'    #handling string
                y += f'{node.num} -- {c[1]}\n'
        return y
    sc = 'strict graph G {\n'
    sc += make_nodes(node)
    sc += '}'
    return sc

#building yacc, parser is an object here
parser = yacc.yacc()

s = input('calc>')
result = parser.parse(s)
print(result.value)
number_nodes(result) #number nodes to remove dublicates
with open('graph.dot', 'w') as f:
    f.write(create_dot_script(result))
