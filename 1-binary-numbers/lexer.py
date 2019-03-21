import ply.lex as lex
import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument('inp', type=str, help='Input C file')
# parser.add_argument('--cfg', type=str, dest='cfg', help='Config file for coloring')
# parser.add_argument('--output', type=str, dest='output', help='Output html file')
# args = parser.parse_args()

################################### Create Lexer ################################################

tokens = ['DOT', 'ZERO', 'ONE']

#there are no reserved keywords
t_DOT = r'\.'
t_ZERO = r'0'
t_ONE = r'1'



# tokens = ['ID', 'CONSTANT', 'STRING',  # SCHAR - single character (distinguish with CHAR keywoard)
#          'EQUAL', 'LT', 'GT', 'LTE', 'GTE', 'NE',
#          'ADD', 'SUB', 'MUL', 'DIV', 'MOD',
#          'ANDB', 'ORB', 'NOTB', 'XOR', 'LSHIFT', 'RSHIFT',
#          'ANDL', 'ORL', 'NOTL',
#          'ASSIGN', 'ADD_ASSIGN', 'SUB_ASSIGN', 'MUL_ASSIGN', 'DIV_ASSIGN', 'MOD_ASSIGN',
#          'LSHIFT_ASSIGN', 'RSHIFT_ASSIGN', 'AND_ASSIGN', 'OR_ASSIGN', 'XOR_ASSIGN',
#          'INCR', 'DECR',
#          'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'LBRACKET', 'RBRACKET',
#          'SEMICOLON', 'COMMA', 'QMARK', 'COLON', 'HATCH', 'DOT', 'PTR_OP', 'ELLIPSIS',
#          'COMMENT', 'MLCOMMENT'
# ]
#
# # all 32 keywords of C language
# reserved = { 'auto' : 'AUTO', 'double' : 'DOUBLE', 'int' : 'INT', 'struct' : 'STRUCT',
#              'break' : 'BREAK', 'else' : 'ELSE', 'long' : 'LONG', 'switch' : 'SWITCH',
#              'case' : 'CASE', 'enum' : 'ENUM', 'register' : 'REGISTER', 'typedef' : 'TYPEDEF',
#              'char' : 'CHAR', 'extern' : 'EXTERN', 'return' : 'RETURN', 'union' : 'UNION',
#              'const' : 'CONST', 'float' : 'FLOAT', 'short' : 'SHORT', 'unsigned' : 'UNSIGNED',
#              'continue' : 'CONTINUE','for' : 'FOR', 'signed' : 'SIGNED', 'void' : 'VOID',
#              'default' : 'DEFAULT', 'goto' : 'GOTO', 'sizeof' : 'SIZEOF', 'volatile' : 'VOLATILE',
#              'do' : 'DO', 'if' : 'IF', 'static' : 'STATIC', 'while' : 'WHILE',
# }
#
# tokens += [ val for _, val in reserved.items() ]
#
#
# # one line definitions
# t_ignore = ' \t'
# t_CONSTANT =  r'((([0-9]+(\.[0-9]+)?)|(\.[0-9]+))(E[+-]?[0-9]+)?)|(\'(.|\n)\')'    # all NUMBERs and one letter
# t_EQUAL = r'=='
# t_LT = r'<'
# t_GT = r'>'
# t_LTE = r'<='
# t_GTE = r'>='
# t_NE = r'!='
# t_ADD = r'\+'
# t_SUB = r'-'
# t_MUL = r'\*'
# t_DIV = r'/'
# t_MOD = r'%'
# t_ANDB = r'&'
# t_ORB = r'\|'
# t_NOTB = r'~'
# t_XOR = r'\^'
# t_LSHIFT = r'<<'
# t_RSHIFT = r'>>'
# t_ANDL = r'&&'
# t_ORL = r'\|\|'
# t_NOTL = r'!'
# t_ASSIGN = r'='
# t_ADD_ASSIGN = r'\+='
# t_SUB_ASSIGN = r'-='
# t_MUL_ASSIGN = r'\*='
# t_DIV_ASSIGN = r'/='
# t_MOD_ASSIGN = r'%='
# t_LSHIFT_ASSIGN = r'<<='
# t_RSHIFT_ASSIGN = r'>>='
# t_INCR = r'\+\+'
# t_DECR = r'--'
# t_LPAREN = r'\('
# t_RPAREN = r'\)'
# t_LBRACE = r'\{|<%'
# t_RBRACE = r'\}|>%'
# t_LBRACKET = r'\[|<:'
# t_RBRACKET = r'\]|:>'
# t_SEMICOLON = r';'
# t_COMMA = r','
# t_QMARK = r'\?'
# t_COLON = r':'
# t_HATCH = r'\#'
# t_DOT = r'\.'
# t_PTR_OP = r'->'
# t_ELLIPSIS = r'\.\.\.'
#
# def t_ID(t):
#     r'[a-zA-Z_][a-zA-Z0-9_]*'
#     try:
#         t.type = reserved[t.value.lower()]
#         t.value = t.value.lower() # make lexeme lower if it is a keywoard
#     except KeyError:
#         t.type = 'ID'
#     return t
#
# # C does not allow multiline strings
# def t_STRING(t):
#     r'\"[^"\n]*?\"' # should there be ?
#     t.lexer.lineno += t.value.count('\n') # '\n' count always 0 since C don't allow '\n' in strings
#     return t
#
#
# def t_newline(t):
#     r'\n+'
#     t.lexer.lineno += len(t.value)
#
# # comments only coloured, not returned as token
# def t_COMMENT(t):
#     r'//.*'
#
# # multiline comment
# # as in C, doesn't allow commants like /* asdf "*/" */
# def t_MLCOMMENT(t):
#     r'/\*(.|\n)*?\*/'
#     t.lexer.lineno += t.value.count('\n')
#

# skip 1 character in case of error
def t_error(t):
    print(f'unrecognized token "{t.value}" at line {t.lineno}')
    t.lexer.skip(1)
    return t

lex.lex()

# lexer = lex.lex()
#
# # Test it out
# data = '''2+3'''
#
# # Give the lexer some input
# lexer.input(data)
#
# # Tokenize
# while True:
#      tok = lexer.token()
#      if not tok:
#          break      # No more input
#      print(tok)


######################################################################################################
