
"""
Unemployement and GDP : 

"""


from algo.tools import *
from algo.plotting import *


#t = sym.symbols('t')

t = np.arange(0,25,0.5)
u_t = 5*np.cos(2*t/np.pi)/ (2 + np.sin(2*t/np.pi)) + 6 

gdp_t = 5*np.cos(2*t/np.pi + 5) + 2 


plotting(t, gdp_t)
