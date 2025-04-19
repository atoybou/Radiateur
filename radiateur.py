# -*- coding: utf-8 -*-
"""
Created on Sat Apr 19 16:06:02 2025

@author: ordin
"""

import numpy as np
import matplotlib.pyplot as plt


nx=101
ny=101
nt=1500
dx=2/(nx-1)
dy=2/(nx-1)
alpha=20
sigma=0.25
dt=sigma*dx*dy/alpha

u=5

x=np.linspace(0,2,nx)
y=np.linspace(0,2,ny)
temp=4*np.ones((nx, ny))

for i in range(nt):
    temp_n=temp.copy()
    temp[1:-1,1:-1]=temp_n[1:-1,1:-1]-u*dt/dx*(temp_n[1:-1,1:-1]-temp_n[0:-2,1:-1]) \
        - u*dt/dy*(temp_n[1:-1,1:-1]-temp_n[1:-1,0:-2]) \
        + alpha*dt/(dx**2)*(temp_n[1:-1,2:]-2*temp_n[1:-1,1:-1]+temp_n[1:-1, 0:-2]) \
        + alpha*dt/(dy**2)*(temp_n[2:,1:-1]-2*temp_n[1:-1,1:-1]+temp_n[0:-2, 1:-1])
    temp[0,:]=4
    temp[-1,:]=4
    temp[:,0]=4
    temp[:,-1]=4
    temp[int(nx/4),int(ny/20)]=50

X, Y = np.meshgrid(x, y)
fig, ax = plt.subplots()
im = ax.imshow(temp_n, interpolation="bicubic", origin="lower", extent=[0,2,0,2])
fig.colorbar(im)
plt.show()