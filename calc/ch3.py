

"""
WORLD POPULATION

1. Uninhibited growth
P = P0 * 2 **(t/D)

example : if t = Doubling time , then P(D) = P0 * 2 always
"""
from algo.tools import *

t = sym.symbols('t')
P0 = 2.983435 * 10 ** 9
D = 40
t0 = 1959

fun = P0 * 2 ** (t/D)

# Rate of change of pop
d_fun = d_f(fun, symbol=t)
print(d_fun)

# Rate of change of pop on 2011
d_fun_2011 = sym.lambdify(t,d_fun)(2011-t0)
print(d_fun_2011)


# Approx pop of world in 2011.
fun_2011 = sym.lambdify(t,fun)(2011-t0)
print(fun_2011)



