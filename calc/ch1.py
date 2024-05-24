
"""
Pollution in clear lake
"""
import matplotlib.pyplot as plt
import numpy as np

def plotting():
    plt.plot(x,y)
    plt.show()
def tolerance():
    x  = [2,0.5]
    return x[1]
def fine_per_yr():
    y  = [100000,200000]
    return y[1]
def plot_table(x,y, Tolerance = 2):
    for i in range(0,x.size):
        if( y[i] <= Tolerance):
            return x[i]
        else: 
            print("t: ",x[i],end='')
            print("||",end='')
            print(" PPM:",y[i])
x = np.arange(0,100,1)
y = (0.8)**x*10 # 20% decrease each year

Tolerance = tolerance()
f_p_y = fine_per_yr()
t = plot_table(x,y, Tolerance)
# Fine 
fine = t*f_p_y
print("Fine : ", fine)
# Plotting 
plotting()
