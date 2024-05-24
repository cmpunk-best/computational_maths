
"""
Lunar Module 
"""
import sympy as sym

def d_f(fun, symbol = 't', times = 1):
    return sym.diff(fun, symbol, times)



Rt, Vt, At, JA , SA , t = sym.symbols('Rt Vt At Jt St t')

r_r = Rt + Vt*t + 0.5*At*t**2 + (1/6.0)*JA*t**3 + (1/24.0)*SA*t**4

r_r1 = sym.lambdify(t,r_r)
v_r, a_r, j_r, s_r = [sym.lambdify(t,d_f(r_r,times=1)) , sym.lambdify(t,d_f(r_r,times=2)), sym.lambdify(t,d_f(r_r,times=3)) , sym.lambdify(t,d_f(r_r,times=4))]

#print(r_r1(0))
#print(v_r(0))
#print(a_r(0))
#print(j_r(0))
#print(s_r(0))

print(d_f(r_r,times=1))
print(d_f(r_r,times=2))
