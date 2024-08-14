

"""
Using MVT to find the point c . where a<c<b 
1. function is continous and diff in [a,b]
"""

from tools import *
x  = sym.symbols('x')

#Returns a list
def mvt(fun, a, b, symbol = 'x'):
    try :
        f_diff = d_f(fun,symbol)
        fun_a = sym.lambdify(symbol,fun)(a)
        fun_b = sym.lambdify(symbol,fun)(b)
        rise =  (fun_b - fun_a) if ( b > a) else (fun_a - fun_b)
        move =  (b - a ) if ( b > a) else (a - b )
        slope = rise / move
        return sym.solve((f_diff - slope), symbol) # It solves for eq = 0 , hence the fdiff-slope = 0
    except ZeroDivisionError: 
        print("Division by zero, check a and b")


