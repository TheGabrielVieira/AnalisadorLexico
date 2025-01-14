from lexer import Token
from symbols import Type

def create_arith(tok, x1, x2):
    def arith():
        nonlocal tok, x1, x2
        expr1 = x1
        expr2 = x2
        type = Type.max(expr1["type"], expr2["type"])
        if type is None:
            error("type error")
        return {
            "tok": tok,
            "expr1": expr1,
            "expr2": expr2,
            "type": type,
            "gen": gen,
            "__str__": __str__
        }
    
    def gen():
        return create_arith(tok, expr1["gen"](), expr2["gen"]())
    
    def __str__():
        return str(expr1) + " " + str(tok) + " " + str(expr2)
    
    return arith()

def error(s):
    raise Error(s)  # Substitua Error com a implementação real de erro

def emit(s):
    print("\t" + s)

