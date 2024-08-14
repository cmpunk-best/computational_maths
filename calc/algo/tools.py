
"""

CONTAINS BASIC TOOLS AND IMPORTS 

Imports
Differentiation 
Integration
"""


import sympy as sym
import numpy as np

def d_f(fun, symbol = 'x', times = 1):
    return sym.diff(fun, symbol, times)

def int_f(fun, symbol = 'x', a =0, b=1):
    return sym.integrate(fun, (symbol,a , b))


class IntegralValueZeroError(Exception):
    pass
def sum_at_all_n_points_1(func, symbol,a,b,n,delta_x):
    total = 0 
    for i in range(1,n):
        total = total + sym.lambdify(symbol, func)(i*(delta_x) + a)

    return 2*total + sym.lambdify(symbol, func)(a) + sym.lambdify(symbol, func)(b)
def sum_at_all_n_points_2(func, symbol,a,b,n,delta_x):
    even_tot = 0
    odd_tot  = 0
    for i in range(1,n):
        if i%2 == 0:
            even_tot = even_tot + sym.lambdify(symbol,func)(i*(delta_x) + a)
        else:
            odd_tot = odd_tot + sym.lambdify(symbol,func)(i*(delta_x) + a)
    return 2*even_tot + 4*odd_tot + sym.lambdify(symbol, func)(a) + sym.lambdify(symbol, func)(b)
# Trapezoidal method
def numerical_integral_1(func, n = 10, symbol='x', a=0 , b=0 ):
    try:
        if a == b : 
            raise IntegralValueZeroError(" Value of a and b are same")
        delta_x = (b - a)/n if (b > a) else (a - b)/n
    except ZeroDivisionError:
        print(" n cannot be 0")
    else:
        return delta_x/2 * (sum_at_all_n_points_1(func,symbol,a,b,n,delta_x))
# Simpson Method
def numerical_integral_2(func , n = 10 , symbol = 'x', a =0 , b=0):
    try :
        if a == b : 
            raise IntegralValueZeroError(" Value of a and b are same")
        delta_x = (b - a)/n if (b > a) else (a - b)/n
    except ZeroDivisionError:
        print(" n cannot be 0")
    else:
        return delta_x/3 * (sum_at_all_n_points_2(func,symbol,a,b,n,delta_x))

        

#x = sym.symbols('x')
#func = sym.sin(x)/x
#print(f'Integral approx value trap {numerical_integral_1(func,a=22/7,b=44/7,n =4)}')
#print(f'Integral approx value simp {numerical_integral_2(func,a=22/7,b=44/7,n =4)}')
#print(f'Integral actual value {int_f(func,a=1,b=2)}')



