import ply.lex as lex
import re
import codecs
import os
import sys
from ply.lex import TOKEN


reservadas = [ 'WRITELOG', 'WRITESTR','TAUTO', 'WRITETABLA',
                'CONTRA', 'DECI','WRITEINTRO'
              ]

tokens = reservadas+[ 'AND', 'NOT', 'ENTONCES', 'DOBLEENTONCES', 'ASIGNACION', 'NUMERO', 'ESTERM',
          'ID', 'OR', 'APAR', 'CPAR', 'PCOMA', 'LETRA', 'DIGITO', 'ALFANUMERICO', 'CTEXTO', 'IDENTIFICADOR'
           ]

t_ignore = '\t '
t_AND = r'\*'
t_OR = r'\+'
t_NOT = r'\-'
t_ENTONCES = r'\->'
t_CPAR = r'\)'
t_APAR = r'\('
t_PCOMA = r';'
t_DOBLEENTONCES = r'<->'
t_ASIGNACION  = r'=='
t_TAUTO = r'tauto'
t_DECI = r'deci'
t_WRITELOG = r'writelog'
t_WRITETABLA = r'writetabla'
t_WRITESTR = r'writestr'
t_WRITEINTRO = r'writeintro'
t_CONTRA = r'contra'
t_LETRA = r'[a-zA-Z]'
t_DIGITO = r'[0-9]'
t_NUMERO = r'[0-1]'
t_ALFANUMERICO = r'(' + t_LETRA + r'|' + t_DIGITO + r')'
t_IDENTIFICADOR = r'((' + t_LETRA + r')(' + t_ALFANUMERICO + r')*)'
t_CTEXTO = r'"' + r'([\x20-\x21\x23-\xFE]' + r')*"'
t_ESTERM = r'[\ \t\f\r|\n|\r\n]'

#”([\x20-\x21\x23-\xFE])*”

#r'(' + nondigit + r'(' + digit + r'|' + nondigit + r')*)'

@TOKEN(t_IDENTIFICADOR)
def t_ID(t):
    r'(' + t_IDENTIFICADOR + r')'
    if t.value.upper() in reservadas:
       t.value = t.value.upper()
       t.type = t.value

    return t



def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print ("Lexic error {0}".format(t.value[0]))
    t.lexer.skip(1)

# def buscarFicheros(directorio):
#     ficheros = []
#     numArchivo = ''
#     respuesta = False
#     cont = 1
# #
#     for base, dirs, files in os.walk(directorio):
#         ficheros.append(files)
# #
#     for file in files:
#         print (str(cont)+". " +file)
#         cont = cont+1
# #
#     while respuesta == False:
#         numArchivo = input('\nNumero del test: ')
#         for file in files:
#             if file == files[int (numArchivo)-1]:
#                 respuesta = True
#                 break
#     print ("has escogido \"%s\" \n" %files[int(numArchivo)-1])
#     return files[int(numArchivo)-1]
# #
# #
# directorio = "/Users/Madssimo/Documents/Compiladores/L-0/pruebas/"
# archivo = buscarFicheros(directorio)
# test = directorio+archivo
# fp = codecs.open(test, "r", "utf-8")
# cadena = fp.read()
# fp.close
# #
analizador = lex.lex()
# analizador.input(cadena)
# #
# while True:
#     tok = analizador.token()
#     if not tok : break
#     print (tok)
