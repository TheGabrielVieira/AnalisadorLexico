#type não ta utilizado corretamente, criar função depois.
#Faltando outra parte
from typing import Type
from Tag import tag
from Word import create_token
import sys

line = 1
peek = ' '
words = {}

def reserve(w):
    words[w.lexeme] = w

def Lexer():
    reserve(create_token("if", tag.IF))
    reserve(create_token("else", tag.ELSE))
    reserve(create_token("while", tag.WHILE))
    reserve(create_token("do", tag.DO))
    reserve(create_token("break", tag.BREAK))
    reserve(create_token("true", tag.TRUE))
    reserve(Type.Int)
    reserve(Type.Bool)
    reserve(create_token("False", tag.FALSE))
    reserve(Type.Char)
    reserve(Type.Float)

def readch():
    global peek
    peek = sys.stdin.read(1)

def readch(c):
    readch()
    if peek != c:
        return False
    peek = ''
    return True