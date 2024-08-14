


"""
Finding the volume using disk method

BY USERS : 
    For volume under x axis
    1. Need to provide a , b [Sometimes may be need to find point of intersections]

    For volume under y axis
    1. Need to provide the func in terms of y if need the y axis volume.
        a. Change symbol for volume on the y axis 
        b. find a , b for y axis
"""

from tools import *

"""
Volume using disk method 
<<EASIER FOR HORIZONTAL AXIS>>
"""
def disk_volume_f(func, symbol='x', a=0, b=1):
    return np.pi*int_f(func**2,symbol, a , b)

"""
Volume using washer method between 2 func's
<<EASIER FOR HORIZONTAL AXIS>>
"""
def washer_volume_2f(func1,func2, symbol='x', a=0 , b=1):
    return np.pi*int_f(func1**2 - func2**2,symbol, a , b)

#SHELL METHOD for y axis rotation 
# FUNC = basically height
"""
Volume using shell method between 2 func's
<<EASIER FOR VERTICAL AXIS ROTATION >>
V = 2*pi*avg_radius *Thickness* height(which is f(x) or (f(x) - g(x))
V = integrate(xf(x)dx)(a,b) 
"""

def shell_volume_f(func ,symbol='x', a=0 , b=1):
    return 2*np.pi*int_f(x*func,symbol, a , b)

#x = sym.symbols('x')
#print(shell_volume_f((12-x-x**2),a=1,b=3))

