# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 12:27:55 2023

@author: Yudhish
"""

import numpy as np
import matplotlib.pyplot as plt

plt.style.use("dark_background")
fig, (ax2, ax3) = plt.subplots(1,2, figsize=(10,4))

# Placing Ar in the center and assigning relevent values for Ar
atom = (5,5)
epsilon = 0.997*10**3
sigma = 3.4

def LJ_potential_calculation1D(r):
    return 4*epsilon*((sigma/r)**12 - (sigma/r)**6)


def LJ_potential_calculation2D(a1,a2):
    r = np.sqrt((a1[0]-a2[0])**2 + (a1[1]-a2[1])**2)
    return 4*epsilon*((sigma/r)**12 - (sigma/r)**6)

def field():
    x0, y0 =  np.meshgrid(np.linspace(0,10,200), np.linspace(0,10,200))
    value0 = np.array([LJ_potential_calculation2D(atom,(x,y)) for (x,y) in zip(x0,y0)])
    
    for l, row in enumerate(value0):
        for m, value in enumerate(row):
            if value > 0: 
                value0[l,m] = np.log(m)
    
    extent = np.min(x0), np.max(x0), np.min(y0), np.max(y0)
    pcm = ax3.imshow(value0, cmap='gnuplot2', interpolation="quadric",extent= extent, origin = "lower")
    cbar = fig.colorbar(pcm,fraction=0.046,pad=0.04, ax = ax3)
    cbar.set_label('$log(kJ/mol)$ when $E_p>0$ else $kJ/mol$', labelpad=15)
 

ax3.add_patch(plt.Circle((5, 5), 0.98, color='r', fill = False, linestyle='--', label = "Ar størrelse"))
ax3.plot([5,5+0.98], [5,5],linestyle='--')
ax3.text(5,5.1,r"$r = 0.98Å$",style='italic',fontsize = 8, c = "black")



ax2.set_xlabel("Angstrom(Å)")
ax3.set_xlabel("Angstrom(Å)")
ax3.set_ylabel("Angstrom(Å)")
ax2.set_ylabel("$kJ/mol$")
x_values = np.linspace(3,6,100)
y_values = list(map(LJ_potential_calculation1D,x_values))
field()

plt.show()