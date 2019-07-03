import ply.yacc as yacc
import os
import codecs
import re
from pylex import tokens
from sys import stdin

precedence = (
     ('left', 'WRITESTR'),
     ('left', 'WRITETABLA'),
     ('left', 'WRITELOG'),
     ('left', 'WRITEINTRO'),
     ('left', 'ID'),
     ('left', 'DOBLEENTONCES'),
     ('left', 'ENTONCES'),
     ('left', 'OR'),
     ('left', 'AND'),
     ('right', 'NOT'),
     ('left', 'APAR', 'CPAR'),

)


def p_prog(p):
    '''prog : sentencias'''
    print ("prog")

def p_sentencias(p):
    '''sentencias : sentencias sentencia
                  | sentencia
                  | empty'''
    print ("sentencias")

def p_sentencia(p):
    '''sentencia : asig PCOMA
                 | sentwritestr PCOMA
                 | sentwritelog PCOMA
                 | sentwriteintro PCOMA
                 | sentwritetabla PCOMA'''
    print ("sentencia")

def p_expresion(p):
    '''expresion : NOT expresion
                 | expresion DOBLEENTONCES expresion
                 | expresion ENTONCES expresion
                 | expresion AND expresion
                 | expresion OR expresion
                 | NUMERO
                 | APAR expresion CPAR
                 | identificador
                 | senttauto
                 | sentcontra
                 | sentdeci'''
    print ("expresion")

def p_asig(p):
    '''asig : identificador ASIGNACION expresion'''

    print ("asignacion")

def p_identificador(p):
    '''identificador : ID'''

    print ("identificador")

def p_sentwriteintro(p):
    '''sentwriteintro : WRITEINTRO APAR CPAR'''

    print ("sentwriteintro")

def p_sentwritelog(p):
    '''sentwritelog : WRITELOG APAR expresion CPAR'''

    print ("sentwritelog")

def p_sentwritestr(p):
    '''sentwritestr : WRITESTR APAR CTEXTO CPAR'''

    print ("sentwritestr")

def p_sentwritetabla(p):
    '''sentwritetabla : WRITETABLA APAR matriz CPAR'''

    print ("sentwritetabla")

def p_matriz(p):
    '''matriz : NOT matriz
              | matriz DOBLEENTONCES matriz
              | matriz ENTONCES matriz
              | matriz AND matriz
              | matriz OR matriz
              | APAR matriz CPAR
              | identificador'''

    print ("matriz")

def p_senttauto(p):
    '''senttauto : TAUTO APAR matriz CPAR'''

    print ("senttauto")

def p_sentcontra(p):
    '''sentcontra : CONTRA APAR matriz CPAR'''

    print ("sentcontra")

def p_sentdeci(p):
    '''sentdeci : DECI APAR matriz CPAR'''

    print ("sentdeci")

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    print ("Syntax error", p)
    print ("Error en linea "+str(p.lineno))


def buscarFicheros(directorio):
    ficheros = []
    numArchivo = ''
    respuesta = False
    cont = 1

    for base, dirs, files in os.walk(directorio):
        ficheros.append(files)

    for file in files:
        print (str(cont)+". " +file)
        cont = cont+1

    while respuesta == False:
        numArchivo = input('\nNumero del test: ')
        for file in files:
            if file == files[int (numArchivo)-1]:
                respuesta = True
                break
    print ("has escogido \"%s\" \n" %files[int(numArchivo)-1])
    return files[int(numArchivo)-1]


directorio = "/Users/Madssimo/Documents/Compiladores/L-0/pruebas/"
archivo = buscarFicheros(directorio)
test = directorio+archivo
fp = codecs.open(test, "r", "utf-8")
cadena = fp.read()
fp.close

parser = yacc.yacc('SLR')
result = parser.parse(cadena)

print (result)
