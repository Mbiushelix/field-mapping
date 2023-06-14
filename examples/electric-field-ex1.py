# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


k_e = 8.99*10e9
e = 1.6*10e-16
n_points = 30

plt.rcParams['figure.figsize'] = [12, 12]
plt.style.use("dark_background")

# (x,y,c) where c is the charge given as a whole number
def plates(n, x, y):
    plate1 = [(x + 0.1*l,y, -5) for l in range(n)]
    plate2 = [(x + 0.1*m,y + 5, 5) for m in range(n)]
    return plate1 + plate2

charges = plates(20,4,2.5)


def vector_field(): 
    # Const pointfield
    x,y = np.meshgrid(np.linspace(0,10,n_points),np.linspace(0,10,n_points))
    
    # Calc vectors for pointfield
    for i, charge in enumerate(charges):
        if i == 0:
            u = k_e * (1/((x-charges[0][0])**2 + (y-charges[0][1])**2)) * charges[0][2] * (x-charges[0][0])
            v = k_e * (1/((x-charges[0][0])**2 + (y-charges[0][1])**2)) * charges[0][2] * (y-charges[0][1])
        else: 
            u += k_e * (1/((x-charge[0])**2 + (y-charge[1])**2)) * charge[2] * (x-charge[0])
            v += k_e * (1/((x-charge[0])**2 + (y-charge[1])**2)) * charge[2] * (y-charge[1])
            
    # Normalize vectors         
    values = np.array([np.sqrt(u0**2 + v0**2) for (u0,v0) in zip(u,v)])
    u = u/values 
    v = v/values
    
    # Plot vectorfield
    plt.quiver(x,y,u,v, color = "black")


def field():
    # Const pointfield 
    x0, y0 =  np.meshgrid(np.linspace(0,10,200), np.linspace(0,10,200))
    
    # Calc fieldstrength for pointfield
    
    for i, charge in enumerate(charges):
        if i == 0:
            u0 = k_e * (1/((x0-charges[0][0])**2 + (y0-charges[0][1])**2)) * charges[0][2] * (x0-charges[0][0])
            v0 = k_e * (1/((x0-charges[0][0])**2 + (y0-charges[0][1])**2)) * charges[0][2] * (y0-charges[0][1])
        else: 
            u0 += k_e * (1/((x0-charge[0])**2 + (y0-charge[1])**2)) * charge[2] * (x0-charge[0])
            v0 += k_e * (1/((x0-charge[0])**2 + (y0-charge[1])**2)) * charge[2] * (y0-charge[1])
            
    value0 = np.array([np.sqrt(l**2 + m**2) for (l,m) in zip(u0, v0)])
    value0 = np.log(value0)
    
    # Plot field
    extent = np.min(x0), np.max(x0), np.min(y0), np.max(y0)
    plt.imshow(value0, cmap='gnuplot2', interpolation="quadric",extent= extent, origin = "lower")
    cbar = plt.colorbar(fraction=0.046,pad=0.04)
    cbar.set_label('Electric field strength in logarithmic scale ($log(N/C)$)', labelpad=15)

# Vectorfield and heatmap
vector_field()
field()

# Customize point-particles
for charge in charges: 
    color = 'r' if charge[2] > 1 else 'b'
    plt.scatter(charge[0], charge[1], c=color)

# Plot custom
red_patch = mpatches.Patch(color='red', label='Positive charge (point charge)')
blue_patch = mpatches.Patch(color='blue', label='Negative charge (point charge)')
plt.legend(handles=[red_patch,blue_patch])

plt.title("Electric field around point charges", pad=15)
plt.tick_params(left = False, right = False , labelleft = False ,
                labelbottom = False, bottom = False)
plt.show()