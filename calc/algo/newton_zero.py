

"""
Newton method for finding zeros
1. Recursive method.
2. Finding initial guess (c1)
3. Finding c2 from eq
    y - f(c1) = f'(c1) * (x - c1)
    plug y = 0
    -f(c1) = f'(c1) * (c2-c1)
    c1 - f(c1)/f'(c1) = c2 
    Basically,
    c_n = c_n-1 - f(c_n-1)/f'(c_n-1)
    c_n+1 = c_n - f(c_n)/f'(c_n)

4. Guessing c_n-1 is the toughest part
"""
"""
TODO : Finding 2 values which have opposite values , so that IMV proves that there is a real zero that exists
"""


from tools import *

def newton_zero(fun,c_n,symbol='x'):
    if(sym.lambdify(symbol,fun)(c_n) <= 0.002):
        return c_n
    else:
        c_n_1 = c_n - (sym.lambdify(symbol,fun)(c_n)/sym.lambdify(symbol,d_f(fun))(c_n))
        return newton_zero(fun,c_n_1)

# Functions
#x = sym.symbols('x')
#fun = x**3 + x**2 - x - 2 
#print("Final zero value = " ,newton_zero(fun, c_n=1.5))










